import numpy as np
# from neuron import h
import pyvista as pv
from scipy.interpolate import interp1d


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