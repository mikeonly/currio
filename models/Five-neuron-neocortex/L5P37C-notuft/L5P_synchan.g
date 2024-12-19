// Reinoud Maex 20 June 2007
// The AMPA and GABAA channels are copied from De Schutter & Bower 
// Purkinje cell model, modified by Sergio Solinas et al. (EJN 2006).
// The NMDA channel is copied from the Maex & De Schutter (J Neurophysiol 1998)
// granule cell model.
// Hence this script merges the files Purk_syn37dC.g and Gran_synchan.g 


//genesis - Purkinje cell M9 genesis2.1 script
/* Copyright E. De Schutter (Caltech and BBF-UIA) */

/**********************************************************************
** Sets of synapse objects developed for rat cerebellum Purkinje
** E. De Schutter, Caltech, 1991-1992
**********************************************************************/

/* Reference:
** E. De Schutter and J.M. Bower: An active membrane model of the
** cerebellar Purkinje cell: II. Simulation of synaptic responses.
** Journal of Neurophysiology  71: 401-419 (1994).
** http://bbf-www.uia.ac.be/TNB/TNB_pub7.html
** Consult this reference for sources of experimental data.
*/

include ../L5P37C-notuft/L5P_const+axon+syn.g

// CONSTANTS
/* should be defined by calling routine (all correctly scaled):
**	E_non_NMDA
**	E_GABA, G_GABA */

// factor Q10 of 1.5: Regehr et al. J. Neuroscience 1996 16(18):5661-5671
float Q10 = 1.5
function Calc_tau(Q10,T1,T2,tau1)
  return {tau1 / { Q10**{{T2 -T1}/10}}}
end

float temp = 37 // Celsius degrees
float Q12_non_NMDA = 1.68 // for 10 1.4


// correctio for low input resistance
float Rin_corr = 1


  /*********************************************************************
  **               The synaptic conductance equations 
  *********************************************************************/


function make_GABAA_channels
    
    /* GABA channel, made by SS */
    /* Reference: current clamp data from 
    ** Pouzat C. and Hestrin S. J. Neuroscince 1997
    ** V_drive 60 mV, I_syn 20 pA -> G_peak = 333 pS
    ** (that is 35.3 pA at 37 C which should be recorded in voltage clamp)
    ** T_rise: 2.6 +- 0.5 ms, Thalf-width = 16.7 +- 2.7 ms 
    ** room temperature: we assume 23 Celsius degrees
    ** Found T_on = 1.65 ms and T_off = 9.3 ms by hand (MATLAB)
    ** Found with c++ program /bbf/milaan/sergio/Work/C++/Rise2Tau/rise2tau:
    ** Found T_on = 2.1 ms and T_off = 15.3 ms by hand (c++)	*/
    float PC_GABAA_factor = 5.8
    // Stell & Stell1 channels: average conpartment surface  4.020627647e-11 m2
    float PC_GABAA_gmax = {333e-12 /  4.020627647e-11 * PC_GABAA_factor}
    // Stell3 channels: average conpartment surface  2.247033843e-10 m2
    float PC_GABAAm_gmax = {333e-12 / 2.49670427e-10 * PC_GABAA_factor}
    // Stell4 channels: somatic surface  m2
    float PC_GABAAs_gmax = {3.5e-9 / 2.789857497e-09 }
    float PC_GABAA_t_on = 1.65e-3
    float PC_GABAA_t_off = 9.3e-3


    /* Synaptic channel for Stellate connections */
    if (!({exists GABA}))
        	create synchan GABA
    end
    setfield GABA Ek {E_GABA} 	\
  	tau1 {Calc_tau {Q10} 23 {temp} {PC_GABAA_t_on}} \
        	tau2 {Calc_tau {Q10} 23 {temp} {PC_GABAA_t_off}}  \
       	gmax {G_GABA} frequency 0.0
  

    /* Synaptic channel for Basket connections on PC main dendrite */
    if (!({exists GABA2}))
        	create synchan GABA2
    end
    setfield GABA2 Ek {E_GABA} 	\
  	tau1 {Calc_tau {Q10} 23 {temp} {PC_GABAA_t_on}} \
        	tau2 {Calc_tau {Q10} 23 {temp} {PC_GABAA_t_off}}  \
       	gmax {G_GABA} frequency 0.0
  

    /* Synaptic channel for Basket connections PC soma */
    if (!({exists GABA3}))
        	create synchan GABA3
    end
	// SS We use 37 degrees here since it's not specified in the article
	// RM This does not make sense because then the somatic GABA is slower than the dendritic; 
	// changed to 37 to 23
    setfield GABA3 Ek {E_GABA} 	\
  	tau1 {Calc_tau {Q10} 23 {temp} {PC_GABAA_t_on}} \ 
      	tau2 {Calc_tau {Q10} 23 {temp} {PC_GABAA_t_off}}  \
       	gmax {G_GABA} frequency 0.0


    // set the right GABAA density value to get gmax from Hausser M. and Clark B. A. Neuron 1997
    G_GABA = {{PC_GABAA_gmax} * {Q10**{{{temp} - 23}/10}}}
    echo GABAA gmax {G_GABA}
    G_GABAm = {{PC_GABAAm_gmax} * {Q10**{{{temp} - 23}/10}}}
    echo GABAA2 gmax {GB_GABA}
    G_GABAs = {{PC_GABAAs_gmax} * {Q10**{{{temp} - 37}/10}}} 
    echo GABAAs soma gmax {GB_GABAs}

