//Genesis - ascii output file

   str asc_name = "L5P_out"
   create asc_file /output/{asc_name}
   addmsg /L5P/soma /output/{asc_name} SAVE Vm
   addmsg /L5P/axon[0] /output/{asc_name} SAVE Vm
   addmsg /L5P/axon[10] /output/{asc_name} SAVE Vm
//   addmsg /L5P/p0b1b2b1b1b1b2b1b2b1b2b1b2b1b1b1b2b1b2b1b2b1b2b1b2b1b2b1b1[8] /output/{asc_name} SAVE Vm

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









