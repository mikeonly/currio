// genesis

// RM 17 Sep 2008
// Contains function with as parameters : source, target, connection probability,
// weight and delay.

// A few parameters have been assumed fixed, hence they are not in the argument list
// (such as weight and delay distributions). 
// The connections are laid horizontally, using only the z-coordinate as a criterion,
// Radial connections have been implemented in Excitatory_fibres_connect.g, but not 
// tested yet. 


 

function connect_horizontally (source, target, probability, weight, delay)

	str source, target
        float probability, weight, delay
 
// First connection scheme: each fiber runs horizontally and is allowed to make a synapse
// on each compartment in (approximately) the same horizontal plane

	echo connecting {source} to {target} with probability {probability} \
			weight {weight} and delay {delay}

	volumeconnect 	{source} \
                    	{target} \
                    	-relative \
                    	-sourcemask box -1 -1 -1 1 1 1 \
                    	-destmask ellipsoid 0 0 0 1 1 2e-6 \ 
                    	-probability {probability}

	volumeweight 	{source} \
                   	{target} \
			-fixed {weight} \
			-uniform {weight_distribution}

	volumedelay   	{source} \
                    	{target} \
                    	-radial {E_fibre_conduction_velocity} \
			-uniform {delay_distribution}

	volumedelay   	{source} \
                    	{target} \
                    	-fixed {delay}\
			-add

end



