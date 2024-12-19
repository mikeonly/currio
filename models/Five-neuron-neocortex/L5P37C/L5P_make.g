//genesis


// This is a version of the L5P model intended for use in a network.
// It only creates the L5P neuron, without any further processing,
// input or output.


str name

include defaults.g


        if (!({exists /library }))
               create neutral /library
        end
        disable /library
        pushe library


//Make prototype channels and compartments in library

include ../L5P37C/L5P_const+axon+syn.g

//include L5P_chans.g
include ../L5P37C/L5P_chans_tab.g

include ../L5P37C/L5P_synchan.g

//include L5P_comps.g
//include L5P_comps+axon.g
include ../L5P37C/L5P_comps+axon+syn.g

include ../L5P37C/DiffRm.g
include ../L5P37C/Hgradient.g

	pope


function create_L5P (pathname, px, py, pz)

	str pathname
	float px, py, pz   // the position

        echo {pathname}
        echo  px = {px}, py = {py}, pz = {pz}


//Set up multicompartmental model in Hines solver mode based on reconstructed morphology
//and rotate axes

	readcell ../L5P37C/DS1_141099_rot2_sc_defmesh_axon.p {pathname} // -hsolve

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


	setfield {pathname}/soma/NaF Gbar {{getfield {pathname}/soma/NaF Gbar} * 1}
	setfield {pathname}/soma/KDr Gbar {{getfield {pathname}/soma/KDr Gbar} * 1}


//	setfield {pathname}/axon[]/InNa Gbar {{getfield {pathname}/axon/InNa Gbar} * 0.5}
//	setfield {pathname}/axon[]/KDr Gbar {{getfield {pathname}/axon/KDr Gbar} * 0.5}


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
//include ../L5P37C/DiffRm.g
//include ../L5P37C/Hgradient.g

	DiffRm {pathname} 4.0 0.27 500e-6 50e-6
	Hgradient {pathname} H 0.15 6.0 500e-6 50e-6


end

/*
// This is moved to ../Network/Network_make.g

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



