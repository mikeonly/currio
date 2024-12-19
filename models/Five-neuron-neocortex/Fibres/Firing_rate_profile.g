//genesis

/* This script has to do with the spatial (vertical depth) profile of inputs.
   Input arguments:
	PATH : the pathname of an array of diffamp elements;
		each element has been assigned a (vertical) position
		and corresponds to a fibre (randomspike element) to 
		which it sends a RATE msg
        O1, SD1, W!, O2, SD2, W2 : parameters for two 1D Gaussians 
		along vertical dimension (cortical depth) (origin, SD, total area)

   Output:
        the PLUS field of each diffamp element is set to the (sum of) Gaussian weights,
        by which the diffamps represent a spatial profile of weight and/or fibre density
*/

// Note: why not put gain field, and send other inputs as PLUS msgs ?
// Done 9/9/2008


// Assumes diffamps already exist!!!

// Firing rate now in input field, gain now modulated by GAIN msg from other diffamp.

// Modification on 12/9/2007. To allow other factors to mofidy
// afferent firing rate, diffamp elements are inserted. The 'firing rate'
// is now expressed in the 'gain' field of the diffamp element.
// The diffamp element sends  its output to its corresponding randomspike
// element, and can receive PLUS or MINUS msgs from other objects.

// Sets the firing rates of the randomspike elements to values
// defined by position. The profile is the sum of two Gaussians.
// Position can be defined either along the depth (Z-) axis, or
// radially from the soma.
// Normalization makes the mean firing rate of the entire population
// of afferents equal to mean_firing_rate.
// The profile will be written to a file to be visualized with (Genesis) xplot
// (which does not seem to require ordered series for plotting).
// Of course the resulting density of afferent spikes will also be greatly determined by the density
// of fibres along depth location, which this procedure does not take into account. 



function make_firing_rate_profile (path, o1, sd1, w1, o2, sd2, w2, mean_firing_rate)


str path

// the origins, standard deviations and weights of the two gaussians
// the weights are relative magnitudes, their absolute values will be normalized out
float o1, o2, sd1, sd2, w1, w2  

float mean_firing_rate
float firing_rate
float denominator,coefficient, sum
float position
int number_of_elements, index
str name, diffamp_path, diffamp_element


echo {path}  {o1}  {sd1}  {w1}  {o2}  {sd2}  {w2}  {mean_firing_rate}


// count the elements in path

      number_of_elements = 0
      ce {path}
      foreach name ({el ./##[][TYPE=diffamp]})
//        echo {name}
        number_of_elements = {number_of_elements + 1}
      end
      echo number_of_elements {number_of_elements}



// make the profile by calculating the gain field of the diffamp elements

//      ce {diffamp_path}
      sum = 0

// first Gaussian

      if ({{w1 * sd1} != 0})
      
      denominator = {sd1*sd1*2}
      coefficient = {w1 / sd1}
      foreach name ({el ./##[][TYPE=diffamp]})
          position = {getfield {name} z}
          firing_rate = {coefficient * {exp {-{{position-o1}*{position-o1}}/denominator}}}
//          echo {name} {position} {firing_rate}
          sum = {sum + firing_rate}
//          setfield {name} plus {firing_rate}
          setfield {name} gain {firing_rate}
      end

      end
      echo sum1 {sum}

// second Gaussian and calculation of sum for later normalization

      if ({{w2 * sd2} != 0})
      denominator = {sd2*sd2*2}
      coefficient = {w2 / sd2}
      foreach name ({el ./##[][TYPE=diffamp]})
          position = {getfield {name} z}
          firing_rate = {coefficient * {exp {-{{position-o2}*{position-o2}}/denominator}}}
//          echo {name} {position} {firing_rate}
//          setfield {name} plus {{getfield {name} plus} + {firing_rate}} 
          setfield {name} gain {{getfield {name} gain} + {firing_rate}} 
          sum = {sum + firing_rate}
      end

      end
      echo sum2 {sum}
 

// normalize and show
// want that sum of firing rates equals {mean_firing_rate * number_of_elements}
//      denominator = {sum / number_of_elements * mean_firing_rate}
      denominator = {sum / {number_of_elements * mean_firing_rate}}
      echo denominator {denominator}
      if ({denominator != 0})
	  foreach name ({el ./##[][TYPE=diffamp]})
//            echo {name}  {getfield {name} z}   {getfield {name} plus}  {{getfield {name} plus} / {denominator}}
//              firing_rate =  {{getfield {name} plus} / {denominator}}
              firing_rate =  {{getfield {name} gain} / {denominator}}
//              setfield {name}  plus {firing_rate}
              setfield {name}  gain {firing_rate}
//            echo {name}  {getfield {name} z}    {firing_rate}
	  end
      end



// print the profile

str list = ""
str output = {substring {path} 1 1} @ "_" @ {substring {path} 19 {{strlen {path}} -1}} @ "_profile.dat" // remove initial backslah from pathname
echo {output}

      foreach name ({el ./##[][TYPE=diffamp]})
//          list = (list) @ {getfield {name} z} @ " " @ {getfield {name} plus} @ {chr 10}
          list = (list) @ {getfield {name} z} @ " " @ {getfield {name} gain} @ {chr 10}
//          echo {name} {getfield {name} z} {getfield {name} plus}
      end
      echo {list}  > {output} // {source_list}


      sum = 0
      foreach name ({el ./##[][TYPE=diffamp]})
//          sum = {{sum} + {getfield {name} plus}}
          sum = {{sum} + {getfield {name} gain}}
      end

      echo average firing rate is {sum / {number_of_elements}} 

end

