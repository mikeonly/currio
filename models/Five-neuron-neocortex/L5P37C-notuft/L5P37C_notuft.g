//genesis

float dt = 25e-6 // 10e-6 // 2.5e-6 // 0.05e-6 // 2.5e-6
str label = "notuft" // "fixbug" // "try"
   str filename = "./" // "/cluster/scratch/local/reinoud/"
//str label = "chanmode1"

setclock 0 {dt} // the numerical integration step
setclock 1 50e-6 // the LFP sampling step
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
readcell DS1_141099_rot2_sc_defmesh_axon_notuft.p /L5P // -hsolve

//rotcoord /L5P {-3.1415927/2} -x  // does not work : gives segmentation violation
// the following trick works

      foreach name ({el /L5P/##[][TYPE=compartment]})
	rotcoord {name} {3.1415927/2} -x -fixkids
      end
      foreach name ({el /L5P/##[]/##[]})
	rotcoord {name} {3.1415927/2} -x  -fixkids 
      end


setfield /L5P/axon[0-9]/InNa Gbar {{getfield /L5P/axon[0]/InNa Gbar} * 1.2}
setfield /L5P/axon[0-19]/KDr Gbar {{getfield L5P/axon[0]/KDr Gbar} * 3}

setfield /L5P/soma/NaF Gbar {{getfield L5P/soma/NaF Gbar} * 1.2}
setfield /L5P/soma/KDr Gbar {{getfield L5P/soma/KDr Gbar} * 10}


//Set up differential distributions of Rm and h-channels
include DiffRm.g
include Hgradient.g

DiffRm /L5P 4.0 0.27 500e-6 50e-6
Hgradient /L5P H 0.15 6.0 500e-6 50e-6



//Set up graphical and ascii output
include L5P_graph.g
include L5P_ascout.g

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

include nsynapses

include L5P_history.g

include Firing_rate_profile.g

make_firing_rate_profile  /Excitatory_fibres/FF  0.0008  0.0002 2 -0.0001 0.0001 1 10 
make_firing_rate_profile  /Excitatory_fibres/FBintra  0.001  0.0002 2 -0.0001 0.0001 1 10 
make_firing_rate_profile  /Inhibitory_fibres/FF  0.0008  0.0004 1 -0.000 0.0004 2 45 
make_firing_rate_profile  /Inhibitory_fibres/FBintra  0.001  0.0004 1 -0.000 0.0002 2 40 

include Harsch-Robinson_modulation.g

Harsch_Robinson_modulation 30 0.1 // 10 0.1 // 0.05


include Firing_rate_modulation.g



randseed 12345

// current injection

//setfield /L5P/soma inject 20e-12 // 800e-12



// because there is a bug with the graph window when plotting with hines solver

 name = {findsolvefield /L5P/solve /L5P/soma Vm}
 addmsg /L5P/solve /data1/DS1_141099 PLOT {name} *Soma_Vm *red

 name = {findsolvefield /L5P/solve  /L5P/axon[19] Vm}
 addmsg /L5P/solve /data1/DS1_141099 PLOT {name} *Axon_Vm *blue

 name = {findsolvefield /L5P/solve /L5P/p0b1b2b1b1b1b2b1b2b1b2b1b2b1b1b1b2b1b2b1b2b1b2b1b2b1b2b1b1[8] Vm}
 addmsg /L5P/solve /data1/DS1_141099 PLOT {name} *Dend_Vm *black 

reset

 step 0.1 -t

//quit