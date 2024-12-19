//genesis

// This scripts regulates the temporal modulation of the fibres.
// Feedforward input modulated by Harsch-Robinson.
// Intracolumnar feedback input regulated by membrane potential of L5P.
// Intercolumner feedback: to be implemented later.



/*************** Feedforward input  *******************/


// feedforward input from the Harsch-Robinson external stochastic process


// kept this in main script
// include Harsch-Robinson_modulation.g
// Harsch_Robinson_modulation 20 0.05


addmsg /HR_modulation/RC/diffamp  /Excitatory_fibres/FF/FF_diffamp[] GAIN output
addmsg /HR_modulation/RC/diffamp  /Inhibitory_fibres/FF/FF_diffamp[] GAIN output




/********** Intracolumnar feedback input  **************/

// feedback input from L5P
// As feedback signal, we use the continuous soma membrane potential instead the 
// discrete action potential timing.
// Diffamps are used to covert Vm to values positive (set plus field) and to change their amplitude
// (set gain field).

// It is expected that this intracolumnar feedback will suffice to induce oscillations.
// The delay of this feedback can be set by the delay field of the synapses.
// The position of the feedback synapses can be tuned via Firing_rate_profile.g



// Excitatory

   ce /L5P
   create diffamp soma/E_diffamp
   setfield soma/E_diffamp plus 0.08  minus 0 \
                         saturation 10e10 \
                         gain 10
   addmsg soma soma/E_diffamp PLUS Vm
//   addmsg /L5P/solve soma/E_diffamp PLUS {findsolvefield /L5P/solve /L5P/soma Vm}


addmsg /L5P/soma/E_diffamp /Excitatory_fibres/FBintra/FBintra_diffamp[] GAIN output

    addmsg soma/E_diffamp      /output/{asc_name} SAVE output
 

// Inhibitory

   ce /L5P
   create diffamp soma/I_diffamp
   setfield soma/I_diffamp plus 0.08  minus 0 \
                         saturation 10e10 \
                         gain 10
   addmsg soma soma/I_diffamp PLUS Vm
//   addmsg /L5P/solve soma/I_diffamp PLUS {findsolvefield /L5P/solve /L5P/soma Vm}

   addmsg soma/I_diffamp /Inhibitory_fibres/FBintra/FBintra_diffamp[] GAIN output

    addmsg soma/I_diffamp      /output/{asc_name} SAVE output
 

/********** Intercolumnar feedback input  **************/

// Note that strictly speaking this input can be of the feedforward type !




