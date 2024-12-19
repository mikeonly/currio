//genesis

// This is the main script for setting up and running a network.


	float dt = 10e-6 
	str label = "IMTEK" 
   	str filename = "./" 

	setclock 0 {dt} 
	setclock 1 50e-6 
	float tmax = 0.15
	str name

include defaults.g



// making the neurons

/*  Make L5P pyramidal cell   */
include ../L5P37C/L5P_make.g
create_L5P /L5P 0 0 0 

/*  Make L5P pyramidal cell without tuft or backpropagating spike */
include ../L5P37C-notuft/L5P_notuft_make.g
create_L5Pnotuft /L5Pnotuft -0.00004 0 0.0002 

/*  Make neuron with narrow spikes  */
include ../L5P37C-onlybasal/L5P_onlybasal_make.g
create_L5Ponlybasal /L5Ponlybasal 0.00004 0 0.0001 

/* Make additional inhibitory neuron */
create_L5Ponlybasal /L5Ponlybasal2 -20e-6 -30e-6 0.0003 

/* Make additional excitatory neuron */
create_L5Pnotuft /L5Pnotuft2 20e-6  30e-6 0.0003 

cd ../Network_5neuron_IMTEK



/* Set up graphical and ascii output */

include ../Output/L5P_view.g
	add_xcell /L5P
	add_xcell /L5Ponlybasal
	add_xcell /L5Pnotuft
	add_xcell /L5Ponlybasal2
	add_xcell /L5Pnotuft2

//include ../Output/L5P_graph.g
//        add_xgraph /L5P
//	add_xgraph /L5Ponlybasal
//	add_xgraph /L5Pnotuft
//	add_xgraph /L5Ponlybasal2
//	add_xgraph /L5Pnotuft2


include ../Output/L5P_ascout.g
	add_ascout /L5P
	add_ascout /L5Ponlybasal
	add_ascout /L5Pnotuft
	add_ascout /L5Ponlybasal2
	add_ascout /L5Pnotuft2


/* Set up electrode arrays  */ 

include ../Electrodes/electrodesIMTEK_make.g
include ../Electrodes/electrodes_connect.g
//	connect_to_electrodes L5P
//	connect_to_electrodes L5Ponlybasal
//	connect_to_electrodes L5Pnotuft

//	connect_to_electrodes L5Ponlybasal2
//	connect_to_electrodes L5Pnotuft2

useclock   /electrode_array    1
useclock   /electrode_array/##[]    1


/* Setup the hines solvers  */
include Network_hsolve.g

	make_hsolve /L5P
	make_hsolve /L5Ponlybasal
	make_hsolve /L5Pnotuft

	make_hsolve /L5Ponlybasal2
	make_hsolve /L5Pnotuft2

include ../Output/L5P_graphsolve.g
        add_xgraph /L5P
	add_xgraph /L5Ponlybasal
	add_xgraph /L5Pnotuft
	add_xgraph /L5Ponlybasal2
	add_xgraph /L5Pnotuft2
	

/* generate for each compartment of L5P an associated fibre  */

	randseed 54321 // 12345


// make the fibres using L5P as template neuron
include ../Fibres/Fibres_make

	make_fibres /Excitatory_fibres /L5P/p# 
	make_fibres /Inhibitory_fibres /L5P/p#


// connect the fibres to the neurons
include ../Fibres/Fibres_connect

	connect_horizontally 	/Excitatory_fibres/FF/fibre[] \
				/L5P/p#[][TYPE=compartment]/AMPA \
				0.05 {weight_AMPA_synapse * 0.5} 0

	connect_horizontally 	/Excitatory_fibres/FBintra/fibre[] \
				/L5P/p#[][TYPE=compartment]/AMPA \
				0.05 {weight_AMPA_synapse * 0.5} 0.02

	connect_horizontally 	/Inhibitory_fibres/FF/fibre[] \
				/L5P/p#[][TYPE=compartment]/GABA \
				0.025 {weight_GABA_synapse * 0.25} 0.002

	connect_horizontally 	/Inhibitory_fibres/FBintra/fibre[] \
				/L5P/p#[][TYPE=compartment]/GABA \
				0.025 {weight_GABA_synapse * 0.25} 0.033 // 0.025


	connect_horizontally 	/Excitatory_fibres/FF/fibre[] \
				/L5Ponlybasal/p#[][TYPE=compartment]/AMPA \
				0.1 {weight_AMPA_synapse * 0.15} 0

	connect_horizontally 	/Excitatory_fibres/FBintra/fibre[] \
				/L5Ponlybasal/p#[][TYPE=compartment]/AMPA \
				0.1 {weight_AMPA_synapse * 0.10} 0.02

	connect_horizontally 	/Inhibitory_fibres/FF/fibre[] \
				/L5Ponlybasal/p#[][TYPE=compartment]/GABA \
				0.025 {weight_GABA_synapse * 0.7} 0.002

	connect_horizontally 	/Inhibitory_fibres/FBintra/fibre[] \
				/L5Ponlybasal/p#[][TYPE=compartment]/GABA \
				0.025 {weight_GABA_synapse * 0.7} 0.033


	connect_horizontally 	/Excitatory_fibres/FF/fibre[] \
				/L5Pnotuft/p#[][TYPE=compartment]/AMPA \
				0.05 {weight_AMPA_synapse * 0.8} 0

	connect_horizontally 	/Excitatory_fibres/FBintra/fibre[] \
				/L5Pnotuft/p#[][TYPE=compartment]/AMPA \
				0.05 {weight_AMPA_synapse * 0.8} 0.02

	connect_horizontally 	/Inhibitory_fibres/FF/fibre[] \
				/L5Pnotuft/p#[][TYPE=compartment]/GABA \
				0.02 {weight_GABA_synapse * 0.4} 0.002

	connect_horizontally 	/Inhibitory_fibres/FBintra/fibre[] \
				/L5Pnotuft/p#[][TYPE=compartment]/GABA \
				0.02 {weight_GABA_synapse * 0.4} 0.033


