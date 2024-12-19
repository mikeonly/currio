// genesis

int i, j
float  x, y, z
str list 
str output 

// include ../Electrodes/Electrodes_make.g

    list = ""
    output = "Electrode-positions.dat"


   	for (i = 0; i < {number_electrodes}; i = i + 1)
 
      		list = (list) @ "electrode" @ {i} @ {chr 10}

            for (j = 0; {j < number_contact_points}; j = j + 1)
                x =  {getfield /electrode_array/electrode[{i}]/contact[{j}] x}
                y =  {getfield /electrode_array/electrode[{i}]/contact[{j}] y}
                z =  {getfield /electrode_array/electrode[{i}]/contact[{j}] z}
                list = (list) @ "contact" @ {j} @ "    (" @ {x} @ ", " @ {y} @ ", " @ {z} @ ")" @ {chr 10}  
            end

            list = (list) @ {chr 10}
    end

    echo {list}  > {output}




