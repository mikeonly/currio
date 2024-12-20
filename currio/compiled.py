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
            unit_B = unit_magnetic_field(pt, current_pts[j], current_pts[j+1])
            for t_idx in range(nt):
                B[:, i, t_idx] += unit_B * current[j, t_idx]
    return B
