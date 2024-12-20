import numpy as np
import pyvista as pv

import os

from currio import __modelpath__


class Neuron(object):
    def __init__(self, model_name=None, hocfile='mosinit.hoc'):
        from neuron import h
        self.h = h
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
        A list of dictionaries, each containing the 3D coordinates of the neuron model per section.
        The keys of the dictionary are:
            - `id`: the name of the section
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
            
            For each section in h.allsec():
            - `sec_name`: a dictionary with keys:
                - `v`: a list of voltage traces `_ref_v` for each segment in the section, i.e.
                    `v[i]` is the voltage trace for the `i`-th segment in the section of length `len(t)`.
                - `var_i`: a list of tracked variable passed to the `simulate` function as an argument
                    `record` as `.simulate(record=['var_1', 'var_2', ...])` with the same structure as `v`.
                - `var_i`: a list of tracked variable passed to the `record` function as `.record(track=['var_1', 'var_2', ...])`
                    with the same structure as `v`.
                - `var_i`: a list of tracked variable passed to the `simulate` function as an argument
                    `record` as `.simulate(record=['var_1', 'var_2', ...])` with the same structure as `v`.
                - `sec`: a reference to the section object in NEURON.
        """
        
        self.mesh: pv.MultiBlock = None
        """PyVista mesh of the neuron model. Updated by `.create_3d_mesh()` method. 
        Used to plot the 3D model of the neuron, to compute arc lengths along sections and 
        to store values for visualization."""
        
        self.mesh: pv.MultiBlock = None
        """PyVista mesh of the neuron model. Updated by `.create_3d_mesh()` method. 
        Used to plot the 3D model of the neuron, to compute arc lengths along sections and 
        to store values for visualization."""
        
    def load_model(self, model_name):
        os.chdir(self.model_path)
        self.h.load_file(self.hocfile)
        return self
        return self
        
    def simulate(self, proc_name, force=False, record=None):
    def simulate(self, proc_name, force=False):
    def simulate(self, proc_name, force=False, record=None):
        """Run a simulation procedure defined in the model .hoc file."""
        
        # Access and run the procedure
        if not hasattr(self.h, proc_name):
            raise ValueError(f"Procedure '{proc_name}' not found in the model.")
        
        for r in self.records:
            if r["proc_name"] == proc_name and not force:
                raise ValueError("Simulation already run. Use `force=True` to run again.")
            
        self.create_record(proc_name=proc_name, record=record)
        self.create_record(proc_name=proc_name)
        self.create_record(proc_name=proc_name, record=record)
        getattr(self.h, proc_name)()
        self.convert_record()
        return self
        return self
        
    def create_record(self, proc_name, record=None):
    def create_record(self, proc_name):
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
            voltages = np.array([v.as_numpy() for v in sec_dict["v"]])
            record[key] = {"v": voltages, "sec": sec}
        
        self.record = record
        self.records[-1] = record

    def load_3d_model(self):
        data = {}
        for sec in self.h.allsec():
            xs = [sec.x3d(i) for i in range(sec.n3d())]
            ys = [sec.y3d(i) for i in range(sec.n3d())]
            zs = [sec.z3d(i) for i in range(sec.n3d())]
            ds = [sec.diam3d(i) for i in range(sec.n3d())]
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
        
        elif isinstance(sec, self.h.Section):
            meshes = {sec.hname(): self.get_section_mesh(sec.hname())}
        
        elif isinstance(sec, list):
            if all([isinstance(s, str) for s in sec]):
                meshes = {s: self.get_section_mesh(s) for s in sec}
            elif all([isinstance(s, self.h.Section) for s in sec]):
                meshes = {sec.hname(): self.get_section_mesh(s.hname()) for s in sec}
            else:
                raise ValueError("Invalid type for `sec`. It is a list, but the elements are not strings or NEURON sections.")
            
        meshes = pv.MultiBlock(meshes)
        return meshes

    def create_3d_mesh(self):
        if self.mesh is None:
            self.mesh = self.get_3d_mesh()
        return self
    
    def get_section_mesh(self, sec_name):
        if self.data_3d is None:
            self.load_3d_model()
        
        sec_data = self.data_3d.get(sec_name, None)
        if sec_data is None:
            raise ValueError(f"Section '{sec_name}' not found in the 3D model.")
        
        points = sec_data["x"], sec_data["y"], sec_data["z"]
        points = np.array(points).T  # shape: (n_points, 3)
        
        diameters = np.array(sec_data["d"])
        
        # Implement one section - one line policy
        if len(points) > 2:
            spline = pv.Spline(points, len(points))
        else:
            spline = pv.Line(points[0], points[1])
            
        spline["diameter"] = diameters
        spline = spline.interpolate(spline, sharpness=10.0)
        mesh = spline.tube(radius=0.5, scalars="diameter", capping=True, absolute=True)
        return mesh