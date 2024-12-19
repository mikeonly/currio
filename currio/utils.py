import numpy as np
# from neuron import h
import pyvista as pv
from scipy.interpolate import interp1d

def load_model(model_name):
    h.load_file(f"{model_name}/mosinit.hoc")
    return h

def extract_vt():
    vt_dict = {}
    vt_dict["t"] = h.Vector().record(h._ref_t)
    for sec in h.allsec():
        vt_dict[sec.name()] = {"v": []}
        for seg in sec.allseg():
            v = h.Vector().record(seg._ref_v)
            vt_dict[sec.name()]["v"].append(v)
            vt_dict[sec.name()]["sec"] = sec
    h.superrun()
    return vt_dict

def explode_3d_vt_dict(vt_dict):
    res_dict = {}
    for key, sec_dict in vt_dict.items():
        if key == "t":
            res_dict["t"] = sec_dict.as_numpy()
            continue
        sec = sec_dict["sec"]
        diameters = np.array([sec.diam3d(i) for i in range(sec.n3d())])
        voltages = np.array([v.as_numpy() for v in sec_dict["v"]])
        x = np.array([seg.x for seg in sec.allseg()]) * sec.L
        arc3d = get_arc_lengths(sec, cumulative=True)
        pts3d = np.array([[sec.x3d(i), sec.y3d(i), sec.z3d(i)] for i in range(sec.n3d())])
        newvoltages = interp_along_axis(voltages, x, arc3d, axis=0)
        res_dict[key] = {"v": newvoltages, "pts3d": pts3d, "diam": diameters, "arc3d": arc3d, "sec": sec}
    return res_dict

def get_arc_lengths(sec, cumulative=False):
    lengths = np.empty((sec.n3d(), ))
    L = sec.L
    x, y, z = sec.x3d(0), sec.y3d(0), sec.z3d(0)
    r = np.array([x, y, z])
    lengths[0] = 0.
    for i in range(sec.n3d()-1):
        p = np.array([sec.x3d(i+1), sec.y3d(i+1), sec.z3d(i+1)])
        l = np.linalg.norm(p - r)
        r = p
        if cumulative:
            lengths[i+1] = lengths[i] + l
        else:
            lengths[i+1] = l
    if cumulative and lengths[-1] - L > 1e-6:
        lengths[-1] = L
    return lengths

def interp_along_axis(y, x, newx, axis):
    if y.shape[axis] != x.shape[0]:
        raise ValueError("y and x must have the same length along the axis to interpolate")
    newy_shape = list(y.shape)
    newy_shape[axis] = len(newx)
    newy = np.empty(newy_shape)
    newy = np.apply_along_axis(lambda y: interp1d(x, y, kind='linear', fill_value='extrapolate')(newx), axis, y)
    return newy

def extract_neuron_3d_model():
    data = []
    for sec in h.allsec():
        xs = [sec.x3d(i) for i in range(sec.n3d())]
        ys = [sec.y3d(i) for i in range(sec.n3d())]
        zs = [sec.z3d(i) for i in range(sec.n3d())]
        ds = [sec.diam3d(i) for i in range(sec.n3d())]
        data.append({
            "id": sec.hname(),
            "x": xs,
            "y": ys,
            "z": zs,
            "d": ds
        })
    return data

def convert_to_pyvista_mesh(neuron_data):
    points = []
    lines = []
    diameters = []
    for sec_data in neuron_data:
        n_points = len(sec_data["x"])
        for i in range(n_points):
            points.append([sec_data["x"][i], sec_data["y"][i], sec_data["z"][i]])
            diameters.append(sec_data["d"][i])
            if i < n_points - 1:
                lines.append([2, len(points) - 1, len(points)])
    points = np.array(points)
    lines = np.array(lines)
    diameters = np.array(diameters)
    
    polydata = pv.PolyData()
    polydata.points = points
    polydata.lines = lines
    polydata["diameter"] = diameters
    return polydata.tube(radius=0.5, scalars="diameter", capping=True, absolute=True)
