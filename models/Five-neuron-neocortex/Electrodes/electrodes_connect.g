

function connect_to_electrodes (pathname)


	str pathname
	int msgcount, msgindex
	int total_number_axial_msgs = 0
	int diffamp_index = 0
	str sender



// count how many diffamps are needed

   	foreach name ({el {pathname}/##[][TYPE=compartment]})
     		msgcount = {getmsg {name} -incoming -count}
// echo {msgcount}
		for (msgindex = 0; msgindex < {msgcount}; msgindex = {msgindex} + 1)
         	if (! {strcmp {getmsg {name}  -in -type {msgindex}} "AXIAL"})
// echo {name} {msgindex} AXIAL
            		total_number_axial_msgs = {total_number_axial_msgs} + 1
         	elif (! {strcmp {getmsg {name}  -in -type {msgindex}} "RAXIAL"})
// echo {name} {msgindex} RAXIAL
            		total_number_axial_msgs = {total_number_axial_msgs} + 1
         	end
// echo {getmsg {name} -in -type {msgindex}}
     		end
   	end
     	echo total number of AXIAL and RAXIAL msgs is {total_number_axial_msgs}


          
// create the diffamp array


	if ({!{exists /diffamp}})
          	create diffamp /diffamp 
   	end

    	createmap /diffamp /diffamp_array_{pathname} {total_number_axial_msgs} 1



// position each diffamp element to the corresponding compartment, and make msgs
    
   	foreach name ({el {pathname}/##[][TYPE=compartment]})
     		msgcount = {getmsg {name} -incoming -count}
// echo {msgcount}
     		for (msgindex = 0; msgindex < {msgcount}; msgindex = {msgindex} + 1)
         	if (! {strcmp {getmsg {name}  -in -type {msgindex}} "AXIAL"})
// echo {name} {msgindex} AXIAL {diffamp_index}
            		setfield /diffamp_array_{pathname}/diffamp[{diffamp_index}] \
						x {getfield {name} x} \
                                                y {getfield {name} y} \
                                                z {getfield {name} z}
            		addmsg {name} /diffamp_array_{pathname}/diffamp[{diffamp_index}] PLUS Vm
            		sender = {getmsg {name}  -in -source {msgindex}}
            		addmsg {sender} /diffamp_array_{pathname}/diffamp[{diffamp_index}] MINUS Vm
            		setfield /diffamp_array_{pathname}/diffamp[{diffamp_index}] \
						gain {1.0 / {getfield {name} Ra}} saturation 10e10
            		diffamp_index = {diffamp_index} + 1
            
	         elif (! {strcmp {getmsg {name}  -in -type {msgindex}} "RAXIAL"})
// echo {name} {msgindex} RAXIAL {diffamp_index}
            		setfield /diffamp_array_{pathname}/diffamp[{diffamp_index}] \
						x {getfield {name} x} \
                                                y {getfield {name} y} \
                                                z {getfield {name} z}
            		addmsg {name} /diffamp_array_{pathname}/diffamp[{diffamp_index}] PLUS Vm
            		sender = {getmsg {name}  -in -source {msgindex}}
            		addmsg {sender} /diffamp_array_{pathname}/diffamp[{diffamp_index}] MINUS Vm
            		setfield /diffamp_array_{pathname}/diffamp[{diffamp_index}] \
						gain {1.0 / {getfield {sender} Ra}} saturation 10e10
            		diffamp_index = {diffamp_index} + 1
            	end
// echo {getmsg {name} -in -type {msgindex}}
     		end
   	end

// echo {name}



// make msgs from {pathname} diffamps to electrodes

   	float el_x, el_y, el_z  // (x,y,z) coordinates of electrode
   	float cp_x, cp_y, cp_z  // (x,y,z) coordinates of compartment
   	float distance          // distance between electrode and compartment
   	str name, name2, elem


      	foreach name2 ({el /electrode_array/##[][TYPE=efield]})

  echo making msgs from {pathname} to electrode {name2}

          	el_x = {getfield {name2} x}
          	el_y = {getfield {name2} y}
          	el_z = {getfield {name2} z}

          	foreach name ({el /diffamp_array_{pathname}/##[][TYPE=diffamp]})
 
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
 
      		end // foreach diffamp
      	end // foreach efield


end // function

















