# currio

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`currio` is a Python package for creating, visualizing and simulating neuron models using NEURON simulator[^1]. It provides an interface for:

- Loading and visualizing 3D neuron morphology from ModelDB (for models which have 3D morphology)
- Running simulations and recording membrane properties (using defined procedures in `.hoc` files)
- Computing and visualizing magnetic fields from neural activity (using Eq. (2) from Karadas et al.[^2] for magnetic field from axial currents)
- Interactive 3D plotting with [PyVista](https://github.com/pyvista/pyvista)
- Saving and loading simulation results

## Table of Contents

- [Installation](#installation)
  - [Requirements](#requirements)
  - [Verifying Installation](#verifying-installation)
- [Models](#models)
  - [Getting Models](#getting-models)
- [Quick Start](#quick-start)
- [Installation for development](#installation-for-development)

## Installation

To install locally and use in a project, download the repository and install the package with `pip`:

```bash
git clone https://github.com/mikeonly/currio.git
cd currio
pip install -e .
```

### Requirements

`currio` requires NEURON simulator (tested with version 8.2.6). To check your NEURON installation:
```bash
pip show neuron
```

If NEURON is not installed, see the [NEURON installation guide](https://nrn.readthedocs.io/en/8.2.6/install/install.html).

### Verifying Installation

To verify everything is working:
```python
import neuron
import currio

print(neuron.__version__)  # Should show 8.2.6 or later
```

## Models

`currio` works with NEURON models from [ModelDB](https://modeldb.science/). Currently tested with:

- [CA1 pyramidal neuron model](https://modeldb.science/55035) (Migliore et al., 2005) - A detailed model showing signal propagation in oblique dendrites of CA1 neurons. The model includes:
  - Cell type: Hippocampus CA1 pyramidal GLU cell
  - Currents: I_Na, I_A, I_K, I_h

### Getting Models

1. Browse [ModelDB](https://modeldb.science/) to find appropriate models
2. Download and extract model files to your local `models/` directory. The folder name is the name `Neuron` object loads the model from (e.g. `n = Neuron("model_folder_name")`), you can rename it to the ModelDB ID (e.g. `55035`) or use the default name, but reference it properly in the code. For example, we will use the model from [Migliore et al., 2005](https://modeldb.science/55035) and rename the folder to `55035` (the default name the downloaded model is extracted to is `obliques`):
   
   ```bash
   models/
   ├── 55035/                 # Folder name must match ModelDB ID
   │   ├── mosinit.hoc       # Main model file
   │   ├── h.mod             # Channel mechanisms
   │   ├── fig2A.hoc         # Simulation procedures
   │   └── ...                # Other files
   └── ...                    # Other models
   ```

   You can either:
   - Rename the extracted folder to the model ID (e.g. `55035`)
   - Or keep the original folder name and use it when creating a neuron.

3. Build model mechanisms
   ```bash
   cd models/55035
   nrnivmodl                 # Compiles .mod files
   ```

4. Reference the model in your code:
   ```python
   # Using model ID number (if folder is named "55035")
   neuron = Neuron(55035)
   # OR using folder name (if different from ID)
   neuron = Neuron("obliques")
   ```

Note: Not all ModelDB models include 3D morphology data. Look for models that use NEURON's `h.Section()` or load morphology from `.swc`/`.hoc` files.

## Quick Start

```python
from currio import IO, Neuron, Sensor

# Load a neuron model from ModelDB
neuron = Neuron(55035)  # CA1 pyramidal cell

# Create a sensor grid
sensor = Sensor(bounds=[[-50,50], [-50,50], [0,10]], resolution=5)

# Run simulation and compute magnetic field
neuron.simulate("superrun")  # Run Long Term Potentiation protocol
sensor.get_B(neuron)    # Compute magnetic field at sensor points

# Visualize results
IO(neuron, sensor).plot()
```

## Installation for development

`pip install --no-build-isolation --no-deps -e .`

After that, in the current python environment, you can import the module with `import currio` and use its functions with `currio.function_name()` everywhere! As a bonus, if you update any files in the `