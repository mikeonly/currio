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

    # TODO: Use numpy.interp instead of the interp1d class in scipy
    newy = np.apply_along_axis(lambda y: interp1d(x, y, kind='linear', fill_value='extrapolate')(newx), axis, y)
    return newy

def get_t_idx_from_times(t, times):
    """Parse `t` and return an element of `times` closest to `t`.
    
    Args:
        t (float): Time point in ms
        times (list): List of time points in ms
    
    Returns:
        float: An element of `times` closest to `t`
    """
    idx = np.argmin(np.abs(np.array(times) - t))
    return times[idx], idx

# This will be a useful function for future, to explore available functions for a NEURON object
def nrndir(obj):
    print(textwrap.fill(', '.join([x for x in dir(obj) if not x.startswith('_')])))
    
def parse_time_range(t_spec, times):
    """Parse time range specification and return corresponding indices.
    
    Args:
        t_spec (str or slice): Time range specification, e.g.:
            - "10..20s"    (10 to 20 seconds)
            - "-1..500ms"  (−1 to 500 milliseconds)
            - "0..1s"      (0 to 1 second)
            - "100..200"   (100 to 200 milliseconds, default unit)
        times (np.ndarray): Array of time points in milliseconds
    
    Returns:
        slice: Slice object with start and stop indices
    """
    if t_spec is None:
        return slice(None)  # Return full range
        
    if isinstance(t_spec, slice):
        return t_spec
        
    if not isinstance(t_spec, str):
        raise ValueError(f"Time specification must be string or slice, got {type(t_spec)}")
    
    # Parse the range specification
    try:
        start, end = t_spec.split('..')
    except ValueError:
        raise ValueError(f"Invalid time range format: {t_spec}. Use 'start..end' format.")
    
    # Extract units if present
    def parse_time_value(val):
        if val.endswith('ms'):
            return float(val[:-2])  # Already in ms
        elif val.endswith('s'):
            return float(val[:-1]) * 1000  # Convert seconds to ms
        else:
            return float(val)  # Assume ms
            
    try:
        t_start = parse_time_value(start)
        t_end = parse_time_value(end)
    except ValueError as e:
        raise ValueError(f"Could not parse time values in {t_spec}: {e}")
    
    # Find corresponding indices
    idx_start = np.searchsorted(times, t_start)
    idx_end = np.searchsorted(times, t_end)
    
    # Ensure we don't exceed array bounds
    idx_start = max(0, min(idx_start, len(times)-1))
    idx_end = max(0, min(idx_end, len(times)))
    
    return slice(idx_start, idx_end)
    
def get_multipole_expansion_from_line_currents(currents, pts, order=0, r0=np.array([0, 0, 0])):
    """Compute n-th order of multipole expansion of the current. 
    Current is a list of values of the current in units of current (A, mA) and `pts` are 
    points between which the current is flowing.
    
    currents: (array-like of length (N-1,)) list of current values in units of current (A, mA)
    pts: (array-like of length (N, 3)) list of points between which the current is flowing
    order: (int) order of the multipole expansion
    r0: (array-like of length (3)) reference point for the multipole expansion, default: (0, 0, 0)
    """
    npts = len(pts)
    nsegs = len(currents)
    
    if npts - 1 != nsegs:
        raise ValueError("Number of points must be one more than number of segments, "
                        "got `pts` with length {} and `currents` with length {}".format(npts, nsegs))

    if order == 0:
        """Compute monopole expansion, i.e. the vector sum of all the currents."""
        return np.sum(current_vecs, axis=0)
    
    midpoints = (pts[:-1] + pts[1:]) / 2
    seglengths = np.linalg.norm(pts[1:] - pts[:-1], axis=1)
    
    # Pre-allocate arrays
    current_vecs = np.zeros((3, nsegs))
    current_vecs = currents[:, np.newaxis] * (pts[1:] - pts[:-1]) / seglengths[:, np.newaxis]
    
    if order == 1:
        """Compute dipole expansion, i.e. the vector sum of 
        
        \sum_{i=1}^{N-1} seglength_i * \vec{I}_i × (pm_i - r0),
        
        where \vec{I}_i is the computed directed current in `current_vecs`,
        and pm_i is the midpoint between points i and i+1.
        """
        return 0.5 * np.sum(seglengths[:, np.newaxis] *  np.cross(current_vecs, (midpoints - r0)), axis=0)
        
    else:
        raise NotImplementedError(f"Order {order} is not implemented yet")
    
def get_multipole_expansion_from_current_density(currents, pts, volume_element, order=0, r0=np.array([0, 0, 0])):
    """
    
    Input:
        currents: (array-like of length (N, 3)) list of current densities values in units of current (A/m^2)
        pts: (array-like of length (N, 3)) list of points between which the current is flowing
        volume_element: (float) volume element of the current density (m^3)
        
        order: (int) order of the multipole expansion
        
        r0: (array-like of length (3)) reference point for the multipole expansion, default: (0, 0, 0)
    """
    
    if order == 0:
        return np.sum(currents, axis=0) * volume_element
    
    if order == 1:
        return 0.5 * np.sum(np.cross((pts - r0[np.newaxis, :]), currents), axis=0) * volume_element
        # dimensions are: 
        # pts - r0: (N, 3) - (3,) = (N, 3)
        # currents: (N, 3)