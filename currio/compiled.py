import numpy as np
from numba import njit

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
    rho_hat, rho, h, l_hat, l_norm = rhohl(sbeg, send, pt)
    factor = (h / np.sqrt(h**2 + rho**2) - l_norm / np.sqrt(l_norm**2 + rho**2)) / rho
    unit_B = 1e-1 * np.cross(l_hat, rho_hat) * factor
    return unit_B

@njit
def get_b_njit(pts3d, pts, I):
    nt = I.shape[1]
    B = np.zeros((3, len(pts), nt))
    for i, pt in enumerate(pts):
        for j in range(len(pts3d) - 1):
            for t_idx in range(nt):
                B[:, i, t_idx] += unit_magnetic_field(pt, pts3d[j], pts3d[j+1]) * I[j, t_idx]
    return B
