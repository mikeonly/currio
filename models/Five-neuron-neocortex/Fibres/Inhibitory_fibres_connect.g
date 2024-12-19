// genesis

// Assumes /Inhibitory_fibres has been created (by calling make_fibres from Fibres_make.g).

// A parameter TARGET gives the pathname of the target neuron to which all fibres from
// /Inhibitory fibres are to be connected.

// The connections may be laid horizontally, using only the z-coordinate as a criterion,
// or radially, allowing the fibre to connect to all compartments at about the same
// position from the soma. Only the first implementation is active now.

// Remark: It would be cleaner to add the fibres along with all connection parameters as
// arguments of the function, but this is too complicated now.
 
int  index


function connect_horizontally_to_inhibitory_fibres (target)

	str target
 
// Connecting fibres to L5P *****

	ce /Inhibitory_fibres



// First connection scheme: each fiber runs horizontally and is allowed to make a synapse
// on each compartment in (approximately) the same horizontal plane


echo Connecting inhibitory feedforward fibres 

	volumeconnect FF/fibre[] \
                    {target}[][TYPE=compartment]/GABA \
                    -relative \
                    -sourcemask box -1 -1 -1 1 1 1 \
                    -destmask ellipsoid 0 0 0 1 1 2e-6 \ 
                    -probability 0.025 // 0.05 // 1.0 // {P_parallel_fiber_to_Golgi_cell_synapse}

	volumeweight FF/fibre[] \
                   {target}[][TYPE=compartment]/GABA  -fixed \
                   {weight_GABA_synapse} -uniform {weight_distribution}

	volumedelay   FF/fibre[] \
                    {target}[][TYPE=compartment]/GABA \
                    -fixed 0.001 // 0.0004 // 08 // 0.001 // 0.002
// -radial {E_fibre_conduction_velocity} -uniform {delay_distribution}


echo Connecting inhibitory intracolumnar feedback fibres 

	volumeconnect FBintra/fibre[] \
                    {target}[][TYPE=compartment]/GABA \
                    -relative \
                    -sourcemask box -1 -1 -1 1 1 1 \
                    -destmask ellipsoid 0 0 0 1 1 2e-6 \ 
                    -probability 0.05 // 1.0 // {P_parallel_fiber_to_Golgi_cell_synapse}

	volumeweight FBintra/fibre[] \
                   {target}[][TYPE=compartment]/GABA  -fixed \
                   {weight_GABA_synapse} -uniform {weight_distribution}

	volumedelay   FBintra/fibre[] \
                    {target}[][TYPE=compartment]/GABA \
                    -fixed 0.02
//                    -radial {E_fibre_conduction_velocity} -uniform {delay_distribution}

end

/*
echo Connecting inhibitory intercolumnar feedback fibres

      volumeconnect FBinter/FBinter_fibre[] \
                    /L5P/p#[][TYPE=compartment]/GABA \
                    -relative \
                    -sourcemask box -1 -1 -1 1 1 1 \
                    -destmask ellipsoid 0 0 0 1 1 2e-6 \ 
                    -probability 0.05 // 1.0 // {P_parallel_fiber_to_Golgi_cell_synapse}

      volumeweight FBinter/FBinter_fibre[] \
                   /L5P/p#[][TYPE=compartment]/GABA  -fixed \
                   {weight_GABA_synapse} -uniform {weight_distribution}

      volumedelay   FBinter/FBinter_fibre[] \
                    /L5P/p#[][TYPE=compartment]/GABA \
                    -radial {E_fibre_conduction_velocity} -uniform {delay_distribution}
*/

/*

// Second connection scheme: each fiber is allowed to make a synapse on compartments
// located from the soma (the origin) at the same distance as the compartment to which the fibre
// has been associated (remember that a fibre for each compartment was created).
int i
float r, x1, y1, z1

      ce {FF}

      for (i = 0; i < 686; i = {i} + 1)
          x1 = {getfield FF_fibre[{i}] x}
          y1 = {getfield FF_fibre[{i}] y}
          z1 = {getfield FF_fibre[{i}] z}
          r = {sqrt {x1*x1 + y1*y1 + z1*z1}}
//          echo {r}

          volumeconnect FF_fibre[{i}] \
                    /L5P/p#[][TYPE=compartment]/GABA \
                    -sourcemask box -1 -1 -1 1 1 1 \
                    -destmask ellipsoid 0 0 0 {r + 1e-6} {r + 1e-6} {r + 1e-6} \ 
                    -desthole ellipsoid 0 0 0 {r - 1e-6} {r - 1e-6} {r - 1e-6} \ 
                    -probability 0.1 // 0.05
      end

      volumeweight FF_fibre[] \
                   /L5P/p#[][TYPE=compartment]/GABA  -fixed \
                   {weight_AMPA_synapse} -uniform {weight_distribution}

      volumedelay   FF_fibre[] \
                    /L5P/p#[][TYPE=compartment]/GABA \
                    -radial {E_fibre_conduction_velocity} -uniform {delay_distribution}


      ce {FBintra}

      for (i = 0; i < 686; i = {i} + 1)
          x1 = {getfield FBintra_fibre[{i}] x}
          y1 = {getfield FBintra_fibre[{i}] y}
          z1 = {getfield FBintra_fibre[{i}] z}
          r = {sqrt {x1*x1 + y1*y1 + z1*z1}}
//          echo {r}
  
          volumeconnect FBintra_fibre[{i}] \
                    /L5P/p#[][TYPE=compartment]/GABA \
                    -sourcemask box -1 -1 -1 1 1 1 \
                    -destmask ellipsoid 0 0 0 {r + 1e-6} {r + 1e-6} {r + 1e-6} \ 
                    -desthole ellipsoid 0 0 0 {r - 1e-6} {r - 1e-6} {r - 1e-6} \ 
                    -probability 0.1 // 0.05
      end

      volumeweight FBintra_fibre[] \
                   /L5P/p#[][TYPE=compartment]/GABA  -fixed \
                   {weight_AMPA_synapse} -uniform {weight_distribution}

      volumedelay   FBintra_fibre[] \
                    /L5P/p#[][TYPE=compartment]/GABA \
                    -radial {E_fibre_conduction_velocity} -uniform {delay_distribution}




      ce {FBinter}

      for (i = 0; i < 686; i = {i} + 1)
          x1 = {getfield FBinter_fibre[{i}] x}
          y1 = {getfield FBinter_fibre[{i}] y}
          z1 = {getfield FBinter_fibre[{i}] z}
          r = {sqrt {x1*x1 + y1*y1 + z1*z1}}
//          echo {r}
  
          volumeconnect FBinter_fibre[{i}] \
                    /L5P/p#[][TYPE=compartment]/GABA \
                    -sourcemask box -1 -1 -1 1 1 1 \
                    -destmask ellipsoid 0 0 0 {r + 1e-6} {r + 1e-6} {r + 1e-6} \ 
                    -desthole ellipsoid 0 0 0 {r - 1e-6} {r - 1e-6} {r - 1e-6} \ 
                    -probability 0.1 // 0.05
      end

      volumeweight FBinter_fibre[] \
                   /L5P/p#[][TYPE=compartment]/GABA  -fixed \
                   {weight_AMPA_synapse} -uniform {weight_distribution}

      volumedelay   FBinter_fibre[] \
                    /L5P/p#[][TYPE=compartment]/GABA \
                    -radial {E_fibre_conduction_velocity} -uniform {delay_distribution}




*/


