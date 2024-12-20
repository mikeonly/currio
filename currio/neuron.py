import numpy as np
import pyvista as pv

import os

from scipy.interpolate import interp1d

from currio import __modelpath__
from currio.utils import interp_along_axis


class Neuron(object):
    def __init__(self, model_name=None, hocfile='mosinit.hoc'):
        from neuron import h, nrn
        self.h = h
        self.nrn = nrn
        self.hocfile = hocfile
        
        # Look for the model in the modelpath
        if model_name is not None:
            if isinstance(model_name, int):
                # model_name can be an int specifying the model number in the ModelDB, then
                model_name = str(model_name)
                
            self.model_path = __modelpath__ / model_name
        elif model_name is None:
            # Assume the model is in the current working directory
            self.model_path = os.getcwd()
        
        self.load_model(model_name)
        
        self.data_3d: dict = None
        """3D model of the neuron. Updated by `.load_3d_model()` method.
        
        A dictionary with keys being names of sections. Values are dictionaries
        each containing the 3D coordinates of the neuron model per section. The
        keys of the dictionary are:
            - `x`: the x-coordinates of segments
            - `y`: the y-coordinates of segments
            - `z`: the z-coordinates of segments
            - `d`: the diameters of segments
        """
        
        self.records: list = []
        self.record: dict = None
        """Record dictionary of the simulation. Updated by `.create_record()` method.
        
        A list of dictionaries, each containing the voltage traces of the neuron model per section and
        a reference to the section object in NEURON. The keys of the dictionary are:
        
            - `proc_name`: the name of the procedure used to run the simulation.
            - `t`: the time vector 
            
            A key `sec_name` for each section in h.allsec():
            - `sec_name`: a dictionary with keys:
                - `v`: a list of voltage traces `_ref_v` for each segment in the section, i.e.
                    `v[i]` is the voltage trace for the `i`-th segment in the section of length `len(t)`.
                - `var_i`: a list of tracked variable passed to the `simulate` function as an argument
                    `record` as `.simulate(record=['var_1', 'var_2', ...])` with the same structure as `v`.
                - `sec`: a reference to the section object in NEURON.
        """
        
        self.mesh: pv.MultiBlock = None
        """PyVista mesh of the neuron model. Updated by `.create_3d_mesh()` method. 
        Used to plot the 3D model of the neuron, to compute arc lengths along sections and 
        to store values for visualization."""
        
    def load_model(self, model_name):
        os.chdir(self.model_path)
        self.h.load_file(self.hocfile)
        return self
        
    def simulate(self, proc_name, force=False, record=None):
        """Run a simulation procedure defined in the model .hoc file."""
        
        # Access and run the procedure
        if not hasattr(self.h, proc_name):
            raise ValueError(f"Procedure '{proc_name}' not found in the model.")
        
        for r in self.records:
            if r["proc_name"] == proc_name and not force:
                raise ValueError("Simulation already run. Use `force=True` to run again.")
            
        self.create_record(proc_name=proc_name, record=record)
        getattr(self.h, proc_name)()
        self.convert_record()
        return self
        
    def create_record(self, proc_name, record=None):
        """Creates a record of the simulation. Record is a dictionary with keys 
        as section names and values as dictionaries containing the voltage traces and 
        references to section objects in NEURON.
        """
        record = {}
        """Record dictionary of the simulation."""
        record["proc_name"] = proc_name
        record["t"] = self.h.Vector().record(self.h._ref_t)
        for sec in self.h.allsec():
            record[sec.name()] = {"v": []}
            for seg in sec.allseg():
                v = self.h.Vector().record(seg._ref_v)
                record[sec.name()]["v"].append(v)
                record[sec.name()]["sec"] = sec
        
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
            
            sec = sec_dict["sec"]
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
            - `I`: a list of currents for each segment in the section of length `len(t)`.
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
        
        for key, sec_dict in record.items():
            if key == "t" or key == "proc_name":
                continue
            
            sec = sec_dict["sec"]
            voltages = sec_dict["v"]
            diameters = data_3d[key]["d"]
            
            polydata = mesh[key]
            
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
            record[key]["interp_v"] = interp_v
            record[key]["currents"] = currents
        return self


    def load_3d_model(self):
        data = {}
        for sec in self.h.allsec():
            xs = np.array([sec.x3d(i) for i in range(sec.n3d())])
            ys = np.array([sec.y3d(i) for i in range(sec.n3d())])
            zs = np.array([sec.z3d(i) for i in range(sec.n3d())])
            ds = np.array([sec.diam3d(i) for i in range(sec.n3d())])
            data[sec.hname()] = {
                "x": xs,
                "y": ys,
                "z": zs,
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
        
        points = sec_data["x"], sec_data["y"], sec_data["z"]
        points = np.array(points).T  # shape: (n_points, 3)
        
        diameters = np.array(sec_data["d"])
        
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