//genesis (R.M. 13/12/95)

include defaults 

/* 
The function "make_Golgi_cell_array" creates {length} Golgi cells,
named /granule_cell_layer/Golgi_cell [0] 
   to /granule_cell_layer/Golgi_cell [{length} - 1].
Each Golgi cell is a copy of the Golgi cell described in Golg1M0.p.
A spikegen object is added to the soma.

*/


include ../Granule_cell/Gran_const.g 
include ../Granule_cell/Gran_chan_tab.g
include ../Granule_cell/Gran_synchan.g 
//include ../Golgi_cell/Golg_comp.g 
//include ../Granule_cell/Gran_comp_soma_dend.g
include ../Granule_cell/Gran_comp_soma_dend_axon.g
//include ../Golgi_cell/Golg_comp_passivedend.g

function make_Golgi_cell_array (length)

   int length
   int i
   str cellpath = "/Golgi"

   if (! {exists /library/granule})
      create neutral /library/granule
   end
   ce /library/granule

// Make the prototypes of channels and compartments that can be invoked in .p files
   make_Granule_chans
   make_Granule_syns
   make_Granule_comps_soma_dend_axon

   if (!{exists /granule_cell_layer})
          create neutral /granule_cell_layer
   end

// MAEX 16/4/96
   setfield /library/granule/soma/mf_AMPA normalize_weights 1
   setfield /library/granule/soma/pf_AMPA normalize_weights 1
   setfield /library/granule/soma/GABAA   normalize_weights 1
   setfield /library/granule/dend[]/mf_AMPA normalize_weights 1
   setfield /library/granule/dend[]/pf_AMPA normalize_weights 1
   setfield /library/granule/dend[]/GABAA   normalize_weights 1

   setfield /library/granule/soma/GABAA \
            tau1 {{getfield /library/granule/soma/GABAA  tau1}  / 3} \
            tau2 {{getfield /library/granule/soma/GABAA  tau2}  / 3} // 3} 
//            tau2 {{getfield /library/granule/soma/GABAA  tau2} * 4 / 3} 
//   setfield /library/granule/dend/GABAA \
//            tau1 {{getfield /library/granule/dend/GABAA  tau1} / 3} \
//            tau2 {{getfield /library/granule/dend/GABAA  tau2} / 3} // 3} 
// read cell data from .p file
   readcell ../Granule_cell/Gran1M0_dend3D.p {cellpath}

   setfield /Golgi/soma/InNa Gbar {{getfield /Golgi/soma/InNa Gbar} * 5.0}
   setfield /Golgi/soma/KDr  Gbar {{getfield /Golgi/soma/KDr  Gbar} * 5.0}

// add a spikegen object
   create spikegen {cellpath}/soma/spike
   setfield {cellpath}/soma/spike thresh -0.02 \
                                  abs_refract 0.001 \
                                  output_amp 1
   addmsg {cellpath}/soma {cellpath}/soma/spike INPUT Vm

// add a diffamp for gap junction
   create diffamp {cellpath}/diffamp


//   createmap {cellpath} /granule_cell_layer \
//             {length} 1 -delta {Golgi_cell_separation} 0.0 -origin 0.0 0.0

  
   createmap {cellpath} /granule_cell_layer \
             {length} {length} \ 
             -delta {Golgi_cell_separation} {Golgi_cell_separation * {sqrt {3}} * 0.5} \
             -origin 0.0 0.0

   for (i = 0; i < {length}; i = {i + 2})
   for (j = 0; j < {length}; j = {j + 1})
   position /granule_cell_layer/Golgi[{i*length + j}] \
      {{getfield /granule_cell_layer/Golgi[{i*length + j}] x} + {Golgi_cell_separation * 0.5}} \
      {getfield /granule_cell_layer/Golgi[{i*length + j}] y} \
      {getfield /granule_cell_layer/Golgi[{i*length + j}] z}
   end
   end

   disable {cellpath}


end   





