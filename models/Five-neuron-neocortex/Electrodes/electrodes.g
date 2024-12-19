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


// according to Hugo Cornelis, now supported by hines solver (9/12/2006)


//include defaults
//include Gran_layer_const.g

echo making electrodes

// the constants

   int nx = 1 // 10 // 9 // 3 // 1   // number of electrodes along X-axis
   int ny = 1 // 10 // 9 // 3 // 1   // number of electrodes along Y-axis
   int number_electrodes = {nx * ny}
   float dx = 50e-6 // 0  // interelectrode spacing
   float dy = 50e-6 // 0 
   float ox = 20e-6 // 9e-6 // 0 // -225e-6 // -50e-6 // 20e-6 // 0 
   float oy = 20e-6 // 2.3e-5 // 0 // -225e-6 // -50e-6 // 20e-6 // 0

   int number_contact_points = 11 // 1 // 11
   float contact_separation = 0.15e-3 // 0.6e-3
   float depth = -0.5e-3 // 0 // -0.5e-3 // -1e-3 // vertical position electrode tip (on z-axis)

   int i //  j, index

// the make function


// make 1 prototype electrode

function make_electrode_shaft (number_contact_points, contact_separation, depth)

   int number_contacts_points, i
   float contact_separation, depth

   create efield /library/contact
   setfield ^ scale -1e-3

//   possibility to low-pass-filter the electrode signal, so that it
//   can be sampled at a lower clock rate

   create RC /library/contact/RC 
   setfield ^ V0 0 R 1 C 0.005  // should give same amplitude as input,
                                //  but low-pass-filtered with tau 1 ms

   addmsg /library/contact /library/contact/RC INJECT field

   if(!{exists /library/electrode})
          create neutral /library/electrode 
   end

   createmap /library/contact  /library/electrode 1 {number_contact_points} \ 
                        -delta 0 {contact_separation} -origin 0 {depth}

   for (i = 0; {i < number_contact_points}; i = i + 1)
       setfield /library/electrode/contact[{i}] z {getfield /library/electrode/contact[{i}] y}
       setfield /library/electrode/contact[{i}] y 0
   end
 
end



// make array of electrodes

function make_electrode_array  (number_contact_points, contact_separation, depth, nx, ny, dx, dy, ox, oy)

   int   length, number_contact_points
   float depth, contact_separation 

   int   nx, ny // n = number
   float dx, dy, ox, oy // d = delta, o = origin

   if(!{exists /library})
          create neutral /library 
          disable /library
   end

   make_electrode_shaft {number_contact_points} {contact_separation} {depth}

   createmap /library/electrode /electrode_array  {nx} {ny} -delta {dx} {dy} -origin {ox} {oy}

end


// make the array

   create neutral /electrode_array
   make_electrode_array {number_contact_points} {contact_separation} {depth} {nx} {ny} {dx} {dy} {ox} {oy}


// connect all electrodes to all compartments of the PC

echo making msgs to electrodes

   float el_x, el_y, el_z  // (x,y,z) coordinates of electrode
   float cp_x, cp_y, cp_z  // (x,y,z) coordinates of compartment
   float distance          // distance between electrode and compartment
   str name, name2, elem

   foreach name ({el /L5P/##[][TYPE=compartment]})

//      echo {name}
      cp_x = {getfield {name} x}
      cp_y = {getfield {name} y}
      cp_z = {getfield {name} z}

      foreach name2 ({el /electrode_array/##[][TYPE=efield]})

//      for (i = 0; i < {nx}; i = i + 1)
//      for (j = 0; j < {ny}; j = j + 1)
//          index = {i * nx + j}
//          echo {getfield /electrode[{index}] x}
//          el_x = {getfield /electrode[{index}] x}
//          el_y = {getfield /electrode[{index}] y}
//          el_z = {getfield /electrode[{index}] z}

          el_x = {getfield {name2} x}
          el_y = {getfield {name2} y}
          el_z = {getfield {name2} z}

          distance = {sqrt {{pow {{cp_x} - {el_x}} 2.0} + \
                           {pow {{cp_y} - {el_y}} 2.0} + \
                           {pow {{cp_z} - {el_z}} 2.0}}}
//          echo {distance}

//          elem = ({findsolvefield {name}/../solve {name} Im})

//          echo {elem}

//          addmsg {name}/../solve  /electrode[{index}] CURRENT {elem} {distance}
 
          addmsg {name} {name2} CURRENT Im {distance}
 
//      end
      end
   end



// connect the electrodes to an asc_file element

   str electrodes_ascii_filename   // =  "electrodes" @ ".ascii"
   str name2, pathname

   for (i = 0; i < {number_electrodes}; i = i + 1)
 
      pathname = "/output/electrode" @ {i}
      electrodes_ascii_filename   =  "electrode" @ {i} @ {label} @ ".ascii"

      if (!({exists {pathname}}))
            create asc_file {pathname}
      end
//   setclock 7 20e-5
      useclock {pathname} 1
      enable /output
      enable {pathname}
      setfield {pathname} filename {electrodes_ascii_filename} \ 
               initialize 1 leave_open 1  flush 1
      echo Output to {electrodes_ascii_filename}

      foreach name2 ({el /electrode_array/electrode[{i}]/##[][TYPE=efield]})

          addmsg {name2} {pathname} SAVE field
//          addmsg {name2}/RC  /output/electrodes SAVE state
      end

end


// this reset is needed to activate the connections to the asc_file object ? 

//   reset















