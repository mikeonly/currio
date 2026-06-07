import numpy as np
from numba import njit, prange

@njit(parallel=True, fastmath=True)
def get_odmr_shifts(B_fields, nv_axes, gamma):
    """Calculate ODMR frequency shifts for B-field vectors and NV orientations.
    
    Efficiently handles different input shapes:
    - Single B field vector: shape (3,)
    - Multiple B field vectors: shape (n_points, 3)
    
    Args:
        B_fields: Magnetic field vector(s)
        nv_axes: NV axes, shape (n_axes, 3)
        gamma: Gyromagnetic ratio in Hz/T
        
    Returns:
        shifts: Frequency shifts with shape:
               - (n_axes,) for single B field input
               - (n_points, n_axes) for multiple B fields
    """
    is_single = B_fields.ndim == 1
    n_axes = len(nv_axes)
    
    if is_single:
        shifts = np.empty(n_axes, dtype=np.float64)
        
        for a in prange(n_axes):
            B_proj = (B_fields[0] * nv_axes[a, 0] + 
                     B_fields[1] * nv_axes[a, 1] + 
                     B_fields[2] * nv_axes[a, 2])
            shifts[a] = 2.0 * gamma * B_proj
            
        return shifts
        
    else:
        n_points = len(B_fields)
        shifts = np.empty((n_points, n_axes), dtype=np.float64)
        
        factor = 2.0 * gamma
        
        for p in prange(n_points):
            b_x = B_fields[p, 0]
            b_y = B_fields[p, 1]
            b_z = B_fields[p, 2]
            
            for a in prange(n_axes):
                B_proj = (b_x * nv_axes[a, 0] + 
                         b_y * nv_axes[a, 1] + 
                         b_z * nv_axes[a, 2])
                shifts[p, a] = factor * B_proj
                
        return shifts
    
@njit(parallel=True, fastmath=True)
def get_multipole_expansion(currents, pts, order=0, r0=None):
    """Compute n-th order of multipole expansion of the current. 
    Current is a list of values of the current in units of current (A, mA) and `pts` are 
    points between which the current is flowing.
    
    currents: (array-like of length (N-1,)) list of current values in units of current (A, mA)
    pts: (array-like of length (N, 3)) list of points between which the current is flowing
    order: (int) order of the multipole expansion
    r0: (array-like of length (3)) reference point for the multipole expansion, default: (0, 0, 0)
    
    Returns:
        (a vector of length (n_order * 3)) n-th order of multipole expansion of the current
    """
    npts = len(pts)
    nsegs = len(currents)
    
    assert npts - 1 == nsegs, "Number of points must be one more than number of segments"
    
    current_vecs = np.zeros((3, nsegs))
    result = np.zeros(3)
    
    for i in prange(nsegs):
        current_vecs[0, i] = currents[i] * (pts[i+1, 0] - pts[i, 0])
        current_vecs[1, i] = currents[i] * (pts[i+1, 1] - pts[i, 1])
        current_vecs[2, i] = currents[i] * (pts[i+1, 2] - pts[i, 2])
    
    if order == 0:
        """Compute monopole expansion, i.e. the vector sum of all the currents."""
        for i in prange(3):
            result[i] = np.sum(current_vecs[i, :])
        return result
    
    elif order == 1:
        """Compute dipole expansion, i.e. the vector sum of 
        
        \sum_{i=1}^{N-1} \vec{I}_i × (pm_i - r0),
        
        where \vec{I}_i is the computed directed current in `current_vecs`,
        and pm_i is the midpoint between points i and i+1.
        """
        midpoints = np.zeros((nsegs, 3))
        for i in prange(nsegs):
            midpoints[i, 0] = 0.5 * (pts[i, 0] + pts[i+1, 0])
            midpoints[i, 1] = 0.5 * (pts[i, 1] + pts[i+1, 1])
            midpoints[i, 2] = 0.5 * (pts[i, 2] + pts[i+1, 2])
        
        for i in prange(nsegs):
            rx = midpoints[i, 0] - r0[0]
            ry = midpoints[i, 1] - r0[1]
            rz = midpoints[i, 2] - r0[2]
            
            result[0] += current_vecs[1, i] * rz - current_vecs[2, i] * ry
            result[1] += current_vecs[2, i] * rx - current_vecs[0, i] * rz
            result[2] += current_vecs[0, i] * ry - current_vecs[1, i] * rx
            
        return result
    
    else:
        raise NotImplementedError(f"Order {order} is not implemented yet")
