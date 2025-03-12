import numpy as np
from numba import njit, prange

@njit
def rhohl(sbeg, send, pt):
    l = send - sbeg
    l_norm = np.linalg.norm(l)
    l_hat = l / l_norm
    R = pt - send
    a = np.cross(l_hat, R)
    rho_hat = np.cross(a, l_hat) / np.linalg.norm(a)
    rho = np.dot(R, rho_hat)
    h = np.dot(R, l_hat)
    return rho_hat, rho, h, l_hat, l_norm + h

@njit
def unit_magnetic_field(pt, sbeg, send):
    """Calculate the magnetic field produced by a unit current along the segment sbeg-send at point in space `pt`.
    
    Returns the unit magnetic field vector in T / A.
    """
    rho_hat, rho, h, l_hat, l_norm = rhohl(sbeg, send, pt)
    factor = (h / np.sqrt(h**2 + rho**2) - l_norm / np.sqrt(l_norm**2 + rho**2)) / rho
    unit_B = 1e-1 * np.cross(l_hat, rho_hat) * factor
    return unit_B

@njit(parallel=True)
def get_b_njit(current_pts, pts, current):
    """Calculate the magnetic field produced by a current going through `current_pts` at
    points in space `pts`.
    
    `current_pts` should be of shape (N, 3) where N is the number of points in the current path, and
    `current` should be of shape (N-1, T) where T is the number of time points. `current` direction
    is defined by the direction from `current_pts[i]` to `current_pts[i+1]`.
    """
    npts = len(pts)
    nsegs = len(current_pts) - 1
    nt = current.shape[1]
    B = np.zeros((3, npts, nt))
    
    for i in prange(npts):
        pt = pts[i]
        for j in prange(nsegs):
            p1 = current_pts[j]
            p2 = current_pts[j+1]
            unit_B = unit_magnetic_field(pt, p1, p2)
            B[:, i, :] += np.outer(unit_B, current[j])
    return B

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
    # Check input dimensionality
    is_single = B_fields.ndim == 1
    n_axes = len(nv_axes)
    
    # Handle single B field vector (3,)
    if is_single:
        shifts = np.empty(n_axes, dtype=np.float64)
        
        # Unroll the loop for better performance
        for a in prange(n_axes):
            # Use explicit dot product computation
            B_proj = (B_fields[0] * nv_axes[a, 0] + 
                     B_fields[1] * nv_axes[a, 1] + 
                     B_fields[2] * nv_axes[a, 2])
            shifts[a] = 2.0 * gamma * B_proj
            
        return shifts
        
    # Handle multiple B field vectors (n_points, 3)
    else:
        n_points = len(B_fields)
        shifts = np.empty((n_points, n_axes), dtype=np.float64)
        
        # Pre-compute constants
        factor = 2.0 * gamma
        
        # Parallelize over spatial points
        for p in prange(n_points):
            # Cache B field components for better memory access
            b_x = B_fields[p, 0]
            b_y = B_fields[p, 1]
            b_z = B_fields[p, 2]
            
            for a in prange(n_axes):
                # Manually unrolled dot product for better performance
                B_proj = (b_x * nv_axes[a, 0] + 
                         b_y * nv_axes[a, 1] + 
                         b_z * nv_axes[a, 2])
                shifts[p, a] = factor * B_proj
                
        return shifts