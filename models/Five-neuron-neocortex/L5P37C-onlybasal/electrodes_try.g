
int msgcount
int msgindex
int total_number_axial_msgs = 0
int diffamp_index = 0
str sender

// count how many diffamps are needed

   foreach name ({el /L5P/##[][TYPE=compartment]})
     msgcount = {getmsg {name} -incoming -count}
//     echo {msgcount}
     for (msgindex = 0; msgindex < {msgcount}; msgindex = {msgindex} + 1)
         if (! {strcmp {getmsg {name}  -in -type {msgindex}} "AXIAL"})
//            echo {name} {msgindex} AXIAL
            total_number_axial_msgs = {total_number_axial_msgs} + 1
         elif (! {strcmp {getmsg {name}  -in -type {msgindex}} "RAXIAL"})
//            echo {name} {msgindex} RAXIAL
            total_number_axial_msgs = {total_number_axial_msgs} + 1
         end
//           echo {getmsg {name} -in -type {msgindex}}
     end
   end

     echo total number of AXIAL and RAXIAL msgs is {total_number_axial_msgs}
          
// create the diffamp array

    create diffamp /diffamp
    createmap /diffamp /diffamp_array {total_number_axial_msgs} 1


// position each diffamp element to the corresponding compartment, and make msgs
    
   foreach name ({el /L5P/##[][TYPE=compartment]})
     msgcount = {getmsg {name} -incoming -count}
//     echo {msgcount}
     for (msgindex = 0; msgindex < {msgcount}; msgindex = {msgindex} + 1)

         if (! {strcmp {getmsg {name}  -in -type {msgindex}} "AXIAL"})
//            echo {name} {msgindex} AXIAL {diffamp_index}
            setfield /diffamp_array/diffamp[{diffamp_index}] x {getfield {name} x} \
                                                  y {getfield {name} y} \
                                                  z {getfield {name} z}
            addmsg {name} /diffamp_array/diffamp[{diffamp_index}] PLUS Vm
            sender = {getmsg {name}  -in -source {msgindex}}
            addmsg {sender} /diffamp_array/diffamp[{diffamp_index}] MINUS Vm
            setfield /diffamp_array/diffamp[{diffamp_index}] gain {1.0 / {getfield {name} Ra}} \
                                                             saturation 10e10

            diffamp_index = {diffamp_index} + 1
            
         elif (! {strcmp {getmsg {name}  -in -type {msgindex}} "RAXIAL"})
//            echo {name} {msgindex} RAXIAL {diffamp_index}
            setfield /diffamp_array/diffamp[{diffamp_index}] x {getfield {name} x} \
                                                  y {getfield {name} y} \
                                                  z {getfield {name} z}
            addmsg {name} /diffamp_array/diffamp[{diffamp_index}] PLUS Vm
            sender = {getmsg {name}  -in -source {msgindex}}
            addmsg {sender} /diffamp_array/diffamp[{diffamp_index}] MINUS Vm
            setfield /diffamp_array/diffamp[{diffamp_index}] gain {1.0 / {getfield {sender} Ra}} \
                                                             saturation 10e10

            diffamp_index = {diffamp_index} + 1
            
         end
//           echo {getmsg {name} -in -type {msgindex}}
     end
   end


//      echo {name}


      foreach name2 ({el /electrode_array/##[][TYPE=efield]})

          echo making msgs to electrode {name2}

          el_x = {getfield {name2} x}
          el_y = {getfield {name2} y}
          el_z = {getfield {name2} z}

          foreach name ({el /diffamp_array/##[][TYPE=diffamp]})
 
          cp_x = {getfield {name} x}
          cp_y = {getfield {name} y}
          cp_z = {getfield {name} z}

          distance = {sqrt {{pow {{cp_x} - {el_x}} 2.0} + \
                           {pow {{cp_y} - {el_y}} 2.0} + \
                           {pow {{cp_z} - {el_z}} 2.0}}}
//          echo {distance}

//          elem = ({findsolvefield {name}/../solve {name} Im})

//          echo {elem}

//          addmsg {name}/../solve  /electrode[{index}] CURRENT {elem} {distance}
 
          addmsg {name} {name2} CURRENT output {distance}
 
      end
      end


//   end

















