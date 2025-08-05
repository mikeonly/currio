import numpy as np
import pytest
import time
from tabulate import tabulate
from numba import njit, prange
import magpylib as magpy


from currio.compiled import get_multipole_expansion
from currio.utils import get_multipole_expansion_from_current_density, get_multipole_expansion_from_line_currents

"""Test basic multipole expansions which are known analytically."""

def test_current_square_monopole():
    """Test monopole expansion of a square current loop. 
    Should be zero, since current is flowing in a closed loop.
    """
    currents = np.array([1, 1, 1, 1])
    pts = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 0]])
    r0 = np.sum(pts, axis=0) / 4
    order = 0
    result = get_multipole_expansion(currents, pts, order, r0)
    assert np.allclose(result, np.array([0, 0, 0]))
    
def test_current_square_dipole():
    """Test dipole expansion of a square current loop.
    Should be equal to current multiplied by the area of the square, and 
    directed along the z-axis (normal to the plane of the square).
    """
    currents = np.array([1, 1, 1, 1])
    pts = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 0]])
    r0 = np.sum(pts, axis=0) / 4
    order = 1
    result = get_multipole_expansion(currents, pts, order, r0)
    assert np.allclose(result, np.array([0, 0, 1]))
    
def create_loop(current, diameter, n=50):
    """Create a descritized loop with n points."""
    loop_pts = np.array([[np.sin(2*np.pi*i/n), np.cos(2*np.pi*i/n), 0] for i in range(n+1)])
    current = current * np.ones(n)
    return loop_pts, current
    
def test_current_loop_monopole():
    """Test monopole expansion of a circular current loop.
    Should be zero, since current is flowing in a closed loop.
    """
    pts, current = create_loop(1, 1, n=200)
    r0 = [0, 0, 0]
    order = 0
    result = get_multipole_expansion_from_line_currents(current, pts, order, r0)
    assert np.allclose(result, np.array([0, 0, 0]))
    
def test_current_loop_dipole():
    """Test dipole expansion of a circular current loop.
    Should be equal to current multiplied by the area of the loop, and 
    directed along the z-axis (normal to the plane of the loop).
    """
    pts, current = create_loop(1, 1, n=200)
    r0 = [0, 0, 0]
    order = 1
    result = get_multipole_expansion_from_line_currents(current, pts, order, r0)
    assert np.allclose(result, np.array([0, 0, np.pi]))
    
    
def test_square_current_density_multipole():
    currents = np.array([
        [1, 1, 0] / np.sqrt(2), [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, -1, 0] / np.sqrt(2),
        [0, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, -1, 0],
        [0, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, -1, 0],
        [0, 1, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, -1, 0],
        [-1, 1, 0] / np.sqrt(2), [-1, 0, 0], [-1, 0, 0], [-1, 0, 0], [-1, -1, 0] / np.sqrt(2),
    ])

    pts = np.array([
        [0, 4, 0], [1, 4, 0], [2, 4, 0], [3, 4, 0], [4, 4, 0],
        [0, 3, 0], [1, 3, 0], [2, 3, 0], [3, 3, 0], [4, 3, 0],
        [0, 2, 0], [1, 2, 0], [2, 2, 0], [3, 2, 0], [4, 2, 0],
        [0, 1, 0], [1, 1, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0],
        [0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0],
    ])
    
    volume_element = 1
    order = 0
    result = get_multipole_expansion_from_current_density(currents, pts, volume_element, order)
    expect = 0
    assert np.allclose(result, expect)
    
    order = 1
    result = get_multipole_expansion_from_current_density(currents, pts, volume_element, order)
    expect = 1 * 25
    assert np.allclose(result, 25)
    
def test_square_current_density_multipole_2():
    """Test monopole expansion of a square current loop.
    Should be zero, since current is flowing in a closed loop.
    """
    N = 200
    delta_xy = 1 / N
    delta_z = 1 / N
    
    currents = np.zeros((N, N, 3))
    currents[0, 0, :] = [-1, 1, 0] / np.sqrt(2)
    currents[0, -1, :] = [1, 1, 0] / np.sqrt(2)
    currents[1, 1, :] = [1, -1, 0] / np.sqrt(2)
    currents[-1, 0, :] = [-1, -1, 0] / np.sqrt(2)
    
    # sides
    currents[1:-1, 0, :] = [-1, 0, 0]  # bottom
    currents[1:-1, -1, :] = [1, 0, 0]  # top
    currents[0, 1:-1, :] = [0, 1, 0]    # left
    currents[-1, 1:-1, :] = [0, -1, 0] # right
    currents = currents.reshape(-1, 3)
    
    xs, ys, zs = np.meshgrid(np.linspace(0, 1, N), np.linspace(0, 1, N), [0], indexing='ij')
    pts = np.concatenate([xs, ys, zs], axis=2)
    pts = pts.reshape(-1, 3)
    
    r0 = np.array([0, 0, 0])
    volume_element = delta_xy ** 2 * delta_z
    cross_section_area = delta_xy * delta_z
    current_density = currents / cross_section_area # A/m^2
    
    order = 0
    result = get_multipole_expansion_from_current_density(current_density, pts, volume_element, order)
    expect = 0
    assert np.allclose(result, expect)
    
    order = 1
    result = get_multipole_expansion_from_current_density(current_density, pts, volume_element, order)
    expect = -1
    assert np.allclose(result, expect)