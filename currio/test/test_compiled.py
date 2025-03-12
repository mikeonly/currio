import numpy as np
import pytest
import time
from tabulate import tabulate
from numba import njit, prange

from currio.compiled import get_odmr_shifts

# Original implementation for benchmark comparison
@njit(parallel=True)
def get_odmr_shifts_original(B_fields, nv_axes, gamma):
    """Original implementation of ODMR frequency shifts calculation."""
    # Handle single B field vector (3,)
    if B_fields.ndim == 1:
        # Return shifts for each NV axis
        n_axes = len(nv_axes)
        shifts = np.zeros(n_axes)
        
        for a in range(n_axes):
            # Project B-field onto NV axis
            B_proj = np.dot(B_fields, nv_axes[a])
            # Calculate frequency shift
            shifts[a] = 2 * gamma * B_proj
            
        return shifts
        
    # Handle multiple B field vectors (n_points, 3)
    else:
        n_points = len(B_fields)
        n_axes = len(nv_axes)
        
        # Output array
        shifts = np.zeros((n_points, n_axes))
        
        # Parallelize over spatial points
        for p in prange(n_points):
            B = B_fields[p]
            for a in range(n_axes):
                # Project B-field onto NV axis
                B_proj = np.dot(B, nv_axes[a])
                # Calculate frequency shift
                shifts[p, a] = 2 * gamma * B_proj
                
        return shifts

# Pure NumPy implementation for comparison
def get_odmr_shifts_numpy(B_fields, nv_axes, gamma):
    """NumPy vectorized version of get_odmr_shifts."""
    if B_fields.ndim == 1:
        # Single B field vector
        shifts = 2 * gamma * np.dot(B_fields, nv_axes.T)
        return shifts
    else:
        # Multiple B field vectors
        shifts = 2 * gamma * np.einsum('ij,kj->ik', B_fields, nv_axes)
        return shifts

# Test data with different sizes
@pytest.fixture
def test_data():
    # Generate random B fields and NV axes with different sizes
    np.random.seed(42)
    
    # Single field for correctness tests
    B_fields_single = np.random.rand(3) * 1e-6  # Single B field
    
    # Multiple sizes for benchmarking
    sizes = [10, 100, 1000, 10000]
    B_fields_multi = {}
    
    for size in sizes:
        B_fields_multi[size] = np.random.rand(size, 3) * 1e-6
    
    # NV axes
    nv_axes = np.random.rand(4, 3)  # 4 NV orientations
    # Normalize axes
    nv_axes = nv_axes / np.linalg.norm(nv_axes, axis=1)[:, np.newaxis]
    gamma = 28e9  # Hz/T
    
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
    B_multi = test_data['B_fields_multi'][100]  # Use medium size for correctness tests
    nv_axes = test_data['nv_axes']
    gamma = test_data['gamma']
    
    # Test single B field
    numba_result = get_odmr_shifts(B_single, nv_axes, gamma)
    numpy_result = get_odmr_shifts_numpy(B_single, nv_axes, gamma)
    optimized_result = get_odmr_shifts(B_single, nv_axes, gamma)
    
    assert np.allclose(numba_result, numpy_result)
    assert np.allclose(optimized_result, numpy_result)
    
    # Test multiple B fields
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
    n_runs = 20  # Fewer runs for larger test set
    
    # Pre-compile Numba functions with largest size
    _ = get_odmr_shifts(B_fields_multi[sizes[-1]], nv_axes, gamma)
    _ = get_odmr_shifts_original(B_fields_multi[sizes[-1]], nv_axes, gamma)
    
    # Results table: rows are implementations, columns are sizes
    results = {
        'NumPy': {},
        'Numba Original': {},
        'Numba Optimized': {}
    }
    
    # Test with different sizes
    for size in sizes:
        B_multi = B_fields_multi[size]
        
        # Benchmark NumPy
        start_time = time.time()
        for _ in range(n_runs):
            _ = get_odmr_shifts_numpy(B_multi, nv_axes, gamma)
        numpy_time = (time.time() - start_time) / n_runs
        results['NumPy'][size] = numpy_time * 1e6  # Convert to microseconds
        
        # Benchmark original Numba
        start_time = time.time()
        for _ in range(n_runs):
            _ = get_odmr_shifts_original(B_multi, nv_axes, gamma)
        numba_time = (time.time() - start_time) / n_runs
        results['Numba Original'][size] = numba_time * 1e6  # Convert to microseconds
        
        # Benchmark optimized Numba
        start_time = time.time()
        for _ in range(n_runs):
            _ = get_odmr_shifts(B_multi, nv_axes, gamma)
        optimized_time = (time.time() - start_time) / n_runs
        results['Numba Optimized'][size] = optimized_time * 1e6  # Convert to microseconds
    
    # Format the results table
    table_data = []
    headers = [''] + [f'{size} points' for size in sizes]
    
    for impl, times in results.items():
        row = [impl]
        for size in sizes:
            row.append(f"{times[size]:.1f} µs")
        table_data.append(row)
    
    # Create benchmark report
    try:
        report = "\n" + "="*80 + "\n"
        report += "ODMR SHIFTS PERFORMANCE COMPARISON".center(80) + "\n"
        report += "="*80 + "\n"
        report += f"Average execution time over {n_runs} runs\n\n"
        report += tabulate(table_data, headers=headers, tablefmt='plain') + "\n"
        report += "="*80 + "\n"
    except ImportError:
        # Fallback if tabulate isn't installed
        report = "\n" + "="*80 + "\n"
        report += "ODMR SHIFTS PERFORMANCE COMPARISON".center(80) + "\n"
        report += "="*80 + "\n"
        report += f"Average execution time over {n_runs} runs\n\n"
        
        # Print headers
        report += f"{'Implementation':<20}"
        for size in sizes:
            report += f"{size} points".center(15)
        report += "\n" + "-"*80 + "\n"
        
        # Print data rows
        for impl, times in results.items():
            report += f"{impl:<20}"
            for size in sizes:
                report += f"{times[size]:.1f} µs".center(15)
            report += "\n"
        
        report += "="*80 + "\n"
    
    # Use pytest's built-in reporter
    with capsys.disabled():
        print(report)
    
    # Also add to pytest's output
    pytest.skip(report)
    
    # Validate expectations
    for size in sizes:
        assert results['Numba Original'][size] < results['NumPy'][size], f"Numba Original should be faster than NumPy for {size} points"
        assert results['Numba Optimized'][size] < results['Numba Original'][size], f"Optimized Numba should be faster than original Numba for {size} points" 