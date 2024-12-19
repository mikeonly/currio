// genesis (R.M. 12/12/95)

// Copied from Parallel_fiber.g on 29/12//2001
// Intended to model a 2D array of electrodes

// IMPORTANT
// Because the efield object is not yet supported by the hines solver,
// the elctrodes must be made, and connected, after the hines solver 
// has been installed for the compartments to which the electrodes 
// are to be connected.
// For this reason, the constants, makearray and setup of messages are
// collapsed in this single script.


include defaults
include Gran_layer_const.g



// the constants

   int nx = 1   // number of electrodes along X-axis
   int ny = 1   // number of electrodes along Y-axis
   float dx = 0  // interelectrode spacing
   float dy = 0 
   float ox = {({number_Golgi_cells} - 1) / 2.0} * {Golgi_cell_separation}
   float oy = 0.000300

   int i, j, index

// the make function

function make_electrode_array  (nx, ny, dx, dy, ox, oy)

   int   nx, ny // n = number
   float dx, dy, ox, oy // d = delta, o = origin


   if(!{exists /library})
          create neutral /library 
          disable /library
   end


   create efield /library/electrode
   setfield ^ scale 1e-3


   possibility to low-pass-filter the electrode signal, so that it
   can be sampled at a lower clock rate

   create RC /library/electrode/RC 
   setfield ^ V0 0 R 1 C 0.001  // should give same amplitude as input,
                                //  but low-pass-filtered with tau 1 ms

   addmsg /library/electrode /library/electrode/RC INJECT field



   createmap /library/electrode /  {nx} {ny} -delta {dx} {dy} -origin {ox} {oy}

end


// make the array

   make_electrode_array {nx} {ny} {dx} {dy} {ox} {oy}


// connect the electrodes to an asc_file element

   str electrodes_ascii_filename   =  {filename} @ "electrodes_" @ {label} @ ".ascii"

   if (!({exists /output/electrodes}))
          create asc_file /output/electrodes
   end
   setclock 7 20e-5
   useclock /output/electrodes 7
   enable /output
   enable /output/electrodes
   setfield /output/electrodes filename {electrodes_ascii_filename} \ 
           initialize 1 leave_open 1  flush 1
   echo Output to {filename}

   for (i = 0; i < {nx}; i = i + 1)
   for (j = 0; j < {ny}; j = j + 1)
          index = {i * nx + j}
          addmsg /electrode[{index}]/RC /output/electrodes SAVE field
   end
   end

// this reset is needed to activate the connections to the asc_file object ? 

   reset



// connect all electrodes to all compartments of all Golgi cells

   float el_x, el_y, el_z  // (x,y,z) coordinates of electrode
   float cp_x, cp_y, cp_z  // (x,y,z) coordinates of compartment
   float distance          // distance between electrode and compartment
   str name, elem

   foreach name ({el /granule_cell_layer/##[][TYPE=compartment]})

      echo {name}
      cp_x = {getfield {name} x}
      cp_y = {getfield {name} y}
      cp_z = {getfield {name} z}

      for (i = 0; i < {nx}; i = i + 1)
      for (j = 0; j < {ny}; j = j + 1)
          index = {i * nx + j}
          echo {getfield /electrode[{index}] x}
          el_x = {getfield /electrode[{index}] x}
          el_y = {getfield /electrode[{index}] y}
          el_z = {getfield /electrode[{index}] z}

          distance = {sqrt {{pow {{cp_x} - {el_x}} 2.0} + \
                           {pow {{cp_y} - {el_y}} 2.0} + \
                           {pow {{cp_z} - {el_z}} 2.0}}}
          echo {distance}

          elem = ({findsolvefield {name}/../solve {name} Im})

          echo {elem}

          addmsg {name}/../solve  /electrode[{index}] CURRENT {elem} {distance}
 
      end
      end
   end















