// genesis

// Function make_fibres (pathname).
// Creates in {pathname} three populations of fibres: feedforward, feedback intracolumn,
// feedback intercolumn, using a {template} model neuron as input, so as to create one
// fibre for each compartment of the template.

// Each population consists of randomspike elements with associated diffamps.
// The associated diffamps are needed to flexibly modulate the rates by different sources.
// The diffamps send RATE msgs to their respective randomspikes. 
// In other scripts, the diffamps will get PLUS messages, e.g.feedforward fibres 
// will get input from Harsch-Robinson_input.g.
// The gain fields of the diffamps are set in Firing_rate_profile.g  whereas the randsomspikes will be 
// connected (in Excitatory_fibers.g and Inhibitory_fibres.g) to synapses on the L5P cell.

// Actually, for each compartment on L5P, one fibre is generated, (almost) randomly
// assigned to one of the three classes and put at the same position as the compartment.


 
int  index

	int number_of_fibres 
	int number_FF_fibres 
	int number_FBintra_fibres 
	int number_FBinter_fibres 


function make_fibres (pathname, template)

	str pathname, template


// Make library protoptypes *****

   	if ({!{exists /library}})
        	create neutral /library 
          	disable /library
   	end

	if ({!{exists /library/fibre}})
         //   create randomspike2 /library/fibre  // randomspike 2 does not exist in official release
   		create randomspike /library/fibre
        setfield ^ abs_refract 0.002
		//   setfield ^ rate {E_fibre_rate} 
		//              abs_refract 0.001 
		//              rate_type RS_EFFECTIVE


	create diffamp /library/diffamp
	setfield ^ plus 0 minus 0 saturation 10e10
   	end


// count numbers of fibres to be made

/*
	number_of_fibres = 0

	foreach name ({el /L5P/p#[][TYPE=compartment]})
//	foreach name ({el {template}#[][TYPE=compartment]})
                number_of_fibres = {number_of_fibres} + 1
        end

        echo old number of fibres = {number_of_fibres}
*/

	number_of_fibres = 0
	echo {template}
//	foreach name ({el /L5P/p#[][TYPE=compartment]})
	foreach name ({el {template}[][TYPE=compartment]})
//        echo {name}
                number_of_fibres = {number_of_fibres} + 1
        end

//        echo number of fibres = {number_of_fibres}

	number_FF_fibres = {number_of_fibres / 3}
	number_FBintra_fibres = {number_of_fibres / 3}
	number_FBinter_fibres = {number_of_fibres / 3}
        if ({{number_of_fibres % 3} > 0})
              number_FF_fibres =  {number_FF_fibres + 1}
        end
        if ({{number_of_fibres % 3} > 1})
              number_FBintra_fibres =  {number_FBintra_fibres + 1}
        end

        echo  the number of fibres = {number_of_fibres}
        echo  the number of FF fibres = {number_FF_fibres}
        echo  the number of intracolumn FB fibres = {number_FBintra_fibres}
        echo  the number of intercolumn FB fibres = {number_FBinter_fibres}


// Make subpopulations *****

	echo Making {pathname} and subpopulations

	if(!{exists {pathname}}) 
          create neutral {pathname}
	end
	create neutral {pathname}/FF
	create neutral {pathname}/FBintra
	create neutral {pathname}/FBinter
   
	echo The fibres
	createmap /library/fibre {pathname}/FF \
             {number_FF_fibres} 1 -delta 0 0 -origin 0 0 
	createmap /library/fibre {pathname}/FBintra \
             {number_FBintra_fibres} 1 -delta 0 0 -origin 0 0 
	createmap /library/fibre {pathname}/FBinter \
             {number_FBinter_fibres} 1 -delta 0 0 -origin 0 0 

	echo The diffamps
	createmap /library/diffamp {pathname}/FF \
             {number_FF_fibres} 1 -delta 0 0 -origin 0 0 
	createmap /library/diffamp {pathname}/FBintra \
             {number_FBintra_fibres} 1 -delta 0 0 -origin 0 0 
	createmap /library/diffamp {pathname}/FBinter \
             {number_FBinter_fibres} 1 -delta 0 0 -origin 0 0 


// works only for randomspike2; not sure this exists in Genesis2.3
//   setfield {pathname}/E_fibre[] seed1 0 -increment 9 100
//   setfield {pathname}/E_fibre[] seed2 0 -increment 9e-2 100



// Position fibres at corresponding L5P compartments *****

	echo Calculating positions of {pathname} 

	str subpath
	ce {pathname}
	index = 0
   
//	foreach name ({el /L5P/p#[][TYPE=compartment]})
	foreach name ({el {template}[][TYPE=compartment]})
   
//   echo {name}
		if ({{index % 3} == 0})
        	   	subpath = "FF/fibre"
      		elif ({{index % 3} == 1})
             		subpath = "FBintra/fibre"
      		else subpath = "FBinter/fibre"
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

	for (index = 0; index < {number_FF_fibres}; index = {index} + 1)
	setfield	FF/diffamp[{index}]           	x {getfield FF/fibre[{index}] x} \
	                                             	y {getfield FF/fibre[{index}] y} \
	                                             	z {getfield FF/fibre[{index}] z}
	addmsg		FF/diffamp[{index}]    		FF/fibre[{index}]         RATE    output
	end
   
	for (index = 0; index < {number_FBintra_fibres}; index = {index} + 1)
	setfield 	FBintra/diffamp[{index}]    	x {getfield FBintra/fibre[{index}] x} \
	                                                y {getfield FBintra/fibre[{index}] y} \
	                                                z {getfield FBintra/fibre[{index}] z}
      	addmsg		FBintra/diffamp[{index}]  	FBintra/fibre[{index}]    RATE    output
	end
   
	for (index = 0; index < {number_FBinter_fibres}; index = {index} + 1)
	setfield 	FBinter/diffamp[{index}]   	x {getfield FBinter/fibre[{index}] x} \
	                                                y {getfield FBinter/fibre[{index}] y} \
	                                                z {getfield FBinter/fibre[{index}] z}
	addmsg 		FBinter/diffamp[{index}]	FBinter/fibre[{index}]    RATE    output
	end
   
   
end


