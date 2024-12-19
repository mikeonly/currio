//genesis


// This is a version of the modified L5P model intended for use in a network.
// It only creates the L5P neuron, without any further processing,
// input or output.

// The modifications imply cuttung the tuft and preventing backpropagation of the action potential.




include defaults.g

str name

//Make prototype channels and compartments in library
include ../L5P37C-notuft/L5P_const+axon+syn.g

        if (!({exists /library }))
               create neutral /library
        end
        disable /library
        pushe library

//include L5P_chans.g
include ../L5P37C-notuft/L5P_chans_tab.g

include ../L5P37C-notuft/L5P_synchan.g

//include L5P_comps.g
//include L5P_comps+axon.g
include ../L5P37C-notuft/L5P_comps+axon+syn.g

pope

include ../L5P37C-notuft/DiffRm.g
include ../L5P37C-notuft/Hgradient.g



function create_L5Pnotuft (pathname, px, py, pz)

	str pathname
	float px, py, pz   // the position

        echo {pathname}
        echo  px = {px}, py = {py}, pz = {pz}


//Set up multicompartmental model in Hines solver mode based on reconstructed morphology
//and rotate axes

	readcell ../L5P37C-notuft/DS1_141099_rot2_sc_defmesh_axon_notuft.p {pathname} // -hsolve

//rotcoord /L5P {-3.1415927/2} -x  // does not work : gives segmentation violation
// the following trick works

      	foreach name ({el {pathname}/##[][TYPE=compartment]})
//      	  echo {name}
		rotcoord {name} {3.1415927/2} -x -fixkids
      	end

      	foreach name ({el {pathname}/##[]/##[]})
//        	echo {name}
		rotcoord {name} {3.1415927/2} -x  -fixkids 
      	end



	setfield {pathname}/axon[]/InNa Gbar {{getfield {pathname}/axon[0]/InNa Gbar} * 2}
	setfield {pathname}/axon[]/KDr  Gbar {{getfield {pathname}/axon[0]/KDr Gbar} * 2}

	setfield {pathname}/soma/NaF Gbar {{getfield {pathname}/soma/NaF Gbar} * 2}
	setfield {pathname}/soma/KDr Gbar {{getfield {pathname}/soma/KDr Gbar} * 10}



        setfield {pathname} 	x {{getfield {pathname} x} + {px}} \ 
				y {{getfield {pathname} y} + {py}} \
				z {{getfield {pathname} z} + {pz}}

      	foreach name ({el {pathname}/#[]/#})
//        echo {name}
		setfield {name} x {{getfield {name} x} + {px}} \ 
				y {{getfield {name} y} + {py}} \
				z {{getfield {name} z} + {pz}}
      	end

      	foreach name ({el {pathname}/#[]})
//        echo {name}
		setfield {name} x {{getfield {name} x} + {px}} \ 
				y {{getfield {name} y} + {py}} \
				z {{getfield {name} z} + {pz}}
      	end



//Set up differential distributions of Rm and h-channels
//include ../L5P37C-notuft/DiffRm.g
//include ../L5P37C-notuft/Hgradient.g

	DiffRm {pathname} 4.0 0.27 500e-6 50e-6
	Hgradient {pathname} H 0.15 6.0 500e-6 50e-6


end

/*
// This is moved to ../Network/Network_make.g

/*

ce /L5P


// setup the hines solver

echo preparing hines solver...
	create hsolve solve
	ce solve
// if this is set then reset will NOT change Vm in Hines
 	setfield . path "../##[][TYPE=compartment]" comptmode 1 chanmode 5 // 4 // 5 // 3 
//setfield . path "../##[][TYPE=compartment]" comptmode 1 chanmode 1 computeIm 1 // 5 // 4 // 5 // 3   
	call . SETUP
*/

/*
// because there is a bug with the graph window when plotting with hines solver

name = {findsolvefield /L5P/solve /L5P/soma Vm}
addmsg /L5P/solve /data1/DS1_141099 PLOT {name} *Soma_Vm *red

name = {findsolvefield /L5P/solve  /L5P/axon[19] Vm}
addmsg /L5P/solve /data1/DS1_141099 PLOT {name} *Axon_Vm *blue

name = {findsolvefield /L5P/solve /L5P/p0b1b2b1b1b1b2b1b2b1b2b1b2b1b1b1b2b1b2b1b2b1b2b1b2b1b2b1b1[8] Vm}
addmsg /L5P/solve /data1/DS1_141099 PLOT {name} *Dend_Vm *black 
*/




