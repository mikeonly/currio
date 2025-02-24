# MODELS 
Description of models downloaded and used. 

- 55035 - Migliore M, Ferrante M, Ascoli GA — Signal propagation in oblique dendrites of CA1 pyramidal cells (2005):
  Analysis of the magnetic field of a realistic 3D model of a neuron.

- 144976 - Culmone V, Migliore M — Progressive effect of beta-amyloid peptides accumulation on CA1 pyramidal neurons: a model study suggesting possible treatments (2012)

- 226812 - Van Dijck G et al. — Enhancing the yield of high-density electrode arrays through automated electrode selection (2012):
  This is a 5-neuron model of neocortex, containing one tufted layer-5 pyramidal cell, two non-tufted pyramidal cells, and two inhibitory interneurons. It was used to reproduce extracellular spike shapes in a study comparing algorithms for spike sorting and electrode selection. The neuron models are adapted from Dyhrfjeld-Johnsen et al. (2005). 

  > Uses Python bindings to create the 3D model, so far I have not managed to integrate this Python loading scheme with the inspection of the model. 

- 266775 - Lindroos R, Hellgren Kotaleski J — Predicting complex spikes in striatal projection neurons of the direct pathway following neuromodulation by acetylcholine and dopamine (2020):
  A detailed model of striatal projection neurons with morphological reconstructions and multiple ion channel mechanisms. Investigates how acetylcholine and dopamine modulation affects complex spike generation in direct pathway neurons.

# DOCUMENTATION

To compile model files, run `nrnivmodl` in the model folder.

# MATERIALS

https://github.com/mcdougallab/neuron-course-june-2022/tree/main/notebooks

