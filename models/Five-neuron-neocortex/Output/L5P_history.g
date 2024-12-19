// genesis

// include L5P_const.g


//    str label = "test"

str Excitatory_fibres_history_filename   = {filename} @ "E_"   @ {label} @ ".history"
str Inhibitory_fibres_history_filename   = {filename} @ "I_"   @ {label} @ ".history"

str L5P_history_filename   = {filename} @ "L5P_"   @ {label} @ ".history"



int i
 int size_message_list

   if (!({exists /output/history}))
          create neutral /output/history
   end

   ce /output/history

/*
      echo initializing {Excitatory_fibres_history_filename}
      create spikehistory Excitatory_fibres.history
      setfield Excitatory_fibres.history ident_toggle 0 \ // index
                                    filename {Excitatory_fibres_history_filename} \
                                    initialize 1 leave_open 1 flush 1
      addmsg /Excitatory_fibres/FF/fibre[] /output/history/Excitatory_fibres.history SPIKESAVE
      addmsg /Excitatory_fibres/FBintra/fibre[] /output/history/Excitatory_fibres.history SPIKESAVE
      addmsg /Excitatory_fibres/FBinter/fibre[] /output/history/Excitatory_fibres.history SPIKESAVE
*/


// Inhibitory fibers

/*
      echo initializing {Inhibitory_fibres_history_filename}
      create spikehistory Inhibitory_fibres.history
      setfield Inhibitory_fibres.history ident_toggle 0 \ // index
                                    filename {Inhibitory_fibres_history_filename} \
                                    initialize 1 leave_open 1 flush 1
      addmsg /Inhibitory_fibres/FF/fibre[] /output/history/Inhibitory_fibres.history SPIKESAVE
      addmsg /Inhibitory_fibres/FBintra/fibre[] /output/history/Inhibitory_fibres.history SPIKESAVE
      addmsg /Inhibitory_fibres/FBinter/fibre[] /output/history/Inhibitory_fibres.history SPIKESAVE
*/

// L5P cells

      	echo initializing {L5P_history_filename}
      	create spikehistory L5P.history
      	setfield ^ ident_toggle 0 \ // index
                                   filename {L5P_history_filename} \
                                   initialize 1 leave_open 1 flush 1

	function add_history (pathname)

		str pathname

      		addmsg {pathname}/soma/spike /output/history/L5P.history SPIKESAVE

		create spikegen {pathname}/axon[19]/spike 
		setfield ^  thresh -0.01 abs_refract 0.0015 output_amp 1
   		addmsg {pathname}/axon[1]  ^  INPUT Vm

      		addmsg ^ /output/history/L5P.history SPIKESAVE

        end


//      addmsg /L5Ponlybasal/soma/spike /output/history/L5P.history SPIKESAVE
//      addmsg /L5Pnotuft/soma/spike /output/history/L5P.history SPIKESAVE




