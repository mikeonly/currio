# MODELS 
Description of models downloaded and used. 

- 55035 - Migliore M, Ferrante M, Ascoli GA — Signal propagation in oblique dendrites of CA1 pyramidal cells (2005):
Analysis of the magnetic field of a realistic 3D model of a neuron.

- 144976 - Culmone V, Migliore M — Progressive effect of beta-amyloid peptides accumulation on CA1 
pyramidal neurons: a model study suggesting possible treatments ((2012)


# MATERIALS

https://github.com/mcdougallab/neuron-course-june-2022/tree/main/notebooks

Watching this video (it's a part of playlist)
https://www.youtube.com/watch?v=KVFTgNv0JAk&list=PLydMjAmHmOmj8gCwQPvedIwJqqJAmMqYe&index=8

## How to extract 3D point values and their corresponding voltages, currents and other information vs. time?

14.05.2024: Current issue is that I cannot run `python` code and import
succesfully `.hoc` files via VS Code. Seems to be a working directory issue. Try
running directly `python` in the right folder? Tried it. It results in no error
with the import, but NEURON interfaces flashes without staying on the screen. 

9.09.2024: To compile model files, run `nrnivmodl` in the model folder. This

# MEETINGS
## October 28, 2024

We are looking for models that we can simulate that have multiple neurons. The
IDEA is TO SIMULATE MALFUNCTIONING and see if we detect it in the magnetic
field.

List of models: https://modeldb.science/149739?tab=1 (non working)
https://modeldb.science/149739 - A two-layer biophysical olfactory bulb model of
cholinergic neuromodulation (Li and Cleland 2013) -

https://modeldb.science/modellist/3536 https://modeldb.science/246546
https://modeldb.science/256311 https://modeldb.science/185021

[^sajan] https://modeldb.science/186768 - (NICOLETTI's choice) - can simulate
networks of neuron

This is a two-layer biophysical olfactory bulb (OB) network model to study
cholinergic neuromodulation. Simulations show that nicotinic receptor activation
sharpens mitral cell receptive field, whi...

THE IDEA: replace parameters of CA1 with that of CA3 from paper [^sajan] that
exhibits epilleptic and schisophrenic behaviour. **Reading THESE 3 PAPERS**, can
we use these parameters for our model?

https://modeldb.science/138205 CA1 pyramidal neuron: schizophrenic behavior
(Migliore et al. 2011) NEURON files from the paper: A modeling study suggesting
how a reduction in the context-dependent input on CA1 pyramidal neurons could
generate schizophrenic behavior. by M. Migliore, I. De Blasi,...

https://modeldb.science/144976 CA1 pyramidal neurons: effects of Alzheimer
(Culmone and Migliore 2012) The model predicts possible therapeutic treatments
of Alzheimers's Disease in terms of pharmacological manipulations of channels'
kinetic and activation properties. The results suggest how and whic...

https://modeldb.science/118986 CA1 pyramidal neurons: effects of a Kv7.2
mutation (Miceli et al. 2009) NEURON mod files from the paper: Miceli et al,
Neutralization of a unique, negatively-charged residue in the voltage sensor of
K(V)7.2 subunits in a sporadic case of benign familial neonatal sei...

# November 22, 2024

Run simulation with fixed input (try IClamp in soma) and remove random synapses.
Fix pathologies on the membrane (so that they are not randomly distributed
between runs).

Martina looks for other pathologies: multiple sclerosis. 

We ran `144976` files. What we learned:

- Run `nrngui h.mod` starts a GUI with the simulation, it also load variables
  and procedures to the CLI `oc>`. 
- `dann` is a strange vector so far, (how to determine its length? It says
  Vector[5] but in it, there are more elements.) [Lines
  278:280](file:///Users/mf/Documents/Helmholtz%20Institute%20Mainz/Neuron/144976/membrane_potential.hoc)

# December 5, 2024

Let's try running the simulation with the `144976` model.
Use the same built-in parameters as in the model definition, but use the analysis for the `obliques`,
model `55035`. 

# December 6, 2024

Model `144976` runs, `superrun()` is there to run with default parameters, which I suppose reflect a healthy, control, neuron.

We need to compare these conditions:
1. No spike: cf. pathology and no pathology cases. No spike happens when input was not enough to trigger an action potential.
2. Spike: cf. pathology and no pathology. Spike happens when input was enough to trigger an action potential.

WHAT'S DONE:
- ability to run `superrun` from Python
- figured out `ra`, `rb`, `r` params (see .hoc file)

WHAT'S MISSING:

Next time, for that, we need to set and control 
  a) input locations (`location` variable needs to be tracked and fixed between runs) 
  b) aux. parameters for synaptic input: weight and time delays. 
  c) control affected membrane regions which are generated randomly.

