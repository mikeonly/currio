import numpy as np
import pytest
import time
from tabulate import tabulate
from numba import njit, prange

from currio.compiled import get_odmr_shifts

@njit(parallel=True)
def get_odmr_shifts_original(B_fields, nv_axes, gamma):
    """Original implementation of ODMR frequency shifts calculation."""
    if B_fields.ndim == 1:
        n_axes = len(nv_axes)
        shifts = np.zeros(n_axes)
        
        for a in range(n_axes):
            B_proj = np.dot(B_fields, nv_axes[a])
            shifts[a] = 2 * gamma * B_proj
            
        return shifts
        
    else:
        n_points = len(B_fields)
        n_axes = len(nv_axes)
        
        shifts = np.zeros((n_points, n_axes))
        
        for p in prange(n_points):
            B = B_fields[p]
            for a in range(n_axes):
                B_proj = np.dot(B, nv_axes[a])
                shifts[p, a] = 2 * gamma * B_proj
                
        return shifts

def get_odmr_shifts_numpy(B_fields, nv_axes, gamma):
    """NumPy vectorized version of get_odmr_shifts."""
    if B_fields.ndim == 1:
        shifts = 2 * gamma * np.dot(B_fields, nv_axes.T)
        return shifts
    else:
        shifts = 2 * gamma * np.einsum('ij,kj->ik', B_fields, nv_axes)
        return shifts

@pytest.fixture
def test_data():
    np.random.seed(42)
    
    B_fields_single = np.random.rand(3) * 1e-6
    
    sizes = [10, 100, 1000, 10000]
    B_fields_multi = {}
    
    for size in sizes:
        B_fields_multi[size] = np.random.rand(size, 3) * 1e-6
    
    nv_axes = np.random.rand(4, 3)
    nv_axes = nv_axes / np.linalg.norm(nv_axes, axis=1)[:, np.newaxis]
    gamma = 28e9
    
    return {
        'B_fields_single': B_fields_single,
        'B_fields_multi': B_fields_multi,
        'sizes': sizes,
        'nv_axes': nv_axes,
        'gamma': gamma
    }


def test_get_odmr_shifts_correctness(test_data):
    """Test that all implementations give same results."""
    B_single = test_data['B_fields_single']
    B_multi = test_data['B_fields_multi'][100]
    nv_axes = test_data['nv_axes']
    gamma = test_data['gamma']
    
    numba_result = get_odmr_shifts(B_single, nv_axes, gamma)
    numpy_result = get_odmr_shifts_numpy(B_single, nv_axes, gamma)
    optimized_result = get_odmr_shifts(B_single, nv_axes, gamma)
    
    assert np.allclose(numba_result, numpy_result)
    assert np.allclose(optimized_result, numpy_result)
    
    numba_result = get_odmr_shifts(B_multi, nv_axes, gamma)
    numpy_result = get_odmr_shifts_numpy(B_multi, nv_axes, gamma)
    optimized_result = get_odmr_shifts(B_multi, nv_axes, gamma)
    
    assert np.allclose(numba_result, numpy_result)
    assert np.allclose(optimized_result, numpy_result)

@pytest.mark.benchmark
def test_benchmark_by_size(test_data, capsys):
    """Benchmark implementations with different numbers of points."""
    sizes = test_data['sizes']
    B_fields_multi = test_data['B_fields_multi']
    nv_axes = test_data['nv_axes']
    gamma = test_data['gamma']
    n_runs = 20
    
    _ = get_odmr_shifts(B_fields_multi[sizes[-1]], nv_axes, gamma)
    _ = get_odmr_shifts_original(B_fields_multi[sizes[-1]], nv_axes, gamma)
    
    results = {
        'NumPy': {},
        'Numba Original': {},
        'Numba Optimized': {}
    }
    
    for size in sizes:
        B_multi = B_fields_multi[size]
        
        start_time = time.time()
        for _ in range(n_runs):
            _ = get_odmr_shifts_numpy(B_multi, nv_axes, gamma)
        numpy_time = (time.time() - start_time) / n_runs
        results['NumPy'][size] = numpy_time * 1e6
        
        start_time = time.time()
        for _ in range(n_runs):
            _ = get_odmr_shifts_original(B_multi, nv_axes, gamma)
        numba_time = (time.time() - start_time) / n_runs
        results['Numba Original'][size] = numba_time * 1e6
        
        start_time = time.time()
        for _ in range(n_runs):
            _ = get_odmr_shifts(B_multi, nv_axes, gamma)
        optimized_time = (time.time() - start_time) / n_runs
        results['Numba Optimized'][size] = optimized_time * 1e6
    
    table_data = []
    headers = [''] + [f'{size} points' for size in sizes]
    
    for impl, times in results.items():
        row = [impl]
        for size in sizes:
            row.append(f"{times[size]:.1f} µs")
        table_data.append(row)
    
    report = "\n" + "="*80 + "\n"
    report += "ODMR SHIFTS PERFORMANCE COMPARISON".center(80) + "\n"
    report += "="*80 + "\n"
    report += f"Average execution time over {n_runs} runs\n\n"
    report += tabulate(table_data, headers=headers, tablefmt='plain') + "\n"
    report += "="*80 + "\n"

    with capsys.disabled():
        print(report)
    
    pytest.skip(report)
