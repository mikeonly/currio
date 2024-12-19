//Genesis - ascii output file

   str asc_name = "network" @ {label} // "L5P_test"
   create asc_file /output/{asc_name}


function add_ascout (pathname) 

	str pathname

	addmsg {pathname}/soma /output/{asc_name} SAVE Vm
//	Addmsg /L5P/axon[0] /output/{asc_name} SAVE Vm
   	addmsg {pathname}/axon[1] /output/{asc_name} SAVE Vm
//	addmsg /L5P/p0b1b2b1b1b1b2b1b2b1b2b1b2b1b1b1b2b1b2b1b2b1b2b1b2b1b2b1b1[8] /output/{asc_name} SAVE Vm
//	addmsg /L5P/p4b2b1[15] /output/{asc_name} SAVE Vm

/*
    if ({exists {pathname}/soma/NaF})
        addmsg {pathname}/soma/NaF /output/{asc_name} SAVE Ik
    end
    if ({exists {pathname}/soma/InNa})
        addmsg {pathname}/soma/InNa /output/{asc_name} SAVE Ik
    end
    if ({exists {pathname}/axon/InNa})
        addmsg {pathname}/axon[0]/InNa /output/{asc_name} SAVE Ik
        addmsg {pathname}/axon[1]/InNa /output/{asc_name} SAVE Ik
        addmsg {pathname}/axon[2]/InNa /output/{asc_name} SAVE Ik
        addmsg {pathname}/axon[6]/InNa /output/{asc_name} SAVE Ik
        addmsg {pathname}/axon[10]/InNa /output/{asc_name} SAVE Ik
        addmsg {pathname}/axon[19]/InNa /output/{asc_name} SAVE Ik
    end

    addmsg {pathname}/p0b1b1b1[3]  /output/{asc_name} SAVE Vm
    if ({exists {pathname}/p0b1b1b1[3]/NaF})
        addmsg {pathname}/p0b1b1b1[3]/NaF /output/{asc_name} SAVE Ik
    end
*/
end



/*
   addmsg /L5P/p8[1]      /output/{asc_name} SAVE Vm
   addmsg /L5P/p8[1]/AMPA /output/{asc_name} SAVE Gk
   addmsg /L5P/p8[1]/AMPA /output/{asc_name} SAVE Ik 
   addmsg /L5P/p8[1]/GABA /output/{asc_name} SAVE Gk
  addmsg /L5P/p8[1]/GABA /output/{asc_name} SAVE Ik 
*/
   str asc_file_name = {filename} @ "L5P_" @ {label} @ "_somaVm.dat"
   setfield /output/{asc_name} filename {asc_file_name} initialize 1 append 0 leave_open 1 
   useclock /output/{asc_name} 1

   echo   asc_file_name is {asc_file_name}   
   echo   filename is {filename}
   echo   label is {label}









