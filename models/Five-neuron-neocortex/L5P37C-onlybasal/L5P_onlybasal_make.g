//genesis


// This is a version of the modified  L5P model for use in a network.
// The modifications imply cuttung all but the basal dendrite,
// and using ion channels from a previous cerebellar model,
// in order to produce narrow spikes.
// It only creates the cells.



include defaults.g


//Make prototype channels and compartments in library
include ../L5P37C-onlybasal/L5P_const+axon+syn.g

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

include ../L5P37C-onlybasal/L5P_synchan.g
include ../Granule_cell/Gran_const.g 

//include ../Granule_cell/Gran_comp_soma_dend_axon.g
//made new comps file in present dir
include ../L5P37C-onlybasal/Gran_comp_soma_dend_axon.g


//include L5P_chans.g
//include L5P_chans_tab.g
//include L5P_comps.g
//include L5P_comps+axon.g
//include L5P_comps+axon+syn.g


include DiffRm.g



// Make the prototypes of channels and compartments that can be invoked in .p files
   	make_Granule_chans
//   make_Granule_syns
   	make_Granule_comps_soma_dend_axon

	pope



function create_L5Ponlybasal (pathname, px, py, pz)

	str pathname
	float px, py, pz   // the position

        echo {pathname}
        echo  px = {px}, py = {py}, pz = {pz}

//Set up multicompartmental model in Hines solver mode based on reconstructed morphology

	readcell ../L5P37C-onlybasal/DS1_141099_rot2_sc_defmesh_axon_onlybasal.p {pathname} // -hsolve

	setfield {pathname}/soma/InNa Gbar {{getfield {pathname}/soma/InNa Gbar} * 5}
	setfield {pathname}/soma/KDr Gbar {{getfield {pathname}/soma/KDr Gbar} * 5}


// rotcoord /L5P {-3.1415927/2} -x  // does not work : gives segmentation violation
// the following trick works

      	foreach name ({el {pathname}/##[][TYPE=compartment]})
//        echo {name}
		rotcoord {name} {3.1415927/2} -x -fixkids
      	end
      	foreach name ({el {pathname}/##[]/##[]})
//        echo {name}
		rotcoord {name} {3.1415927/2} -x  -fixkids 
      	end

      	foreach name ({el {pathname}/##[][TYPE=compartment]})
//        echo {name}
		rotcoord {name} {3.1415927/2} -y -fixkids
      	end
      	foreach name ({el {pathname}/##[]/##[]})
//        echo {name}
		rotcoord {name} {3.1415927/2} -y  -fixkids 
      	end


//	position {pathname}  {px} {py} {pz}

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
//include DiffRm.g
//include Hgradient.g

	DiffRm {pathname} 4.0 0.27 500e-6 50e-6
//Hgradient {pathname} H 0.15 6.0 500e-6 50e-6

end


// because there is a bug with the graph window when plotting with hines solver
/*
name = {findsolvefield /L5P/solve /L5P/soma Vm}
addmsg /L5P/solve /data1/DS1_141099 PLOT {name} *Soma_Vm *red

name = {findsolvefield /L5P/solve  /L5P/axon[19] Vm}
addmsg /L5P/solve /data1/DS1_141099 PLOT {name} *Axon_Vm *blue

name = {findsolvefield /L5P/solve /L5P/p6b2b2[15] Vm}
addmsg /L5P/solve /data1/DS1_141099 PLOT {name} *Dend_Vm *black 
*/


