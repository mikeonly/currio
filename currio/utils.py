import numpy as np
# from neuron import h
import pyvista as pv
from scipy.interpolate import interp1d

import textwrap

def get_point_along_spline(spline: pv.PolyData, distance, rel=True):
    """Get a point along a spline at a given distance from the origin.
    
    Args:
        spline: PyVista spline or any mesh with `arc_length` field data
        distance: Distance from the origin along the spline
        rel: If True, the distance is relative to the length of the spline
    
    Return:
        point: Point in 3D space along the spline at the given distance
    """
    if rel:
        distance = distance * \
            spline.field_data["arc_length"][-1]  # multiply by the total length of the spline

    idx = np.argmin(np.abs(spline.field_data["arc_length"] - distance))
    return np.array(spline.points[idx])

def interp_along_axis(y, x, newx, axis):
    """Interpolate along a given axis of an array. Given an array y with shape (N, M), 
    array x with shape N and newx with shape L, this function interpolates y along the axis 0
    and outputs a newy array with shape (L, M). The interpolation is done using a linear interpolation.
    
    In general, if y is of shape (N, ..., K, ...), x should be of shape (K,) and newx of shape (L,) to give
    a newy of shape (N, ..., L, ...).

    This function assumes that the x-xoordinate increases monotonically
    """

    if y.shape[axis] != x.shape[0]:
        raise ValueError("y and x must have the same length along the axis to interpolate")
    
    newy_shape = list(y.shape)
    newy_shape[axis] = len(newx)
    newy = np.empty(newy_shape)

    newy = np.apply_along_axis(lambda y: interp1d(x, y, kind='linear', fill_value='extrapolate')(newx), axis, y)
    
    return newy

# This will be a useful function for future, to explore available functions for a NEURON object
def nrndir(obj):
    print(textwrap.fill(', '.join([x for x in dir(obj) if not x.startswith('_')])))