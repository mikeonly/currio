import pyvista as pv
from currio.neuron import Neuron
from currio.sensor import Sensor

from currio import __resultpath__

import datetime
import json
import numpy as np


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

    def plot(self_or_cls_or_obj, *objects, **kwargs):
        """Plots neurons and sensors.
        
        Can be called as either:
            IO.plot(neuron1, sensor1)     # Class method
            io(neuron1).plot(sensor1)     # Instance method
            io().plot(neuron1, sensor1)   # Instance method
            neuron1.plot()                # Plot single neuron
            sensor1.plot()                # Plot single sensor
        
        Args:
            *objects: Additional Neuron or Sensor objects to plot
                     Combined with objects provided at initialization
        """
        pl = pv.Plotter()
        
        # Determine what kind of call this is
        if isinstance(self_or_cls_or_obj, type):
            # Class method call - plot provided objects
            plot_objects = objects
        elif isinstance(self_or_cls_or_obj, IO):
            # Instance method call - combine with existing objects
            plot_objects = self_or_cls_or_obj.objects + list(objects)
        elif isinstance(self_or_cls_or_obj, (Neuron, Sensor)):
            # Single object call - combine with additional objects
            plot_objects = [self_or_cls_or_obj] + list(objects)
        elif isinstance(self_or_cls_or_obj, IO):
            pass
        else:
            raise TypeError(f"Cannot plot object of type {type(self_or_cls_or_obj)}")
        
        # Plot all objects
        for o in plot_objects:
            if isinstance(o, Neuron):
                pl.add_mesh(o.create_3d_mesh().mesh)
            elif isinstance(o, Sensor):
                pl.add_mesh(o)
        
        # Store plotter reference if IO instance call
        if isinstance(self_or_cls_or_obj, IO):
            self_or_cls_or_obj.pl = pl
        
        pl.show()
        return self_or_cls_or_obj if isinstance(self_or_cls_or_obj, IO) else None
    
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