// I keep the same connections for new neurons 4 and 5
// and do not include them in feedback

	connect_horizontally 	/Excitatory_fibres/FF/fibre[] \
				/L5Ponlybasal2/p#[][TYPE=compartment]/AMPA \
				0.4 {weight_AMPA_synapse * 0.15} 0

	connect_horizontally 	/Excitatory_fibres/FBintra/fibre[] \
				/L5Ponlybasal2/p#[][TYPE=compartment]/AMPA \
				0.1 {weight_AMPA_synapse * 0.10} 0.02

	connect_horizontally 	/Inhibitory_fibres/FF/fibre[] \
				/L5Ponlybasal2/p#[][TYPE=compartment]/GABA \
				0.025 {weight_GABA_synapse * 0.7} 0.002

	connect_horizontally 	/Inhibitory_fibres/FBintra/fibre[] \
				/L5Ponlybasal2/p#[][TYPE=compartment]/GABA \
				0.025 {weight_GABA_synapse * 0.7} 0.033


	connect_horizontally 	/Excitatory_fibres/FF/fibre[] \
				/L5Pnotuft2/p#[][TYPE=compartment]/AMPA \
				0.05 {weight_AMPA_synapse * 0.8} 0

	connect_horizontally 	/Excitatory_fibres/FBintra/fibre[] \
				/L5Pnotuft2/p#[][TYPE=compartment]/AMPA \
				0.05 {weight_AMPA_synapse * 0.8} 0.02

	connect_horizontally 	/Inhibitory_fibres/FF/fibre[] \
				/L5Pnotuft2/p#[][TYPE=compartment]/GABA \
				0.02 {weight_GABA_synapse * 0.4} 0.002

	connect_horizontally 	/Inhibitory_fibres/FBintra/fibre[] \
				/L5Pnotuft2/p#[][TYPE=compartment]/GABA \
				0.02 {weight_GABA_synapse * 0.4} 0.033



include ../Output/L5P_history.g
	add_history  /L5P
	add_history  /L5Ponlybasal
	add_history  /L5Pnotuft

	add_history  /L5Ponlybasal2
	add_history  /L5Pnotuft2


include nsynapses

include ../Fibres/Firing_rate_profile.g

// This gives different weights to the afferent fibres according to their depth (layer) in neocortex

	make_firing_rate_profile  /Excitatory_fibres/FF  0.0008  0.0002 2 0 0.0004 1 10 

	make_firing_rate_profile  /Excitatory_fibres/FBintra  0.001  0.0002 2 0 0.0004 1 10 

	make_firing_rate_profile  /Inhibitory_fibres/FF  0.0008  0.0004 1 0 0.0002 2 45 

	make_firing_rate_profile  /Inhibitory_fibres/FBintra  0.001  0.0004 1 0 0.0002 2 45 


include ../Fibres/Harsch-Robinson_modulation.g

// This gives a temporal profile to the spike rate of the subcortical afferent fibres
	Harsch_Robinson_modulation 30 0.1 


// This gives a temporal profile to the intracortical fibers

include ../Fibres/Firing_rate_modulation.g

resched 


randseed 12345

// current injection

//setfield /L5P/soma inject 20e-12 // 800e-12
reset


// just a check, recording electrode positions
include ../Electrodes/electrode-positions.g

// step 25 -t

//quit