Quick to-do list for the next time
- [ ] Create a vector that tracks locations for inputs, and an option to fix them between runs, and another vector that tracks the affected membrane regions.
- [ ] Create a way to visualize magnetic field not only as a function of a slice location, but also through time. There should be a slider in PyVista, explore that. It makes sense to extract a function similar to `run_simulation` that would return an object for tracking simulations. Each simulation contains a list of measurement points (a PyVista array) and conditions. It makes sense to somehow reference a name of a procedure that resulted in the given simulation.
  THE RESULT: should be that we have similar measurement points for different conditions, and we should compare them.
  What are relevant parameters? a) input locations and their parameters: weights and delays, b) affected membrane regions. 

# December 17, 2024

Refactoring to provide a library-like interface for running simulations. 
The goal is to be able to easily run simulations to obtain a workable and saveable object (file) that contains all the necessary information about the simulation and its results:

→ TASK: Calculate the magnetic field that would be measured at a position of a realisitc diamond. 

What are the dimensions of the realistic diamond? 
Muhib: 5×5×0.5 mm^3 with a 10 um layer of NVs

For refactoring, I need to create a class that would be instantiated with the model (probably string that has a number of the model in the ModelDB). Actually, in general, it would be useful to have a class that is agnostic to the source, but which has .get_B() method that returns the magnetic field at a given point. 

`.get_sensor_B()` can be a method that takes a sensor grid and propagates the values of the magnetic field at each point to that grid. 

What to do with time dependence?
Every mesh can have .field_arrays['TIME'] that would contain the time value of the mesh. Mesh will have the appropriate field calculation at that time. See [pyvista/#412](https://github.com/pyvista/pyvista/issues/412). 
  
To implement a slider to choose a timestep, I can use this: [pyvista/#54](https://github.com/pyvista/pyvista/pull/65)

# December 18, 2024

WHAT'S DONE:
- `Neuron` class that can be instantiated with a model number, string, or a path and has a method `.get_3d_model()` that returns a PyVista mesh of the neuron.
- `Neuron` class has a dictionary `.data_3d` that contains the data of the 3D model.
- `Sensor` class can be instantiated with some bounds and resolutions and it outputs also a mesh that can be plotted together. 

WHAT'S MISSING:
- [ ] Implement a method `.simulate()` that would run a simulation procedure in the NEURON and save the results in the `Neuron` object: what are the parameters that need to be saved? Probably the name of the procedure, since there can be multiple simulations. What are the benefits of creating a separate class for the simulation? (Currently I see only added complexity.)
- [ ] Implement a method `.get_B()` from a source that would propagate values of a magnetic field to the `Sensor` object.
- [ ] Calculate the effect the spread of the magnetic field across the sensor has on the detected ODMR. For that, we need a realistic diamond size. We can then calculate the magnetic field and find it's variation across the diamond. It's interesting to calculate the spread of the ODMR frequencies. The intensity of that frequency would be proportional to the volume of the diamond that experiences that field.
  
Really a pie in the sky idea:

+ That would be nice to be able to select a point on a sensor and the what would be the measured ODMR plot at that point. 
+ Another nifty feature would be to have a sphere with θ and φ sliders that would select an NV axis and show the correspodning ODMR plot.


# TODO

- [ ] Derive vector calculus results that allow to compute the magnetic field around a neuron by accounting only for axial current dipoles $\vec{I}$. 
- [ ] Add a `__str__` method for `Neuron` object that outputs the model number and a short description from the ModelDB or README file of the model folder. 
