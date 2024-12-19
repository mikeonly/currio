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
        
        self.data_3d = None
        """3D model of the neuron.
        
        A list of dictionaries, each containing the 3D coordinates of the neuron model per section.
        The keys of the dictionary are:
            - `id`: the name of the section
            - `x`: the x-coordinates of segments
            - `y`: the y-coordinates of segments
            - `z`: the z-coordinates of segments
            - `d`: the diameters of segments
        """
        
    def load_model(self, model_name):
        os.chdir(self.model_path)
        self.h.load_file(self.hocfile)
        
    def extract_vt(self):
        vt_dict = {}
        vt_dict["t"] = self.h.Vector().record(self.h._ref_t)
        for sec in self.h.allsec():
            vt_dict[sec.name()] = {"v": []}
            for seg in sec.allseg():
                v = self.h.Vector().record(seg._ref_v)
                vt_dict[sec.name()]["v"].append(v)
                vt_dict[sec.name()]["sec"] = sec
        self.h.superrun()
        return vt_dict

    def load_3d_model(self):
        data = []
        for sec in self.h.allsec():
            xs = [sec.x3d(i) for i in range(sec.n3d())]
            ys = [sec.y3d(i) for i in range(sec.n3d())]
            zs = [sec.z3d(i) for i in range(sec.n3d())]
            ds = [sec.diam3d(i) for i in range(sec.n3d())]
            data.append({
                "id": sec.hname(),
                "x": xs,
                "y": ys,
                "z": zs,
                "d": ds  # diameters
            })
        self.data_3d = data
        return data
    
    def get_3d_mesh(self, sec=None):
        """Outputs a pyvista mesh of the neuron. If `sec` is given, only that section(s) is (are) returned.
        Sections can be either a string or a list of strings, or it can be a list of section objects from h 
        NEURON environment."""
        if self.data_3d is None:
            self.load_3d_model()
            
        if sec is None:
            meshes = {sec["id"]: self.get_section_mesh(sec["id"]) for sec in self.data_3d}
        
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
            
        return pv.MultiBlock(meshes)
    
    def get_section_mesh(self, sec_name):
        if self.data_3d is None:
            self.load_3d_model()
        
        sec_data = [sec for sec in self.data_3d if sec["id"] == sec_name]
        if len(sec_data) == 0:
            raise ValueError(f"Section '{sec_name}' not found in the 3D model.")
        elif len(sec_data) > 1:
            raise ValueError(f"Multiple sections with the name '{sec_name}' found in the 3D model.")
        else:
            sec_data = sec_data[0]
        
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
        
        return spline.tube(radius=0.5, scalars="diameter", capping=True, absolute=True)

    # def convert_to_pyvista_mesh(self, neuron_data):
    #     points = []
    #     lines = []
    #     diameters = []
        
    #     for sec_data in neuron_data:
    #         n_points = len(sec_data["x"])
    #         for i in range(n_points):
    #             points.append([sec_data["x"][i], sec_data["y"][i], sec_data["z"][i]])
    #             diameters.append(sec_data["d"][i])
    #             # Add connectivity between lines
    #             if i < n_points - 1:
    #                 lines.append([2, len(points) - 1, len(points)])
        
    #     points = np.array(points)
    #     lines = np.array(lines)
    #     diameters = np.array(diameters)
        
    #     polydata = pv.PolyData()
    #     polydata.points = points
    #     polydata.lines = lines
    #     polydata["diameter"] = diameters
        
    #     return polydata.tube(radius=0.5, scalars="diameter", capping=True, absolute=True)
