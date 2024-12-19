//genesis script for running the layer-5 pyramidal cell

float dt = 25e-6 // 10e-6 // 2.5e-6 // 0.05e-6 // 2.5e-6
str label = "fixbug" // "try"
str filename = "./" 

setclock 0 {dt} // the integration time step
setclock 1 50e-6 // the sampling step for LFPs
float tmax = 0.15
str name

include defaults.g



//Make prototype channels and compartments in library
include L5P_const+axon+syn.g

        if (!({exists /library }))
               create neutral /library
        end
        disable /library
        pushe library

include L5P_chans_tab.g
include L5P_synchan.g
include L5P_comps+axon+syn.g

pope



//Set up multicompartmental model in Hines solver mode based on reconstructed morphology
readcell DS1_141099_rot2_sc_defmesh_axon.p /L5P // -hsolve

//rotcoord /L5P {-3.1415927/2} -x  // does not work : gives segmentation violation
// the following trick works

      foreach name ({el /L5P/##[][TYPE=compartment]})
	rotcoord {name} {3.1415927/2} -x -fixkids
      end
      foreach name ({el /L5P/##[]/##[]})
	rotcoord {name} {3.1415927/2} -x  -fixkids 
      end



//Set up differential distributions of Rm and h-channels
include DiffRm.g
include Hgradient.g

DiffRm /L5P 4.0 0.27 500e-6 50e-6
Hgradient /L5P H 0.15 6.0 500e-6 50e-6



//Set up graphical and ascii output for L5P cell
include L5P_graph.g
include L5P_ascout.g

// include electrodes.g
include electrodes_fixbug.g


ce /L5P


// setup the hines solver

echo preparing hines solver...
create hsolve solve
ce solve
// if this is set then reset will NOT change Vm in Hines
 setfield . path "../##[][TYPE=compartment]" comptmode 1 chanmode 5 // 4 // 5 // 3 
call . SETUP


reset
randseed 54321 // 12345



// generate for each compartment as associated fibre
include Excitatory_fibres
include Inhibitory_fibres

include L5P_history.g

include nsynapses

include Firing_rate_profile.g

make_firing_rate_profile  /Excitatory_fibres/FF  0.0008  0.0002 2 -0.0001 0.0001 1 10 

make_firing_rate_profile  /Excitatory_fibres/FBintra  0.001  0.0002 2 -0.0001 0.0001 1 10 

make_firing_rate_profile  /Inhibitory_fibres/FF  0.0008  0.0004 1 -0.000 0.0004 2 40 

make_firing_rate_profile  /Inhibitory_fibres/FBintra  0.001  0.0004 1 -0.000 0.0002 2 40 

include Harsch-Robinson_modulation.g

Harsch_Robinson_modulation 30 0.1 

include Firing_rate_modulation.g



randseed 12345

reset

// current injection
// setfield /L5P/soma inject 20e-12 // 800e-12

step 0.1 -t

//quit


