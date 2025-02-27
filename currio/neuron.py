from typing import Union
import numpy as np
import pyvista as pv

import os

from scipy.interpolate import interp1d
from scipy.sparse import csr_matrix, csc_matrix

from currio import __modelpath__

import currio
from currio.compiled import get_b_njit
from currio.utils import interp_along_axis
from currio.sensor import Sensor, RegularGridSensor


class Neuron(object):
    """A class representing a neuron model from ModelDB.
    
    Handles loading, simulating, and analyzing NEURON models. Provides methods for
    3D visualization and magnetic field computation.

    Args:
        model_name (str or int, optional): ModelDB ID or folder name. Defaults to None.
        hocfile (str, optional): Main HOC file to load. Defaults to 'mosinit.hoc'.

    Attributes:
        h: NEURON simulator interface
        model_path (Path): Path to model files
        data_3d (dict): 3D model data per section
        records (list): List of simulation records
        record (dict): Current active record
    """

    def __init__(self, model_name=None, hocfile='mosinit.hoc'):
        from neuron import h, nrn, gui
        self.h = h
        self.nrn = nrn
        self.gui = None
        """NEURON GUI object. If not None, the GUI is initialized."""
        self.hocfile = hocfile
        
        # Look for the model in the modelpath
        if model_name is not None:
            if isinstance(model_name, int):
                # model_name can be an int specifying the model number in the ModelDB, then
                model_name = str(model_name)
                
            self.model_path = __modelpath__ / model_name
        else:
            # Assume the model is in the current working directory
            self.model_path = os.getcwd()
        
        self.load_model(model_name)
        
        # Extract the model ID from the model path
        self.id = model_name.split("/")[-1]
        
        self.data_3d: dict = None
        """3D model of the neuron. Updated by `.load_3d_model()` method.
        
        A dictionary with keys being names of sections. Values are dictionaries
        each containing the 3D coordinates of the neuron model per section. The
        keys of the dictionary are:
            - `pts`: the 3D coordinates of the neuron model per section
            - `d`: the diameters of segments
        """
        
        self.records: list = []
        self._active_record_idx = -1
        self.record: dict = ...
        """Record dictionary of the simulation. Updated by `.create_record()`, 
        `.calculate_currents()` and `.propagate_B()` methods.
        
        .records list of dictionaries, each containing the voltage traces of the neuron model per section and
        a reference to the section object in NEURON. The keys of the dictionary are:
        
            - `proc_name`:  the name of the procedure used to run the simulation.
            - `notes`: a string with notes about the simulation.
            - `sensors`: a list of sensors (object references) to which 
                           the magnetic field from the record was propagated.
            - `t`: the time vector 
            
            A key `sec_name` for each section in h.allsec():
            - `sec_name`: a dictionary with keys:
                - `v`: a list of voltage traces `_ref_v` for each segment in the section, i.e.
                    `v[i]` is the voltage trace for the `i`-th segment in the section of length `len(t)`.
                - `var_i` (e.g. `currents`): a list of tracked variables passed to the `simulate` function 
                    as an argument `track_vars` in `.simulate(track_vars=['var_1', 'var_2', ...])` with the 
                    same structure as `v`, or it can also be a variable computed per segment in the 
                    section by e.g. `.calculate_currents()` and can have a different structure.
                - `sec`: a reference to the section object in NEURON.
        """
        
        self.mesh: pv.MultiBlock = None
        """PyVista mesh of the neuron model. Updated by `.create_3d_mesh()` method. 
        Used to plot the 3D model of the neuron, to compute arc lengths along sections and 
        to store values for visualization."""
        
    @property
    def record(self):
        """Active record from records list."""
        if len(self.records) == 0:
            raise ValueError("No records found. Run a simulation with `.simulate()` "
                           "first to create a record.")
        return self.records[self._active_record_idx]

    @record.setter
    def record(self, value):
        self._record = value
    
    def set_active_record(self, record):
        """Set the active record to the given record.
        
        Args:
            record (int, string):  a record to set as active. If int, it is interpreted as the index of the record.
                                  If string, it is interpreted as the name of the record.
        """
        if isinstance(record, int):
            self._active_record_idx = record
        elif isinstance(record, str):
            self._active_record_idx = [r["proc_name"] for r in self.records].index(record)
        else:
            raise ValueError("Invalid type for `record`. It should be an int or a string.")
        return self
    
    
    def get_gui(self):
        if self.gui is None:
            from neuron import gui
            self.gui = gui
        return self.gui
        
    def load_model(self, model_name=None):
        """Load a NEURON model from the models directory.

        Args:
            model_name (str, optional): Model ID or folder name. Defaults to None.

        Raises:
            FileNotFoundError: If model files not found
            RuntimeError: If model fails to load
        """
        # Change to model directory, self.model_path is a Path object, so convert it to str
        success = self.h.chdir(str(self.model_path))
        if success != 0:  # NEURON returns 0 on success of unix operations such as chdir
                            # see https://www.neuron.yale.edu/neuron/static/new_doc/programming/system.html?highlight=load_dll#chdir
            raise RuntimeError(f"Failed to change to model directory {self.model_path}")
        
        # Check if file exists
        if not os.path.exists(self.hocfile):
            raise FileNotFoundError(f"Could not find {self.hocfile} in {self.model_path}")
        
        # Try loading, use 1 as a first argument to force `load_file` even if such a file 
        # has already been loaded.
        success = self.h.load_file(1, self.hocfile)
        if success != 1:  # NEURON returns 1 on success
            raise RuntimeError(f"Failed to load {self.hocfile}")
        
        return self
        
    def simulate(self, proc_name, force=False, track_vars=None):
        """Run a simulation procedure defined in the model .hoc file."""
        
        # Access and run the procedure
        if not hasattr(self.h, proc_name):
            raise ValueError(f"Procedure '{proc_name}' not found in the model.")
        
        for r in self.records:
            if r["proc_name"] == proc_name and not force:
                raise ValueError("Simulation already run. Use `force=True` to run again.")
            
        self.create_record(proc_name=proc_name, track_vars=track_vars)
        getattr(self.h, proc_name)()
        self.convert_record()
        return self
        
    def create_record(self, proc_name, track_vars=None):
        """Creates a record of the simulation. Record is a dictionary with keys 
        as section names and values as dictionaries containing the voltage traces and 
        references to section objects in NEURON.
        
        The record dictionary contains:
            - `proc_name`:  the name of the procedure used to run the simulation.
            - `t`: the time vector 
            - `sections`: a list of section names
            
            A key `sec_name` for each section in h.allsec():
            - `sec_name`: a dictionary with keys:
                - `v`: a list of voltage traces `_ref_v` for each segment in the section, i.e.
                    `v[i]` is the voltage trace for the `i`-th segment in the section of length `len(t)`.
                - `var_i` (e.g. `currents`): a list of tracked variables passed to the `simulate` function 
                    as an argument `track_vars` in `.simulate(track_vars=['var_1', 'var_2', ...])` with the 
                    same structure as `v`, or it can also be a variable computed per segment in the 
                    section by e.g. `.calculate_currents()` and can have a different structure.
                    See variable spec format below.
                - `sec`: a reference to the section object in NEURON.

        Args:
            proc_name (string): The name of the procedure to record.
            track_vars (list[str] or None): List of variable specifications to track. If None, defaults to ["*.v"],
                                                i.e. always tracks voltages across all sections.
            
        Variable spec format:
            {section_pattern}.{variable}
            
            - section_pattern: Pattern matching section names
                * = all sections
                soma = just soma section
                dend* = all sections starting with "dend"
                
            - variable: Name of variable to record
                v = membrane voltage
                i_name = current for mechanism 'name'
                name.var = variable 'var' from point process 'name'
                
        Examples:
            - "*.v" - Record voltage from all sections
            - "dend*.i_hh" - Record HH current from dendrites
            - "*.syn.i" - Record synaptic current from sections with syn point process
        
        Returns:
            self: Returns the Neuron object for chaining.
        """
        record = {
            "proc_name": proc_name,
            "t": self.h.Vector().record(self.h._ref_t),
            "sections": []  # List of section names
        }
        """Record dictionary of the simulation."""

        if track_vars is None:
            track_vars = ["*.v"]  # Default to recording all voltages

        if not isinstance(track_vars, list):
            raise ValueError("`track_vars` must be a list of strings")

        # Initialize record dictionary with empty sections
        for sec in self.h.allsec():
            record[sec.name()] = {}
            record["sections"].append(sec.name())

        # Process each variable specification in `track_vars`
        for var_spec in track_vars:
            try:
                section_pat, *var_parts = var_spec.split(".")
                variable = ".".join(var_parts)  # Rejoin any remaining parts for point process vars
                
            except ValueError:
                raise ValueError(f"Invalid variable specification: {var_spec}. " +
                               "Must be in format: section_pattern.variable")

            # Match sections according to pattern
            for sec in self.h.allsec():
                sec_name = sec.name()
                if section_pat == "*" or sec_name.startswith(section_pat.replace("*", "")):
                    # Add section name to list if not already there
                    if sec_name not in record["sections"]:
                        record["sections"].append(sec_name)
                        record[sec_name] = {}

                    # Initialize list for this variable if not present
                    if variable not in record[sec_name]:
                        record[sec_name][variable] = []
                    
                    # Record variable for each segment
                    for seg in sec.allseg():
                        try:
                            vec = self.h.Vector().record(getattr(seg, f"_ref_{variable}"))
                            record[sec_name][variable].append(vec)
                        except AttributeError:
                            record[sec_name][variable].append(None)

        # Rewrite the last recording 
        self.record = record
        # Add recording to the records list
        self.records.append(record)
        return self
        
    def convert_record(self):
        """Converts the record dictionary from HocObjects to np.arrays."""
        record = self.record
        for key, sec_dict in record.items():
            if key == "t":
                record["t"] = sec_dict.as_numpy()
                continue
            elif key == "proc_name":
                continue
            
            for key, v in sec_dict.items():
                if key == "sec":
                    continue
                else:
                    # Each x is a HocObject of recorded values with length len(t), convert to np.array
                    sec_dict[key] = np.array([x.as_numpy() for x in sec_dict[key]])
        
        self.record = record
        self.records[-1] = record
        return self
        
    def calculate_currents(self):
        """Calculate the currents in the neuron model.
        
        Propagates the self.record dictionary with new keys:
            - `currents`: a list of currents for each segment in 3D model in the
              section of length `len(t)`.
        """
        if self.record is None:
            raise ValueError(
                """No simulation record found. Run a simulation first by specifying
                    the process name in `.simulate('proc_name')`.""")
        else:
            record = self.record
            
        if self.mesh is None:
            mesh = self.create_3d_mesh().mesh
        else:
            mesh = self.mesh
        
        if self.data_3d is None:
            data_3d = self.load_3d_model().data_3d
        else:
            data_3d = self.data_3d
        
        # Iterate through sections using the sections list
        for section in self.record["sections"]:
            sec = self.h.__getattr__(section)
            sec_dict = self.record[section]
            
            voltages = sec_dict["v"]
            diameters = data_3d[section]["d"]
            polydata = mesh[section]
            
            # `v_dists` are distances along the section where voltages are calculated,
            # whereas `seg_points` are points from the 3D model of the neuron.
            # They are different and voltages need to be interpolated to the 3D model points.
            v_dists = np.array([seg.x for seg in sec.allseg()]) * sec.L
            seg_lengths = np.array(polydata.field_data["arc_length"])
            seg_dists = np.cumsum(seg_lengths)
            
            interp_v = interp_along_axis(
                voltages, 
                v_dists,
                seg_dists,
                axis=0)

            axial_resistance = sec.Ra  # axial resistance in Ohm*cm
            axial_resistance *= 1e4    # convert to Ohm*um
            
            # Cross-sectional area of the 3D segments
            middle_diameters = (diameters[:-1] + diameters[1:])  / 2  # find the middle diameters
            
            
            area = middle_diameters ** 2 * np.pi / 4 # cross-sectional area in um^2
            axial_resistance_per_units_length = axial_resistance / area
            
            currents = np.diff(interp_v, axis=0) / (seg_lengths[1:] * axial_resistance_per_units_length)[:, None]
            sec_dict["interp_v"] = interp_v
            sec_dict["currents"] = currents
        return self
    
    def propagate_B(self, sensor, array_name=None):
        """Propagate the magnetic field from the neuron model to the sensor points."""
        if self.record is None:
            raise RuntimeError(
                """No simulation record found. Run a simulation first by specifying
                    the process name in `.simulate('proc_name')`.""")
        else:
            record = self.record
            
        if array_name is None:
            array_name = "B" + "_" + self.id
        
        pts = sensor.points
        B = self.get_B(pts)
            
        # Split vectors into components
        for t_idx, t in enumerate(record["t"]):
            datum = B[:, :, t_idx]
            
            # Add vector field as a point data with a time index
            sensor.point_data[f'B_{self.id}_{t:.4f}'] = datum.T
            
        # Store time points as field data
        sensor.field_data['t'] = record["t"]
        sensor.field_data['t_units'] = ['ms']

        # Track which sensors have fields propagated to them
        if "sensors" not in record:
            record["sensors"] = []
        record["sensors"].append({
            "sensor": sensor,
            "array_name": array_name
        })

        return self
    
    def load_3d_model(self):
        data = {}
        for sec in self.h.allsec():
            xs = np.array([sec.x3d(i) for i in range(sec.n3d())])
            ys = np.array([sec.y3d(i) for i in range(sec.n3d())])
            zs = np.array([sec.z3d(i) for i in range(sec.n3d())])
            pts = np.array([xs, ys, zs]).T
            ds = np.array([sec.diam3d(i) for i in range(sec.n3d())])
            data[sec.hname()] = {
                "pts": pts,
                "d": ds  # diameters
            }
        self.data_3d = data
        return self
    
    def get_3d_mesh(self, sec=None) -> pv.MultiBlock:
        """Outputs a pyvista mesh of the neuron. If `sec` is given, only that section(s) is (are) returned.
        Sections can be either a string or a list of strings, or it can be a list of section objects from h 
        NEURON environment."""
        if self.data_3d is None:
            self.load_3d_model()
            
        if sec is None:
            meshes = {sec: self.get_section_mesh(sec) for sec in self.data_3d.keys()}
        
        elif isinstance(sec, str):
            meshes = {sec: self.get_section_mesh(sec)}
        
        elif isinstance(sec, self.nrn.Section):
            meshes = {sec.hname(): self.get_section_mesh(sec.hname())}
        
        elif isinstance(sec, list):
            if all([isinstance(s, str) for s in sec]):
                meshes = {s: self.get_section_mesh(s) for s in sec}
            elif all([isinstance(s, self.nrn.Section) for s in sec]):
                meshes = {sec.hname(): self.get_section_mesh(s.hname()) for s in sec}
            else:
                raise ValueError("Invalid type for `sec`. It is a list, but the elements are not strings or NEURON sections.")
            
        meshes = pv.MultiBlock(meshes)
        return meshes

    def create_3d_mesh(self):
        if self.mesh is None:
            self.mesh = self.get_3d_mesh()
        return self
    
    def get_section_mesh(self, sec):
        if self.data_3d is None:
            self.load_3d_model()
        
        if isinstance(sec, self.nrn.Section):
            sec_data = self.data_3d.get(sec.hname(), None)
        elif isinstance(sec, str):
            sec_data = self.data_3d.get(sec, None)
        else:
            raise ValueError("""
                Invalid type for `sec`. It should be either a string or a NEURON section,
                but got type {} for `sec` {}.""".format(type(sec), sec))
        
        if sec_data is None:
            raise ValueError(f"Section '{sec}' not found in the 3D model.")
        
        points = sec_data["pts"]
        diameters = sec_data["d"]
        
        # Implement one section - one line policy
        if len(points) > 2:
            spline = pv.Spline(points, len(points))
        else:
            spline = pv.Line(points[0], points[1])
            
        spline = spline.compute_arc_length()
        lengths = spline.point_data["arc_length"]
            
        spline["diameter"] = diameters
        spline = spline.interpolate(spline, sharpness=10.0)
        mesh = spline.tube(radius=0.5, scalars="diameter", capping=True, absolute=True)
        mesh.field_data["arc_length"] = lengths
        return mesh
    
    def get_mechanisms(self, mech):
        mechs = []
        for sec in self.h.allsec():
            for seg in sec.allseg():
                for mech in seg:
                    # Look for the mechanism in the segment
                    if mech in mech.name():
                        mechs.append({
                            "sec": sec.hname(),
                            "seg": seg.x,
                            "mech": mech.name()
                        })
        return mechs
    
    def find_synapses(self):
        synapses = []
        for sec in self.h.allsec():
            for seg in sec:
                for mech in seg:
                    # Look for synapse mechanisms
                    if 'syn' in mech.name():
                        synapses.append({
                            'section': sec.name(),
                            'position': seg.x,
                            'mechanism': mech.name()
                        })
        return synapses

    def get_B(self, pts: Union[np.ndarray, Sensor]) -> np.ndarray:
        """Calculate and return the magnetic field at points `pts` or `sensor.points` 
        in the space.
        
        Uses Eq. (2) from Karadas et al.[^2] to compute the magnetic field from axial currents:

        ..math::
        
            \mathbf{B}(\mathbf{r},t) = \frac{\mu_0}{4\pi} \sum_i \frac{\mathbf{I}^{\mathrm{axial}}_i(t) \times \hat{\boldsymbol{\rho}}_n}{\rho_n} \left[\frac{h_n}{\sqrt{h_n^2 + \rho_n^2}} - \frac{l_n}{\sqrt{l_n^2 + \rho_n^2}}\right]

        where:

        * :math:`\mathbf{r}` is the observation point (sensor location)
        * :math:`\mathbf{I}^{\mathrm{axial}}_i(t)` is the axial current at time t
        * :math:`\rho_n` is the perpendicular distance to the segment
        * :math:`\hat{\boldsymbol{\rho}}_n` is the unit vector perpendicular to the segment
        * :math:`h_n, l_n` are the distances to the segment endpoints along its axis

        (sum over all 3D point segments in the neuron geometry indexed by i)

        Reference:
            Karadas et al., "Feasibility and resolution limits of opto-magnetic imaging 
            of neural network activity in brain slices using color centers in diamond," 
            Scientific Reports, 2018.

        Args:
            pts: Array of points or Sensor object where to compute the field 
                (if Sensor, then pts.points is used)

        Returns:
            np.ndarray: Magnetic field vectors at specified points

        Raises:
            ValueError: If no simulation record exists
        """
        if isinstance(pts, Sensor):
            pts = pts.points
        
        # Check if `currents` are calculated at any key in the record
        if any(["currents" not in self.record[section] for section in self.record["sections"]]):
            print(Warning("Didn't find currents. Calculating currents first."))
            self.calculate_currents()
            
        if len(self.records) == 0:
            Warning("Didn't find any recorded simulations. Running a default procedure now.")
            self.simulate("default")
            self.calculate_currents()
        
        nt = len(self.record["t"])
        B = np.zeros((3, len(pts), nt))
        
        for section in self.record["sections"]:
            sec_dict = self.record[section]
            
            sec_pts = self.data_3d[section]["pts"]
            currents = sec_dict["currents"]
            
            B[:, :, :] += get_b_njit(sec_pts, pts, currents)
        
        return B
