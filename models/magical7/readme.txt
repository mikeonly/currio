NEURON files from the paper:

Single neuron binding properties and the magical number 7,
by M. Migliore, G. Novara, D. Tegolo, Hippocampus, in press (2008).

In an extensive series of simulations with realistic morphologies and active properties, 
we demonstrate how n radial (oblique) dendrites of these neurons may be used to bind n inputs 
to generate an output signal. 
The results suggest a possible neural code as the most effective n-ple of dendrites that 
can be used for short-term memory recollection of persons, objects, or places. 
Our analysis predicts a straightforward physiological explanation for the observed 
puzzling limit of about 7 short-term memory items that can be stored by humans.

The hoc file reproduces the results in Fig.2
Face.exe is an interactive simplified demo of the simulations described in
the paper.

To use the demo, run face.exe.

Use the cursors to select any combination of eyes, nose, and mouth.
"Save Code" to save the configuration, and "Run Simulation" to run the
simulation.

Use again the cursors to test a different configuration then "Save
Code", and click on the "runm - refresh" button on the NEURON panel to
run a simulation with the new configuration of eyes, nose and mouth.

Any configuration will activate the same 3 obliques at t=100ms, 
but with different synaptic weights (stored in sinapsi_weights.txt). 
Only the configuration activating three yellow asterisks below the face
will generate a somatic AP. 

Running the 2ap-distr-c62564AP.hoc will result in a simulation
using the synaptic weights in sinapsi_weights.txt.

Questions on how to use this model
should be directed to michele.migliore@pa.ibf.cnr.it
