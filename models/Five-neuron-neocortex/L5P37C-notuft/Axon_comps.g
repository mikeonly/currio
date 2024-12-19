//genesis

// copied from Golg_comp_soma_dend_axon.g
 
// include L5P_const+axon+syn.g

function make_Axon_comps

/* separate function so we can have local variables */

	float len, dia, surf


	/* make cylindrical axon prototype */
        len = 1
        dia = 1
        surf = len*dia*{PI}


	if (!({exists /library/L5P-notuft/axon}))
		create compartment /library/L5P-notuft/axon
	end

        ce /library/L5P-notuft


	setfield axon Cm {{CM}*surf} Ra {4.0*{RA}*len/(dia*dia*{PI})}  \ 
	    Em {EREST_ACT} Vm {RESET_ACT} Rm {{RMs}/surf} inject 0.0  \
	    dia {dia} len {len}

	// Now copy the channels and set maximal conductances */

        if (!({exists axon/InNa}))
        	copy Axon_InNa axon/InNa
	        addmsg axon axon/InNa VOLTAGE Vm
	        addmsg axon/InNa axon CHANNEL Gk Ek
	end
        setfield axon/InNa Gbar {{GInNa_a}*surf*1} // 1.2}   // 1.2

        if (!({exists axon/KDr}))
        	copy Axon_KDr axon/KDr
	        addmsg axon axon/KDr VOLTAGE Vm
	        addmsg axon/KDr axon CHANNEL Gk Ek
	end
        setfield axon/KDr Gbar {{GKDr_a}*surf*3}   // 2.8 // 2.7 // 1.5

end