Watching this video (it's a part of playlist)
https://www.youtube.com/watch?v=KVFTgNv0JAk&list=PLydMjAmHmOmj8gCwQPvedIwJqqJAmMqYe&index=8

## How to extract 3D point values and their corresponding voltages, currents and other information vs. time?

14.05.2024: Current issue is that I cannot run `python` code and import
successfully `.hoc` files via VS Code. Seems to be a working directory issue. Try
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

## January 17, 2025

- Seems to be no models that model myelination of the neuron (only axon). Perhaps it's an interesting direction to explore. 
- Study of the synapses: complicated? Because we do not have a 3D model of the synapse, we will need to study the processes there. Myelination effect should be easier. 

We need a simpler model with just an axon to model the myelination effect. 

+ Send Martina the `currio` code. 

## January 31, 2025

Martina found a model with myelination: 
[Myelin dystrophy impairs signal transmission and working memory in a multiscale model of the aging prefrontal cortex](https://elifesciences.org/articles/90964#s4)

Myelin and magnetic field paper
[A Physical Perspective to the Inductive Function of Myelin—A Missing Piece of Neuroscience](https://www.frontiersin.org/journals/neural-circuits/articles/10.3389/fncir.2020.562005/full)

As a starting point, we should use the model from the first paper and check the magnetic field. 

The model is:
[ModelDB: 2014821](https://modeldb.science/2014821)



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
- [ ] Create a way to visualize magnetic field not only as a function of a slice location, but also through time. There should be a slider in PyVista, explore that. It makes sense to extract a function similar to `run_simulation` that would return an object for tracking simulations. Each simulation contains a list of measurement points (a PyVista array) and conditions. It makes sense to reference a name of a procedure that resulted in the given simulation.
  
THE RESULT: should be that we have similar measurement points for different conditions, and we should compare them.

What are relevant parameters? a) input locations and their parameters: weights and delays, b) affected membrane regions. 

# December 17, 2024

Refactoring to provide a library-like interface for running simulations. 
The goal is to be able to easily run simulations to obtain a workable and saveable object (file) that contains all the necessary information about the simulation and its results:

- [ ] TASK: Calculate the magnetic field that would be measured at a position of a realisitc diamond. 

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
- `Sensor` class can be instantiated with some bounds and resolutions and it outputs also a mesh that can be plotted together with the neuron. 

WHAT'S MISSING:
- [x] Implement a method `.simulate()` that would run a simulation procedure in the NEURON and save the results in the `Neuron` object: what are the parameters that need to be saved? Probably the name of the procedure, since there can be multiple simulations. What are the benefits of creating a separate class for the simulation? (Currently I see only added complexity.)
- [x] Implement a method `.get_B()` from a source that would propagate values of a magnetic field to the `Sensor` object.
- [ ] Calculate the effect the spread of the magnetic field across the sensor has on the detected ODMR. For that, we need a realistic diamond size. We can then calculate the magnetic field and find its variation across the diamond. It's interesting to calculate the spread of the ODMR frequencies. The intensity of photoluminescence at a given frequency would be proportional to the volume of the diamond that experiences that field.
  
Really a pie in the sky idea:

+ That would be nice to be able to select a point on a sensor and see what would be the measured ODMR plot at that point. 
+ Another nifty feature would be to have a sphere with θ and φ sliders that would select an NV axis and show the corresponding ODMR plot.

# December 25, 2024

Getting back to work on the project. From obvious, what is missing, is a way to save `Neuron` project and some associated `Sensor` objects to be loaded later. It would save time from running the simulation again and computing the magnetic field. What is the structure there? I don't know exactly how it is *best* done, but the way to proceed is to have a `Neuron` object that has a method `.save()` that saves the object to a file (i.e. to have *something* done). It should also have a method `.load()` that loads the object from a file.

What is saved? 
- `Sensor` object
  - for `Sensor`, it has an associated `B` field, 
- `.propagations`: list of `Propagation`, it does not need to be a separate class, just a dictionary with `sensor` and `neuron.record` from which the propagation is done. 

- [done: Feb 10, 2025] Implement a method `.save()` for `Neuron` object that saves the object to a file.
- [done: Feb 10, 2025] Implement a method `.load()` for `Neuron` object that loads the object from a file.

Loading a saved neuron should restore the Neuron object with different propagations. 

What is the goal here?

- [ ] Calculate the effect the spread of the magnetic field across the sensor has on the detected ODMR. For that, we need a realistic diamond size: it is — 5×5×0.5 mm^3 with a 10 um layer of NVs. I.e. make a sensor of that size with a resolution of 0.5 um.
- [ ] Implement setting up size of a sensor with physical units and with a given resolution, i.e. to be able to say `sensor = Sensor(bounds=("5 um", "5 um", "0.5 um"), resolution="0.5 um")`.

After that is done, we can implement `sensor.get_ODMR()` that would calculate the ODMR at a given point of the sensor. Later, we should plot at several points and see how the ODMR changes across the sensor.

- [ ] Implement recording what dendrites get synaptic inputs and when. 
- [ ] Implement repeating same inputs for different simulations.

# January 8, 2025

Next meeting is on Friday, January 10, 2025. I need to implement:

- [ ] Tracking input locations and affected membrane regions between runs.
  It should visualize the input locations and affected membrane regions (i.e. adjust the result mesh of the neuron upon request, and most importantly, track them and save them for exact repetition of the same simulation).
- [ ] Visualize the magnetic field as a function of time. 
  
# January 15, 2025

Another idea from Arian:
- Model the magnetic field from a synapse to see if effect the Ca2+ currents on the polarized Xe atoms can be detected in relaxometry.

- [ ] Find models of synapses with Ca2+ currents.

# January 16, 2025

Yesterday, I couldn't clearly find a model where there might be a real 3D model of a synapse. I downloaded the `2014822`, but couldn't inspect its constituents. Building the neuron works: for that, I extracted a part from `manual_run.py` and adjusted it slightly: 

```python
from src.neuron_builder import NeuronBuilder
from src.synapse_builder_ampanmdasynplast import AMPANMDASynPlastBuilder 

neuron_model = NeuronBuilder(hocfile="cell_seed4_0_control_cell.hoc")
synapse = AMPANMDASynPlastBuilder()

neuron_parameters = { 'nr2bmult': 1}
synapse_parameters = {}
neuron_model.set_parameters(neuron_parameters)
synapse.set_parameters(synapse_parameters)
```

I have also adjusted the `os` module to mimic passing the command line arguments to the `manual_run.py` script:

```python
import os
# Set MILEDIDEBUG environment variable if not already set
# This variable is used in neuron_builder.py to determine whether to print debug messages
# The design was to envoke `manual_run.py` or `auto_run.py` from the command line with 
# the -d flag to print debug messages
if 'MILEDIDEBUG' not in os.environ:
    os.environ['MILEDIDEBUG'] = '0'  # '0' for no debug output, '1' for debug output
```

However, that creates a neuron in an instance of the NEURON which I cannot inspect — I do not know where it is. 

The next steps would be to try finding other models that have a synapse, which do not have this complicated loading procedure through Python. 

I searched (Googled and ChatGPTed) but didn't find any such models. All networks models do not have physical connection in 3D, as far as I understand. They instead use a `NetCon` object to connect neurons, which are fictitious (not physical) connections.

The solution would be to use any model (e.g. the original model `55035`) and find all synapses in it, as well as identify the Ca2+ currents occurring at the synapse. Then I can use a physical model of a synapse from elsewhere to calculate the magnetic field at a given point. To-dos:

- [>] Use `55035` and find all synapses in it.
- [ ] Visualize the synapse in 3D.
- [ ] Identify the Ca2+ currents at the synapse.
- [ ] Track the Ca2+ currents in time during the simulation.
- [ ] Find a physical model of a synapse that has a 3D model of the synapse. 
  
# January 17, 2025

- [ ] Find all sections and their segments where synapses are. 
- [ ] Add them to a plot.

# January 29, 2025

Getting back to work on the project, again. What is missing, and where do we go? 

# February 10, 2025

Implemented `io` module that handles input/output operations on `Neuron` and `Sensor` objects. Currently, there is `.save()` method for `Neuron` that saves the object to a file, it does not expand existing files and handles only the situation of a single neuron and a single sensor. 

What's missing:

- [ ] Implement `.load()` method for `io` that loads the `Neuron`s and `Sensor`s from a file.
- [ ] Make possible choosing a certain time as an active array in `Sensor` and `Neuron` mesh VTK objects. 

After that, I can work on computing the magnetic field at a larger number of point, without the fear of computational cost, as I will be able to load the results from a file, immediately. 

Next step would be to have the magnetic field computed at a realistic sensor distances. As we have established, the sensor is a 5x5x0.5 mm^3 diamond with a resolution of 0.5 um. However, this resolution is too fine for realistic computation time. Therefore, we can reduce resolution to 1 um, and limit the size of the sensor. After that, what would we like to know?

- We want to know what ODMRs are present at a given point of the sensor. For that, we would need to implement a method `.get_ODMR()` for `Sensor` object, or starting with just a point `.get_ODMR_at_point()`.
- We can also implement a visualization of the magnetic field with the `io` object, using the visualization procedure in VTK that we have already implemented.


# TODO

- [ ] Derive vector calculus results that allow to compute the magnetic field around a neuron by accounting only for axial current dipoles $\vec{I}$. 
- [ ] Add a `__str__` method for `Neuron` object that outputs the model number and a short description from the ModelDB or README file of the model folder. 
