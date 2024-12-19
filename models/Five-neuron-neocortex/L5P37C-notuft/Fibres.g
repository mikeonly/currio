// genesis

// Function make_fibres (pathname).
// Creates in {pathname} three populations of fibres: feedforward, feedback intracolumn,
// feedback intercolumn.

// Each population consists of randomspike elements with associated diffamps.
// The diffamps send RATE msgs to their respective randomspikes. 
// In other scripts, the diffamps will get PLUS messages, e.g.feedforward fibres 
// will get input from Harsch-Robinson_input.g, whereas the randsomspikes will be 
// connected (in Excitatory_fibers.g and Inhibitory_fibres.g) to synapses on the L5P cell.

// Actually, for each compartment on L5P, one fibre is generated, (almost) randomly
// assigned to one of the three classes and put at the same position as the compartment.


 
int  index



function make_fibres (pathname)

str pathname


// Make library protoptypes *****

   if ({!{exists /library}})
          create neutral /library 
          disable /library
   end

   if ({!{exists /library/FF_fibre}})
         //   create randomspike2 /library/FF_fibre  // randomspike 2 does not exist in official release
   		create randomspike /library/FF_fibre
		//   setfield ^ rate {E_fibre_rate} 
		//              abs_refract 0.001 
		//              rate_type RS_EFFECTIVE

	   create randomspike /library/FBintra_fibre
	   create randomspike /library/FBinter_fibre

	   create diffamp /library/FF_diffamp
	   setfield ^ plus 0 minus 0 saturation 10e10
	   create diffamp /library/FBintra_diffamp
	   setfield ^ plus 0 minus 0 saturation 10e10
	   create diffamp /library/FBinter_diffamp
	   setfield ^ plus 0 minus 0 saturation 10e10
   end



// Make subpopulations *****

	echo Making {pathname} and subpopulations

	if(!{exists {pathname}}) 
          create neutral {pathname}
	end
	create neutral {pathname}/FF
	create neutral {pathname}/FBintra
	create neutral {pathname}/FBinter
   
	echo The fibres
	createmap /library/FF_fibre {pathname}/FF \
             686 1 -delta 0 0 -origin 0 0 
	createmap /library/FBintra_fibre {pathname}/FBintra \
             686 1 -delta 0 0 -origin 0 0 
	createmap /library/FBinter_fibre {pathname}/FBinter \
             686 1 -delta 0 0 -origin 0 0 

	echo The diffamps
	createmap /library/FF_diffamp {pathname}/FF \
             686 1 -delta 0 0 -origin 0 0 
	createmap /library/FBintra_diffamp {pathname}/FBintra \
             686 1 -delta 0 0 -origin 0 0 
	createmap /library/FBinter_diffamp {pathname}/FBinter \
             686 1 -delta 0 0 -origin 0 0 


// works only for randomspike2; not sure this exists in Genesis2.3
//   setfield {pathname}/E_fibre[] seed1 0 -increment 9 100
//   setfield {pathname}/E_fibre[] seed2 0 -increment 9e-2 100



// Position fibres at corresponding L5P compartments *****

	echo Calculating positions of {pathname} 

	str subpath
	ce {pathname}
	index = 0
   
	foreach name ({el /L5P/p#[][TYPE=compartment]})
   
//   echo {name}
      if ({{index % 3} == 0})
           subpath = "FF/FF_fibre"
      elif ({{index % 3} == 1})
           subpath = "FBintra/FBintra_fibre"
      else subpath = "FBinter/FBinter_fibre"
      end
      
	 setfield {subpath}[{index / 3}] \
                x {getfield {name} x} \
                y {getfield {name} y} \
                z {getfield {name} z} 

//        echo {name} {index}  {subpath} {index / 3}  // OK works
        index = {index + 1}
//        echo index = {index}   // OK 2058 dendritic compartments
   end



// Connect diffamps to fibres *****

	echo Sending RATE msgs from diffmaps to fibres 

	for (index = 0; index < 686; index = {index} + 1)
	   setfield FF/FF_diffamp[{index}]              x {getfield FF/FF_fibre[{index}] x} \
	                                                y {getfield FF/FF_fibre[{index}] y} \
	                                                z {getfield FF/FF_fibre[{index}] z}
	   setfield FBintra/FBintra_diffamp[{index}]    x {getfield FBintra/FBintra_fibre[{index}] x} \
	                                                y {getfield FBintra/FBintra_fibre[{index}] y} \
	                                                z {getfield FBintra/FBintra_fibre[{index}] z}
	   setfield FBinter/FBinter_diffamp[{index}]    x {getfield FBinter/FBinter_fibre[{index}] x} \
	                                                y {getfield FBinter/FBinter_fibre[{index}] y} \
	                                                z {getfield FBinter/FBinter_fibre[{index}] z}
	   
       addmsg FF/FF_diffamp[{index}]            FF/FF_fibre[{index}]              RATE    output
       addmsg FBintra/FBintra_diffamp[{index}]  FBintra/FBintra_fibre[{index}]    RATE    output
       addmsg FBinter/FBinter_diffamp[{index}]  FBinter/FBinter_fibre[{index}]    RATE    output
	end
   
   
end