end // make_GABAA_channels


function make_AMPA_channels
    
    /* non-NMDA channel, made by SS */
    /* Reference: Barbour B. 2002 (personal communication)
    ** room temp: 32 C
    ** somatic EPSC peak = 8.4 +- 7.1 pA
    ** (that is 10.2 pA at 37 C which should be recorded in voltage clamp)
    ** the driving force at the excitatory synapse is 70 mV 
    ** during Voltage clamp at -70 mV
    ** thus the peak conductance G_par_syn = 120 pS
    ** t_on = 1.0 +- 0.7 ms
    ** the low-pass filtering effect of the large PC dendritic tree
    ** could slow down the fast rise EPSC fase. Since the effect of single vescicle release
    ** is kown to have an almost instantaneous effect on PSC we use a faster t_on
    ** t_on = 0.7 ms
    ** t_off = 11.1 +- 5.7 ms 
    ** t_off is long and it light be due to the glutammate spillover
    ** activating the extrasynaptic AMPA receptors 
    ** We use t_off = 1.2 ms */

    /* Modified by SS 30/04/2002
    ** We need to be able to set the AMPA receptor strength 
    ** indipendently on previous settings 
    ** since when the AMPA receptor is placed on the spine head
    ** it's scaled by its surface here we devide the gmax by the surface */
    float dia = 0.54e-6
    float surf = dia*dia*{PI}
    //- here we can keep control of the Gmax since the readcell 
    //   will add the spines (*rand_spines) without modify them
    float PC_AMPA_factor = 9
    float PC_AMPA_gmax =  {120e-12/surf * PC_AMPA_factor}
    float PC_AMPA_t_on = 0.7e-3
    float PC_AMPA_t_off = 1.2e-3
  
    /* asynchronously firing channel */
    if (!({exists AMPA}))
        	create synchan AMPA
    end    
    setfield AMPA 	Ek {E_AMPA} \
        		tau1 {Calc_tau {Q10} 32 {temp} {PC_AMPA_t_on}} \
        		tau2 {Calc_tau {Q10} 32 {temp} {PC_AMPA_t_off}}   \
        	        frequency 0.0
    
    G_par_syn = {{PC_AMPA_gmax}  * {Q10**{{{temp} - 32}/10}} }
    echo AMPA gmax = {G_par_syn}
    setfield AMPA gmax {G_par_syn}

    /* synchronously firing channel removed, was for climbing fibre synapses on PC */

end // make_AMPA_channels


function make_NMDA_channels

	/* NMDA channel made by CP */
	/* From Gabbiani et al.(model) 1994, based on Jahr and Stevens */

	float Q10_synapse =   3.0

	//[Mg] in mM
	float CMg = 1.2
	// per mM
	float eta = 0.2801
	// per V
	float gamma = 62

	float offset = - 0.01

	echo eta = {eta}

	eta = eta * {exp {- gamma * offset}}

	echo new eta = {eta}


	if (!({exists NMDA}))
		create synchan2 NMDA
	end

	setfield NMDA Ek {E_NMDA} tau2 {3e-3  / Q10_synapse} \
                                  tau1 {40e-3 / Q10_synapse} \
                                  gmax {G_NMDA}
	// use the following value for synaptic activation when TEST.g is run
	//                                  gmax {4.0 * G_NMDA}

        if (! {exists NMDA/Mg_BLOCK})
                create Mg_block NMDA/Mg_BLOCK
	end

        setfield NMDA/Mg_BLOCK CMg {CMg}  \
	    KMg_A {1/eta} \ \\ *({exp {EREST_ACT*gamma}})} \ 
            KMg_B {1.0/gamma}

end // make_NMDA_channels


function make_GABAB_channels

	/* GABA_B channel, using a dual exponential function with time constants of 80
	** and 40 msec as in Suarez, Koch and Douglas 1995 (J. Neurosci. 15,
	** 6700-1719; cat visual cortex).  
	** A more detailed model can be found in Otis, De Koninck and Mody 1993
	** (J. Physiol. 463, 391-407; rat hippocampal slices; this model uses 4th 
	** power exponential activation and dual exponential inactivation).
	** See also Benardo 1994 (J. Physiol. 476.2, 203-215; slice rat neocortex)
	** and Connors, Malenka and Silva 1988 (J. Physiol. 406, 443-468; slice
	** rat and cat visual cortex.
	*/

	float Q10_synapse =   3.0
 
	if (!({exists GABAB}))
                create synchan2 GABAB
	end
    	setfield GABAB Ek {E_GABAB} tau1 {0.080 / Q10_synapse} \
                                    tau2 {0.040 / Q10_synapse} \
                                    gmax {G_GABAB} frequency 0.0

end // make_GABAB_channels


  
function make_L5P_synchans
  
    echo making Purkinje synapse library...
    
    /* The conductance equations in this library are general and not
    **  specific to the Purkinje celxl */

	if ({!{exists /library}})
          	create neutral /library 
          	disable /library
   	end
        ce /library

	if ({!{exists L5P-notuft}})
          	create neutral L5P-notuft 
   	end
        ce L5P-notuft


    	make_GABAA_channels
    	make_AMPA_channels
    	make_NMDA_channels
    	make_GABAB_channels

end // make_L5P_synchans


make_L5P_synchans


