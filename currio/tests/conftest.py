import pytest

# Register custom marks
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "benchmark: mark tests that perform benchmarking"
    )

def pytest_addoption(parser):
    parser.addoption("--run-benchmark", action="store_true", default=False,
                     help="run benchmark tests")
    parser.addoption("--only-benchmark", action="store_true", default=False,
                     help="run only benchmark tests")

def pytest_collection_modifyitems(config, items):
    run_benchmark = config.getoption("--run-benchmark")
    benchmark_only = config.getoption("--only-benchmark")
    
    if benchmark_only:
        # If only-benchmark is set, enable running benchmarks automatically
        run_benchmark = True
        skip_non_benchmark = pytest.mark.skip(reason="only running benchmark tests")
        for item in items:
            if "benchmark" not in item.keywords:
                item.add_marker(skip_non_benchmark)
    
    if not run_benchmark:
        skip_benchmark = pytest.mark.skip(reason="need --run-benchmark option to run")
        for item in items:
            if "benchmark" in item.keywords:
                item.add_marker(skip_benchmark)