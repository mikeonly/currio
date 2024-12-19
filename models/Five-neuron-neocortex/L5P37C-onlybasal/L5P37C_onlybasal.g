//genesis

float dt = 10e-6 
str label = "basalonly" // "notuft" // "fixbug" // 'try'


   str filename = "./" // "/cluster/scratch/local/reinoud/"

setclock 0 {dt} 
setclock 1 50e-6 
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



// We borrow channels from cerebellar granule/Golgi cell, hoping to
// produce a cell with narrower action potentials

if (! {exists /library/granule})
    create neutral /library/granule
end
ce /library/granule

include ../Granule_cell/Gran_const.g 
include ../Granule_cell/Gran_chan_tab.g
//include ../Granule_cell/Gran_synchan.g


include L5P_synchan.g
include ../Granule_cell/Gran_const.g 

include Gran_comp_soma_dend_axon.g


   if (! {exists /library/granule})
      create neutral /library/granule
   end
   ce /library/granule

// Make the prototypes of channels and compartments that can be invoked in .p files
   make_Granule_chans
//   make_Granule_syns
   make_Granule_comps_soma_dend_axon

pope



//Set up multicompartmental model in Hines solver mode based on reconstructed morphology
readcell DS1_141099_rot2_sc_defmesh_axon_onlybasal.p /L5P // -hsolve


//rotcoord /L5P {-3.1415927/2} -x  // does not work : gives segmentation violation
// the following trick works

      foreach name ({el /L5P/##[][TYPE=compartment]})
	rotcoord {name} {3.1415927/2} -x -fixkids
      end

      foreach name ({el /L5P/##[]/##[]})
	rotcoord {name} {3.1415927/2} -x  -fixkids 
      end

      foreach name ({el /L5P/##[][TYPE=compartment]})
	rotcoord {name} {3.1415927/2} -y -fixkids
      end

      foreach name ({el /L5P/##[]/##[]})
	rotcoord {name} {3.1415927/2} -y  -fixkids 
      end


setfield /L5P/soma/InNa Gbar {{getfield /L5P/soma/InNa Gbar} * 10}
setfield /L5P/soma/KDr Gbar {{getfield L5P/soma/KDr Gbar} * 10}


//Set up differential distributions of Rm and h-channels
include DiffRm.g
include Hgradient.g

DiffRm /L5P 4.0 0.27 500e-6 50e-6
Hgradient /L5P H 0.15 6.0 500e-6 50e-6



//Set up graphical and ascii output
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

setmethod 11

reset


randseed 54321 // 12345


// generate for each compartment as associated fibre
include Excitatory_fibres
include Inhibitory_fibres


//include nsynapses

include Firing_rate_profile.g

make_firing_rate_profile  /Excitatory_fibres/FF  0.0008  0.0002 2 -0.0001 0.0001 1 10 

make_firing_rate_profile  /Excitatory_fibres/FBintra  0.001  0.0002 2 -0.0001 0.0001 1 10 

make_firing_rate_profile  /Inhibitory_fibres/FF  0.0008  0.0004 1 -0.000 0.0004 2 45 

make_firing_rate_profile  /Inhibitory_fibres/FBintra  0.001  0.0004 1 -0.000 0.0002 2 45 

include Harsch-Robinson_modulation.g

Harsch_Robinson_modulation 30 0.1 


include Firing_rate_modulation.g


include L5P_history.g


randseed 12345

// current injection

//setfield /L5P/soma inject 540e-12 // 400e-12 // 800e-12 // 1200e-12  // 1600e-12 // 800e-12



// because there is a bug with the graph window when plotting with hines solver
/*
name = {findsolvefield /L5P/solve /L5P/soma Vm}
addmsg /L5P/solve /data1/DS1_141099 PLOT {name} *Soma_Vm *red

name = {findsolvefield /L5P/solve  /L5P/axon[19] Vm}
addmsg /L5P/solve /data1/DS1_141099 PLOT {name} *Axon_Vm *blue

name = {findsolvefield /L5P/solve /L5P/p6b2b2[15] Vm}
addmsg /L5P/solve /data1/DS1_141099 PLOT {name} *Dend_Vm *black 
*/
reset

 step 0.1 -t

//quit


