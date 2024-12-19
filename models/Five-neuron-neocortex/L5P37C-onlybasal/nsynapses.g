// genesis

int sum, nsynapses
str list 
str output 

include ../Fibres/Fibres_make.g

    list = ""
    output = "L5P_AMPA_nsynapses.dat"

       sum = 0
       foreach name ({el /L5P/p#[][TYPE=compartment]})
//         echo {name}
         ce {name}/AMPA
         nsynapses = {getfield . nsynapses}
         sum = {sum} + {nsynapses}
//         list = (list) @ {name} @ " " @ {nsynapses} @ " " @ {chr 10}
       end

       list = (list) @ {sum} @ " " @ {chr 10}
       
       
       ce /Excitatory_fibres/FF
       sum = 0
       for (i = 0; i < {number_FF_fibres}; i = {i} + 1)
            sum = {sum} + {getsyncount fibre[{i}]}
       end
       list = (list) @ {sum} @ " " @ {chr 10}
       
       
       ce /Excitatory_fibres/FBintra
       sum = 0
       for (i = 0; i < {number_FBintra_fibres}; i = {i} + 1)
            sum = {sum} + {getsyncount fibre[{i}]}
       end
       list = (list) @ {sum} @ " " @ {chr 10}
       
       
       ce /Excitatory_fibres/FBinter
       sum = 0
       for (i = 0; i < {number_FBinter_fibres}; i = {i} + 1)
            sum = {sum} + {getsyncount fibre[{i}]}
       end
       list = (list) @ {sum} @ " " @ {chr 10}
              
       
    echo {list}  > {output} // {source_list}


    list = ""
    output = "L5P_GABAA_nsynapses.dat"

       sum = 0
       foreach name ({el /L5P/p#[][TYPE=compartment]})
//         echo {name}
         ce {name}/GABA
         nsynapses = {getfield . nsynapses}
         sum = {sum} + {nsynapses}
//         list = (list) @ {name} @ " " @ {nsynapses} @ " " @ {chr 10}
       end

       list = (list) @ {sum} @ " " @ {chr 10}
       
       
       ce /Inhibitory_fibres/FF
       sum = 0
       for (i = 0; i < {number_FF_fibres}; i = {i} + 1)
            sum = {sum} + {getsyncount fibre[{i}]}
       end
       list = (list) @ {sum} @ " " @ {chr 10}
       
       
       ce /Inhibitory_fibres/FBintra
       sum = 0
       for (i = 0; i < {number_FBintra_fibres}; i = {i} + 1)
            sum = {sum} + {getsyncount fibre[{i}]}
       end
       list = (list) @ {sum} @ " " @ {chr 10}
       
       
       ce /Inhibitory_fibres/FBinter
       sum = 0
       for (i = 0; i < {number_FBinter_fibres}; i = {i} + 1)
            sum = {sum} + {getsyncount fibre[{i}]}
       end
       list = (list) @ {sum} @ " " @ {chr 10}
       
       
       
    echo {list}  > {output} // {source_list}





