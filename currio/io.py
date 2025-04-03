import re

import pyvista as pv
from vtkmodules.vtkCommonCore import vtkCommand
from vtkmodules.vtkInteractionWidgets import vtkHoverWidget
from vtkmodules.vtkRenderingCore import vtkPointPicker

from currio.neuron import Neuron, format_field_key
from currio.sensor import Sensor
from currio.diamond import NV

from currio.compiled import get_odmr_shifts

from currio import __resultpath__

import datetime
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class IO:
    def __init__(self, *objects):
        """An object to handle input and output of neurons and sensors simulations.
        Can load, save, and also visualize neurons together with sensors.

        Initialize with optional objects (sensors and neuron) to input/output."""
        self.neurons = []
        self.sensors = []
        # Set active neuron and sensor to last added by default
        self._active_neuron_idx = -1  
        """Internal attribute to point to the last active neuron, by default. Changed by 
        `.set_active_neuron()` method."""
        self._active_sensor_idx = -1  
        """Internal attribute to point to the last active sensor, by default. Changed by 
        `.set_active_sensor()` method."""
        
        for obj in objects:
            self.add(obj)
            
    @property
    def objects(self):
        """All neurons and sensors in the IO instance."""
        return self.neurons + self.sensors

    @property
    def neuron(self):
        """Active neuron - defaults to last added neuron."""
        if not self.neurons:
            return None
        return self.neurons[self._active_neuron_idx]

    @property
    def sensor(self):
        """Active sensor - defaults to last added sensor."""
        if not self.sensors:
            return None
        return self.sensors[self._active_sensor_idx]

    def set_active_neuron(self, neuron=None):
        """Set active neuron by index, ID, or object.
        
        Args:
            neuron: Integer index, model ID string, Neuron object, or None for last
        Returns:
            self: For method chaining
        """
        if neuron is None:
            self._active_neuron_idx = -1
        elif isinstance(neuron, int) and -len(self.neurons) <= neuron < len(self.neurons):
            self._active_neuron_idx = neuron
        elif isinstance(neuron, str):
            try:
                self._active_neuron_idx = [n.id for n in self.neurons].index(neuron)
            except ValueError:
                raise ValueError(f"No neuron found with model ID {neuron}")
        elif neuron in self.neurons:
            self._active_neuron_idx = self.neurons.index(neuron)
        else:
            raise ValueError("Invalid neuron specification")
        return self

    def set_active_sensor(self, sensor=None):
        """Set active sensor by index, ID, or object.
        
        Args:
            sensor: Integer index, sensor ID string, Sensor object, or None for last
        Returns:
            self: For method chaining
        """
        if sensor is None:
            self._active_sensor_idx = -1
        elif isinstance(sensor, int) and -len(self.sensors) <= sensor < len(self.sensors):
            self._active_sensor_idx = sensor
        elif isinstance(sensor, str):
            try:
                self._active_sensor_idx = [s.id for s in self.sensors].index(sensor)
            except ValueError:
                raise ValueError(f"No sensor found with ID {sensor}")
        elif sensor in self.sensors:
            self._active_sensor_idx = self.sensors.index(sensor)
        else:
            raise ValueError("Invalid sensor specification")
        return self

    def __repr__(self):
        """Show summary of loaded neurons and sensors."""
        # Handle neuron count
        n_neurons = len(self.neurons)
        if n_neurons == 0:
            neuron_header = "0 Neurons"
        elif n_neurons == 1:
            neuron_header = "1 Neuron"
        else:
            neuron_header = f"{n_neurons} Neurons"
        
        neuron_info = []
        for n in self.neurons:
            # Handle record count
            n_records = len(n.records) if hasattr(n, 'records') else 0
            if n_records == 0:
                record_str = "0 Records"
            elif n_records == 1:
                record_str = "1 Record"
            else:
                record_str = f"{n_records} Records"
            
            neuron_info.append(n.__repr__())
            
        # Handle sensor count
        n_sensors = len(self.sensors)
        if n_sensors == 0:
            sensor_header = "0 Sensors"
        elif n_sensors == 1:
            sensor_header = "1 Sensor"
        else:
            sensor_header = f"{n_sensors} Sensors"
            
        sensor_info = []
        for s in self.sensors:
            bounds = np.array(s.bounds).reshape(3,2)
            sensor_info.append(
                f"Sensor `{s.id}` with {s.n_points} points in bounds "
                f"x=[{bounds[0,0]:.1f}, {bounds[0,1]:.1f}], "
                f"y=[{bounds[1,0]:.1f}, {bounds[1,1]:.1f}], "
                f"z=[{bounds[2,0]:.1f}, {bounds[2,1]:.1f}] um"
            )
            
        return (
            f"IO with:\n"
            f"{neuron_header}:\n  " + 
            "\n  ".join(neuron_info) + "\n" +
            f"{sensor_header}:\n  " + 
            "\n  ".join(sensor_info)
        )
        
    def show(self):
        """Show the plotter."""
        self.plotter.show()

    def plot(self, *objects, show=True, **kwargs):
        """Plot neurons and sensors. Delegates to module-level plot function."""
        objects = self.neurons + self.sensors + list(objects)
        plotter = plot(*objects, **kwargs, show=show)
        self.plotter = plotter
        return plotter
    
    def add_picker(self):
        """Add a picker to the plotter."""
        if self.plotter is None:
            raise ValueError("No plotter to add picker to.")
        elif self.plotter.iren is None:
            self.plotter.iren.initialize()
        self.plotter = add_picker(self.plotter)
        return self.plotter
    
    def save(self):
        self.__class__.save(*self.neurons, *self.sensors)
    
    @classmethod
    def save(cls, *objects):
        """Save neurons and their associated sensors to disk.
        
        Creates a flat structure:
        results/
        ├── 144976.json              # Records for model 144976
        ├── 144976.vtk               # Sensor data for single model
        ├── 144976+144977.vtk        # Sensor data for multiple models
        └── 001-2af-20240216-12-00-01.txt     # Save description and references
        
        The .txt file format:
        ```
        # Generated on 2024-02-16 15:30:45
        
        [Description]
        LTP study comparing models
        User provided description here
        
        [Records]
        144976_3  # {model id}_{record index}
        144977_2
        
        [Sensor]
        file: 144976+144977.vtk
        fields:
        - B_total
        - B_144976_3  # B_{model id}_{record index}
        - B_144977_1
        - B_144977_2
        - B_144976_3+144977_1  # combination
        ```
        """
        resultspath = __resultpath__
        resultspath.mkdir(exist_ok=True)
        
        neurons = []
        sensors = []
        
        # Save individual objects
        for obj in objects:
            if isinstance(obj, Neuron):
                cls._save_neuron(obj, resultspath)
                neurons.append(obj)
            elif isinstance(obj, Sensor):
                cls._save_sensor(obj, resultspath)
                sensors.append(obj)
        
        # Create bundle file if any objects were saved
        if len(neurons) + len(sensors) > 0:
            cls._save_bundle(neurons, sensors, resultspath)
        
        return cls(*objects)
    
    @classmethod
    def _save_neuron(cls, neuron, resultspath):
        """Save a neuron's records to JSON."""
        records = [make_serializable(record) for record in neuron.records]
        
        with open(resultspath / f"{neuron.id}.json", "w") as f:
            json.dump(records, f, indent=2)
        print(f"Saved records for Neuron {neuron.id} to {resultspath / f'{neuron.id}.json'}")

    @classmethod
    def _save_sensor(cls, sensor, resultspath):
        """Save a sensor to VTK file."""
        sensor.save(resultspath / f"{sensor.id}.vtk")
        print(f"Saved data for Sensor {sensor.id} to {resultspath / f'{sensor.id}.vtk'}")

    @classmethod
    def _save_bundle(cls, neurons, sensors, resultspath):
        """Save a bundle description file."""
        # Generate a name based on the number of description files
        io_id = f"{len(list(resultspath.glob('???-*.txt')))+1:03d}"
        
        # Create a description file
        io_name = io_id + "-" + "-".join([o.id for o in sensors + neurons]) \
            + "-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        
        io_filename = resultspath / f"{io_name}.txt"
        
        with open(io_filename, "w") as f:
            f.write(f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Neurons: {', '.join([o.id for o in neurons])}\n")
            f.write(f"Sensors: {', '.join([o.id for o in sensors])}\n")
        
        print(f"Saved io file to {io_filename}")

    def load(self, save_id):
        """Instance method version of load."""
        loaded = self.__class__.load(save_id)
        self.neurons.extend(loaded.neurons)
        self.sensors.extend(loaded.sensors)
        self.neuron = loaded.neuron
        self.sensor = loaded.sensor
        return self        

    @classmethod
    def load(cls, save_id):
        """Load a saved simulation by ID.
        
        Handles different ID formats:
        - "55035" or 55035 -> Load neuron from results/55035.json
        - "b0c" -> Load sensor from results/*b0c*.vtk
        - "001" or 1 -> Load bundle from results/001-*.txt
        
        Args:
            save_id (str or int): ID to load. Format determines what's loaded:
                - ModelDB ID (>4 digits): loads neuron
                - Sensor ID (alphanumeric): loads sensor
                - Short numeric ID (3 digits): loads bundle
        
        Returns:
            Union[Neuron, Sensor, IO]: Single object or IO instance with multiple objects
        """
        results = __resultpath__
        save_id = str(save_id)
        
        # Case 1: ModelDB ID (neuron)
        if save_id.isdigit() and len(save_id) > 4:
            return cls._load_neuron(save_id)
        
        # Case 2: Short numeric ID (bundle)
        if save_id.isdigit() and len(save_id) <= 3:
            save_id = f"{int(save_id):03d}"
            bundle_files = list(results.glob(f"{save_id}*.txt"))
            if bundle_files:
                return cls._load_bundle(bundle_files[0])
            raise FileNotFoundError(f"No bundle found for ID: {save_id}")
        
        # Case 3: Sensor ID
        sensor_files = list(results.glob(f"*{save_id}*.vtk"))
        if sensor_files:
            return cls._load_sensor(sensor_files[0], save_id)
        
        raise FileNotFoundError(f"No files found matching ID: {save_id}")

    @classmethod
    def _load_neuron(cls, model_id):
        """Load a neuron from its JSON file."""
        neuron_file = __resultpath__ / f"{model_id}.json"
        if not neuron_file.exists():
            raise FileNotFoundError(f"No records for model {model_id}")
        
        with open(neuron_file) as f:
            records = json.load(f)
        
        # Convert loaded data back to proper types, i.e. lists to numpy arrays
        records = [unmake_serializable(record) for record in records]
        
        neuron = Neuron(model_id)
        neuron.records = records
        print(f"Loaded: {neuron}")
        return neuron

    @classmethod
    def _load_sensor(cls, sensor_file, sensor_id):
        """Load a sensor from its VTK file."""
        sensor = pv.read(sensor_file)
        sensor_obj = Sensor(sensor.points)
        sensor_obj.point_data.update(sensor.point_data)
        sensor_obj.field_data.update(sensor.field_data)
        sensor_obj.id = sensor_id
        print(f"Loaded: {sensor_obj}")
        return sensor_obj

    @classmethod
    def _load_bundle(cls, desc_file):
        """Load a bundle of neurons and sensors from description file."""
        with open(desc_file) as f:
            lines = f.readlines()
        
        neurons = []
        sensors = []
        
        for line in lines:
            if line.startswith("Neurons:"):
                neuron_ids = [n.strip() for n in line.split(":")[1].split(",")]
                for nid in neuron_ids:
                    if nid:  # Skip empty strings
                        try:
                            neurons.append(cls._load_neuron(nid))
                        except FileNotFoundError as e:
                            print(f"Warning: {e}")
                            
            elif line.startswith("Sensors:"):
                sensor_ids = [s.strip() for s in line.split(":")[1].split(",")]
                for sid in sensor_ids:
                    if sid:  # Skip empty strings
                        sensor_files = list(__resultpath__.glob(f"*{sid}*.vtk"))
                        if sensor_files:
                            sensors.append(cls._load_sensor(sensor_files[0], sid))
                        else:
                            print(f"Warning: No sensor file found for ID {sid}")
        
        if len(neurons) + len(sensors) == 0:
            raise FileNotFoundError("No objects found in bundle")
        elif len(neurons) + len(sensors) == 1:
            return neurons[0] if neurons else sensors[0]
        
        return cls(*(neurons + sensors))

    def add(self, *objects):
        """Add objects to the IO instance."""
        for obj in objects:
            if isinstance(obj, Neuron):
                self.neurons.append(obj)
            elif isinstance(obj, Sensor):
                self.sensors.append(obj)

    def plot_var(self, variable_spec, t=None, 
                  source="neuron",
                  figsize=(10, 5), backend='matplotlib',
                  ):
        """Plot variables from neuron model records using flexible section/segment specification.
    
        Args:
            *variable_specs: Strings specifying variables to plot. Format:
                            "section_pattern[index](segment_pos).variable_name"
                            - section_pattern: Name of section (soma, dendrite, etc.), can include '*' wildcard
                            - [index]: Optional index of section if multiple sections match pattern
                            - (segment_pos): Optional position along section (0-1)
                            - variable_name: Name of variable to plot (v, currents, etc.)
                            
                            Examples:
                            - "soma[0].*.currents" - All currents in all segments of soma[0]
                            - "apical_dendrite[6](0.5).currents" - Currents at middle (0.5) of apical_dendrite[6]
                            - "dendrite*.*.v" - Voltage in all segments of all dendrite sections
            
            t: Optional tuple (start_time, end_time) to limit plot range
            source: 'neuron' or 'sensor' to specify source of variables
            figsize: Figure size for matplotlib plots
            backend: 'matplotlib' or 'vedo' for visualization
            
        Returns:
            matplotlib.figure.Figure or vedo.Plotter object
        """
        if t is None:
            t = slice(None)
        
        if source == "neuron":
            neuron = self.neuron
            
            # Regex to match: section_name(segment_pos).variable_name, e.g.
            # "soma(0.5).v" or "dendrite[11](0.5).v"
            pattern = r"([\w\[\d+\]]+)\(([0-9\.]+)\)\.(.+)"
            match = re.match(pattern, variable_spec)
            
            section, segment, variable = match.groups()
            
            # Turn segment specification as (0.3) to an index into the segment
            if segment is not None:
                # TODO: Make indexing along the length rather than the heuristics
                # based on the float value. It should check which segment contains 
                # that float point along the length of the section, and optionally
                # interpolate the value at that point. 
                # x ---- x ---- x 
                # 0      0.5       1
                # 
                # x -- x -- x -- x -- x
                # 0  0.25  0.5  0.75  1
                # Usually NEURON segments the section into odd number of segments,
                # so that the middle is always at 0.5. 
                xs = np.linspace(0, 1, len(neuron.record[section][variable]))
                # Find index of the segment that contains the point
                segment = np.argmin(np.abs(xs - float(segment)))
                # TODO: Interpolate the value at that point if the segment is not exactly
                # at the point.
            else:
                raise NotImplementedError("Segment specification not implemented yet")
            
            vals = neuron.record[section][variable][segment, t]
            ts = neuron.record["t"][t]
            if backend == 'matplotlib':
                fig, ax = plt.subplots()
                ax.plot(ts, vals)
                return fig

    def extract_field_timeseries(self, point_indices, field_type='B', neuron_id=None):
        """Extract a time series of a field from the sensor.
        
        Args:
            point_indices: Single index or array of indices for points to extract
            field_type: Type of field to extract (e.g., 'B' for magnetic field)
            neuron_id: ID of neuron to extract data for. If None, uses first available neuron.
        """
        if neuron_id is None:
            neuron_id = self.neuron.id
        return extract_field_timeseries(self.sensor, point_indices, field_type, neuron_id)
    
    def plot_pt_timeseries(self, point_indices, sensor=None,field_type='B', neuron_id=None, 
                           map_fn=None, map_fn_kwargs=None, figsize=(10, 5), backend='matplotlib'):
        """Plot a time series of a field from the sensor.
        
        Args:
            point_indices: Single index or array of indices for points to extract
            sensor: Sensor object to use. If None, uses self.sensor.
            field_type: Type of field to extract (e.g., 'B' for magnetic field)
            neuron_id: ID of neuron to extract data for. If None, uses first available neuron.
            map_fn: Function to apply to the time series, signature: map_fn(b_field_ts, **map_fn_kwargs)
            map_fn_kwargs: Keyword arguments for map_fn, can reference self.attributes 
                with strings `self.attribute`, e.g. for map_fn = get_odmr_shifts,
                map_fn_kwargs = {'nv_axes': 'self.diamond.nv.axes', 'gamma': 'self.diamond.gamma'} or
                directly passing them as `map_fn_kwargs = {'nv_axes': diamond.nv.axes, 'gamma': diamond.gamma}`
            figsize: Tuple of width and height for the plot.
            backend: 'matplotlib' or 'vedo', default is 'matplotlib'. `vedo` is an interactive backend and needs
                to be installed separately.
        """
        if neuron_id is None:
            neuron_id = self.neuron.id
        
        if field_type is None:
            field_type = 'B'
            
        if sensor is None:
            sensor = self.sensor
            
        # Extract field time series
        time_points, values = self.extract_field_timeseries(point_indices, field_type, neuron_id)
        
        # Apply mapping function if provided
        if map_fn is not None:
            map_fn_kwargs = map_fn_kwargs or {}
            
            # Process self-referential arguments
            for key, value in list(map_fn_kwargs.items()):
                if isinstance(value, str) and value.startswith('self.'):
                    attr_path = value[5:]
                    map_fn_kwargs[key] = getattr(self, attr_path)
            
            # Apply the function (will need to handle each point separately)
            transformed_values = np.zeros((values.shape[0], values.shape[1], 
                                        map_fn(values[0, 0]).shape[0] if values.shape[1] > 0 else 0))
            
            for p_idx in range(values.shape[1]):
                transformed_values[:, p_idx] = map_fn(values[:, p_idx], **map_fn_kwargs)
            
            values = transformed_values
        
        # Get point coordinates for labels
        points_coords = [self.sensor.points[idx] for idx in point_indices]
        
        # For ODMR shifts, use different labels
        if map_fn == get_odmr_shifts:
            try:
                nv_axes = self.diamond.nv.axes
                value_labels = [f'NV Axis {i+1}' for i in range(nv_axes.shape[0])]
                colors = ['r', 'g', 'b', 'purple']
                y_label = 'Frequency Shift (Hz)'
            except AttributeError:
                value_labels = [f'{field_type}_{i}' for i in ['x', 'y', 'z']]
                colors = ['r', 'g', 'b']
                y_label = f'{field_type} Field'
        else:
            value_labels = [f'{field_type}_{i}' for i in ['x', 'y', 'z']]
            # Define colorblind-safe categorical colors
            colors = sns.color_palette('husl', n_colors=len(value_labels))
            values = values * 1e9  # convert to pT, because values are in mT, if it's a field
            y_label = f'{field_type} field, pT'
        
        # Create visualization based on backend
        if backend.lower() == 'matplotlib':
            fig, ax = plt.subplots()
            for i in range(values.shape[1]):
                ax.plot(time_points, values[:, i], label=value_labels[i],
                        color=colors[i])
            ax.set_xlabel('Time, ms')
            ax.set_ylabel(y_label)
            ax.legend()
            return fig
            
        elif backend.lower() == 'vedo':
            # Create interactive vedo visualization
            try:
                import vedo
            except ImportError:
                raise ImportError("vedo is not installed. Please install it separately.")
            
            # Create a plotter
            pl = vedo.Plotter(title=f"Time Series for Multiple Points ({field_type})")
            
            # Calculate offsets for better visualization
            z_offset = np.max(np.abs(values)) * 0.3 if values.size > 0 else 1.0
            y_offset = z_offset  # Use same scale for y
            
            # Create axes
            axes = vedo.Axes(
                xrange=(np.min(time_points), np.max(time_points)),
                yrange=(0, (len(point_indices)+1) * y_offset),
                zrange=(np.min(values) if values.size > 0 else -1, 
                    np.max(values) if values.size > 0 else 1),
                xtitle="Time (ms)",
                ytitle="Point Index",
                ztitle=y_label
            )
            pl.add(axes)
            
            # Add lines for each point and value component
            for p_idx, point_idx in enumerate(point_indices):
                point_coord = self.sensor.points[point_idx]
                y_baseline = (p_idx + 1) * y_offset
                
                # Add point label
                label = vedo.Text3D(
                    f"Pt {point_idx}\n({point_coord[0]:.1f}, {point_coord[1]:.1f}, {point_coord[2]:.1f})",
                    pos=(np.min(time_points), y_baseline, np.min(values) if values.size > 0 else 0),
                    s=0.4,
                    c="black"
                )
                pl.add(label)
                
                # Plot each component/axis
                for v_idx in range(values.shape[2] if values.ndim > 2 else values.shape[1]):
                    color = colors[v_idx % len(colors)]
                    
                    if values.ndim > 2:
                        y_data = values[:, p_idx, v_idx]
                    else:
                        y_data = values[:, v_idx]
                    
                    # Create points for the line
                    points = np.column_stack((time_points, np.full_like(time_points, y_baseline), y_data))
                    
                    # Create the line
                    line = vedo.Line(points, c=color, lw=3)
                    pl.add(line)
                    
                    # Add a marker at the first point with label
                    if p_idx == 0:  # Only add legend for first point
                        marker = vedo.Sphere(r=z_offset*0.05, c=color)
                        marker.pos(points[0])
                        pl.add(marker)
                        
                        # Add label
                        text = vedo.Text3D(
                            value_labels[v_idx], 
                            pos=(points[0][0], points[0][1], points[0][2] + z_offset*0.1),
                            s=0.3, 
                            c=color
                        )
                        pl.add(text)
                    
                    # Add vertical lines connecting to baseline
                    for t_idx in range(0, len(time_points), len(time_points)//10):
                        connector = vedo.Line(
                            [time_points[t_idx], y_baseline, 0],
                            [time_points[t_idx], y_baseline, y_data[t_idx]],
                            c='gray', alpha=0.3, lw=1
                        )
                        pl.add(connector)
            
            # Set camera position for a good initial view
            pl.camera.SetPosition(
                np.mean(time_points), 
                -len(point_indices) * y_offset, 
                np.max(values) * 2 if values.size > 0 else 2
            )
            pl.camera.SetFocalPoint(
                np.mean(time_points), 
                np.mean(range(len(point_indices))) * y_offset,
                0
            )
            
            return pl
        
        else:
            raise ValueError(f"Unsupported backend: {backend}. Use 'matplotlib' or 'vedo'.")

def make_serializable(obj):
    """Convert a dictionary with arbitrary objects into a JSON-serializable dict.
    
    Handles:
    - numpy arrays/types -> lists/python types
    - NEURON objects -> string representations
    - datetime objects -> ISO format strings
    - objects with 'to_dict' method -> call method
    - objects with 'id' attribute -> use id
    - other objects -> str(obj)
    """
    if isinstance(obj, dict):
        return {key: make_serializable(value) for key, value in obj.items()}
        
    elif isinstance(obj, (list, tuple)):
        return [make_serializable(item) for item in obj]
        
    elif hasattr(obj, 'to_dict'):  # Custom serializable objects
        return make_serializable(obj.to_dict())
        
    elif hasattr(obj, 'id'):  # Objects with IDs
        return obj.id
        
    elif 'numpy' in str(type(obj)):  # Numpy arrays and types
        return obj.tolist() if hasattr(obj, 'tolist') else obj.item()
        
    elif isinstance(obj, datetime.datetime):
        return obj.isoformat()
        
    elif isinstance(obj, (int, float, str, bool, type(None))):
        return obj
        
    return str(obj)  # Fallback for other types

def unmake_serializable(obj):
    """Convert JSON-serialized data back into numpy arrays.
    
    Handles:
    - Lists that should be numpy arrays
    - Nested dictionaries
    - Special keys that indicate array data
    """
    if isinstance(obj, dict):
        # Handle record dictionary
        result = {}
        for key, value in obj.items():
            if key in ["v", "currents", "interp_v", "t"]:  # Keys that should be arrays
                result[key] = np.array(value)
            else:
                result[key] = unmake_serializable(value)
        return result
    elif isinstance(obj, list):
        # Check if this list should be an array (contains numeric data)
        if obj and all(isinstance(x, (int, float)) or 
                      (isinstance(x, list) and all(isinstance(y, (int, float)) for y in x)) 
                      for x in obj):
            return np.array(obj)
        return [unmake_serializable(x) for x in obj]
    return obj


def extract_field_timeseries(sensor, point_indices, field_type, neuron_id=None):
    """
    Efficiently extract magnetic field time series for one or more sensor points.

    Args:
        sensor: Sensor object containing magnetic field data
        point_indices: Single index or array of indices for points to extract
        neuron_id: ID of neuron to extract data for. If None, uses first available neuron.
        
    Returns:
        tuple: (time_points, b_field_ts) where:
            - time_points: array of time points (ms)
            - b_field_ts: array of shape (n_time_points, n_points, 3) with magnetic field vectors
    """
    # Get time points
    time_points = sensor.field_data["t"]
    n_time_points = len(time_points)

    # Handle neuron_id selection
    if neuron_id is not None:
        if isinstance(neuron_id, int) and "neuron_ids" in sensor.field_data:
            try:
                neuron_id = sensor.field_data["neuron_ids"][neuron_id]
            except IndexError:
                raise ValueError(f"Neuron index {neuron_id} not found in sensor field data")
    else:
        # Choose the first neuron id if none is provided
        if "neuron_ids" in sensor.field_data and len(sensor.field_data["neuron_ids"]) > 0:
            neuron_id = sensor.field_data["neuron_ids"][0]
        else:
            raise ValueError("No neuron ID found in sensor field data")

    # Convert point_indices to numpy array if it's a single index
    if isinstance(point_indices, (int, np.integer)):
        point_indices = np.array([point_indices])
    else:
        point_indices = np.asarray(point_indices)

    n_points = len(point_indices)

    # Pre-compute all field keys to avoid repeated string formatting
    field_keys = [format_field_key('B', neuron_id, t) for t in time_points]

    # Optimize for common case of single point
    if n_points == 1:
        point_idx = point_indices[0]
        b_field_ts = np.zeros((n_time_points, 3))
        
        # Use vectorized operations when possible
        for t_idx, key in enumerate(field_keys):
            b_field_ts[t_idx] = sensor.point_data[key][point_idx]
            
        return time_points, b_field_ts

    # Handle multiple points
    else:
        # PyVista's extract_points is efficient for getting data for specific points
        b_field_ts = np.zeros((n_time_points, n_points, 3))
        
        for t_idx, key in enumerate(field_keys):
            # Get the full array for this time point
            field_data = sensor.point_data[key]
            
            # Extract only the points we need
            b_field_ts[t_idx, :, :] = field_data[point_indices]
            
        return time_points, b_field_ts


def plot(*objects, backend='notebook', show=True, style=None, **kwargs):
    """Plots neurons and sensors.

    Can be called as either:
        IO.plot(neuron1, sensor1)     # Class method
        io(neuron1).plot(sensor1)     # Instance method
        io().plot(neuron1, sensor1)   # Instance method
        neuron1.plot()                # Plot single neuron
        sensor1.plot()                # Plot single sensor
    
    Args:
        *objects: Additional Neuron or Sensor objects to plot
                combined with objects provided at initialization
        backend: 'notebook' or 'window'. If backend is 'notebook', the plot 
                will be displayed in the notebook using Trame. If backend 
                is 'window', the plot will be displayed in a new window with 
                a dedicated VTK renderer.
        show: If True, the plot will be displayed. If False, the plot will not be displayed.
        style: (dict) style parameters to be applied to passed objects, meshes, or the 
                plot itself. 
        **kwargs: Additional keyword arguments to be passed to the plotter.
    """
    if backend == 'notebook':
        pl = pv.Plotter(notebook=True)
    elif backend == 'window':
        pl = pv.Plotter(notebook=False,
                        off_screen=False,
                        window_size=[1024, 768])
        pl.background_color = 'white'  
        # Enable custom interactions if needed
        pl.enable_trackball_style()  # Or other camera styles
        # pl.enable_eye_dome_lighting()  # Better depth perception
        # pl.enable_depth_peeling()  # For better transparency rendering
        
    else:
        raise ValueError(f"Unsupported backend: {backend}. Use 'notebook' or 'window'.")
    
    # TODO: Next step: make visualization of NV centers more informative, add axes labels
    # TODO: Then, define orientation of the NV center relative to the sensor 
    
    # Plot all objects
    for o in objects:
        if hasattr(o, 'mesh'):
            pl.add_mesh(o.mesh)
        elif isinstance(o, NV):
            # Add transparent tetrahedron
            pl.add_mesh(o.mesh['tetrahedron'], opacity=0.2, color='lightgray')
            
            # Add NV axes with thicker lines
            for axis_line in o.mesh['axes']:
                pl.add_mesh(axis_line, color='red', line_width=3)
            
            # Add coordinate axes at offset
            scale = 1.0
            offset = np.array([-scale, -scale, -scale]) + o.position
            labels = ['x', 'y', 'z']
            for i, (color, label) in enumerate(zip([(1,0,0), (0,1,0), (0,0,1)], labels)):
                direction = np.zeros(3)
                direction[i] = 1
                # Add axis line
                pl.add_mesh(pv.Line(offset, offset + direction * scale),
                           color=color, line_width=2)
                # Add text label at end of axis with point marker to ensure visibility
                label_pos = offset + direction * scale * 1.1  # Slightly beyond axis end
                pl.add_mesh(pv.Sphere(radius=0.05, center=label_pos), color=color)  # Add visible point
                pl.add_point_labels([label_pos], [label], text_color=color, font_size=14, 
                                  always_visible=True, shape_opacity=0.3)  # Make label always visible with semi-transparent background
        elif isinstance(o, (pv.PolyData, pv.MultiBlock)):
            if style is None:
                style = {}
            pl.add_mesh(o, **style)
        elif (
            isinstance(o, tuple)
            and len(o) == 2 
            and isinstance(o[0], (pv.PolyData, pv.MultiBlock)) 
            and isinstance(o[1], dict)
             ):
            # If a tuple, treat it as a mesh and style
            pl.add_mesh(o[0], **o[1])
        else:
            raise ValueError(f"Unsupported object type: {type(o)}")
    
    if show:
        pl.show()
    
    if backend == 'window':
        pl.close()
    
    return pl


def save(*objects):
    """Save neurons and their associated sensors to disk.
    
    Can be called as either:
        IO.save(neuron1, sensor1)     # Class method
        io(neuron1).save(sensor1)     # Instance method
        io().save(neuron1, sensor1)   # Instance method
    """
    io = IO().save(*objects)
    return io

def add_picker(plotter):
    """Add a picker to the plotter.
    
    Args:
        plotter: The plotter to add the picker to.
    """
    picker = vtkPointPicker()
    
    def callback(_widget, event_name):
        print(event_name)
        x, y = plotter.iren.GetEventPosition()
        renderer = plotter.iren.get_poked_renderer(x, y)
        picker.Pick(x, y, 0, renderer)
        point_idx = picker.GetPointId()
        
        if point_idx != -1:
            mesh = picker.GetDataSet()
            print(mesh.GetName(), event_name, point_idx)
            
    hw = vtkHoverWidget()
    hw.SetInteractor(plotter.iren.interactor)
    hw.SetTimerDuration(100)  # time in ms required to trigger a hover event
    hw.AddObserver(vtkCommand.TimerEvent, callback)  # start of hover
    hw.AddObserver(vtkCommand.EndInteractionEvent, callback)  # hover ended (mouse moved)
    hw.EnabledOn()
    
    return plotter