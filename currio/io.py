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
                
            neuron_str = [f"Neuron `{n.id}` with {record_str}"]
            
            # Add detailed record info if any exist
            if hasattr(n, 'records') and n.records:
                for r in n.records:
                    proc_name = r.get('proc_name', 'unknown')
                    t = r.get('t', [])
                    
                    # Get tracked variables by looking for array/list values
                    tracked_vars = []
                    for key, value in r.items():
                        # Skip special keys
                        if key in ['proc_name', 'notes', 'sensors', 't']:
                            continue
                        # If it's a section dictionary
                        if isinstance(value, dict):
                            # Add variables that have array/list values
                            tracked_vars.extend(
                                var_name for var_name, var_value in value.items()
                                if isinstance(var_value, (list, np.ndarray))
                                and var_name != 'sec'  # Skip section reference
                            )
                    
                    vars_str = ", ".join(sorted(set(tracked_vars)))  # Remove duplicates
                    
                    if len(t) > 0:
                        time_range = f"t=[{min(t):.1f}, {max(t):.1f}] ms"
                        neuron_str.append(
                            f"    Record `{proc_name}` with {len(t)} time points in {time_range}, "
                            f"recorded values: {vars_str}"
                        )
            
            neuron_info.append("\n".join(neuron_str))
            
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

    def plot(self_or_cls, *objects, **kwargs):
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
        if isinstance(self_or_cls, type):
            # Class method call - plot provided objects
            plot_objects = objects
        elif isinstance(self_or_cls, IO):
            # Instance method call - combine with existing objects
            plot_objects = self_or_cls.objects + list(objects)
        elif isinstance(self_or_cls, (Neuron, Sensor)):
            # Single object call - combine with additional objects
            plot_objects = [self_or_cls] + list(objects)
        else:
            raise TypeError(f"Cannot plot object of type {type(self_or_cls)}")
        
        # Plot all objects
        for o in plot_objects:
            if isinstance(o, Neuron):
                pl.add_mesh(o.create_3d_mesh().mesh)
            elif isinstance(o, Sensor):
                pl.add_mesh(o)
        
        # Store plotter reference if IO instance call
        if isinstance(self_or_cls, IO):
            self_or_cls.pl = pl
        
        pl.show()
        return self_or_cls if isinstance(self_or_cls, IO) else None
    
    def save(self):
        self.__class__.save(*self.neurons, *self.sensors)
    
    @classmethod
    def save(*objects):
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
        
        # Implement the easy case: you pass only one sensor and a neuron with a record,
        # so it just dumps records as a json, and sensor as a vtk.
        neurons = []
        sensors = []
        
        for object in objects:
            
            if isinstance(object, Neuron):
                records = []
                for record in object.records:
                    records.append(make_serializable(record))
                    
                neurons += [object]

                with open(resultspath / f"{object.id}.json", "w") as f:
                    json.dump(records, f, indent=2)
                    print(f"Saved records for Neuron {object.id} to {resultspath / f'{object.id}.json'}")
            
            elif isinstance(object, Sensor):
                object.save(resultspath / f"{object.id}.vtk")
                print(f"Saved data for Sensor {object.id} to {resultspath / f'{object.id}.vtk'}")
                
                sensors += [object]
                
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
        return IO(*objects)
    
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
        
        Args:
            save_id: Integer (e.g. 1) or string ID (e.g. "001"). Will find matching
                    description file like "001-*.txt"
        
        Returns:
            io: New io instance with loaded objects
        """
        # Convert save_id to proper format
        if isinstance(save_id, int):
            save_id = f"{save_id:03d}"
            
        results = __resultpath__
        
        # Find description file
        desc_files = list(results.glob(f"{save_id}-*.txt"))
        if not desc_files:
            raise FileNotFoundError(f"No description file found for save ID {save_id}")
        if len(desc_files) > 1:
            raise ValueError(f"Multiple description files found for save ID {save_id}")
            
        desc_file = desc_files[0]
        
        # Parse description file
        with open(desc_file) as f:
            lines = f.readlines()
            
        # Extract neuron and sensor IDs
        neuron_ids = []
        sensor_ids = []
        
        for line in lines:
            if line.startswith("Neurons:"):
                neuron_ids = [n.strip() for n in line.split(":")[1].split(",")]
            elif line.startswith("Sensors:"):
                sensor_ids = [s.strip() for s in line.split(":")[1].split(",")]
                
        # Load neurons and their records
        neurons = []
        for nid in neuron_ids:
            if not nid:
                continue
            record_file = results / f"{nid}.json"
            if not record_file.exists():
                raise FileNotFoundError(f"No records for model {nid}")
                
            with open(record_file) as f:
                records = json.load(f)
                
            neuron = Neuron(nid)
            neuron.records = records
            neurons.append(neuron)
            
        # Load sensors
        sensors = []
        for sid in sensor_ids:
            if not sid:
                continue
            sensor_file = results / f"{sid}.vtk"
            if not sensor_file.exists():
                raise FileNotFoundError(f"Sensor file not found: {sensor_file}")
                
            sensor = pv.read(sensor_file)
            # Convert to our Sensor class while preserving data
            sensor_obj = Sensor(sensor.points)
            sensor_obj.point_data.update(sensor.point_data)
            sensor_obj.field_data.update(sensor.field_data)
            sensor_obj.id = sid
            sensors.append(sensor_obj)
            
        return cls(*neurons, *sensors)
    
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

