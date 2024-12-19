// genesis

// this is a copy of the channels of the granule cell model
// used also for the axons in Maex & De Schutter 2007

/*********************************************************************
**               The current equations themselves 
*********************************************************************/


float offset = 0.010

function make_Axon_chans_tab

    float temperature = 5
    int i, cdivs
    float zinf, ztau, c, dc, cmin, cmax
    float x, dx, y
    float a, b
    /* The folowing variables are temporary (not temperature) variables
	used to speed up computations */
    float mintau
    float tau
    float temp1
    float temp2


// Make library protoptypes *****

	if ({!{exists /library}})
          	create neutral /library 
          	disable /library
   	end

        ce /library

	if ({!{exists L5P}})
          	create neutral L5P 
   	end

        ce L5P


    /* Equations specific to the Granule cell, made by CP */

// Inactivating Na current */

	if ({!{exists Axon_InNa}})
	create tabchannel Axon_InNa
	setfield Axon_InNa Ek {ENa} Gbar 70 Ik 0 Gk 0 Xpower 3 Ypower 1  \
	    Zpower 0

	call Axon_InNa TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

	setfield Axon_InNa X_A->calc_mode 1 X_B->calc_mode 1

	call Axon_InNa TABCREATE Y {tab_xdivs} {tab_xmin} {tab_xmax}

	setfield Axon_InNa Y_A->calc_mode 1 Y_B->calc_mode 1

        call Axon_InNa TABREAD tabAxonInNa.dat

        call Axon_InNa TABFILL X 3000 0
        call Axon_InNa TABFILL Y 3000 0
	end


// Delayed Rectifier K current 

	if ({!{exists Axon_KDr}})
	create tabchannel Axon_KDr
	setfield Axon_KDr Ek {EK} Gbar 19 Ik 0 Gk 0 Xpower 4 Ypower 1  \
	    Zpower 0

	call Axon_KDr TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

	setfield Axon_KDr X_A->calc_mode 1 X_B->calc_mode 1

	call Axon_KDr TABCREATE Y {tab_xdivs} {tab_xmin} {tab_xmax}

	setfield Axon_KDr Y_A->calc_mode 1 Y_B->calc_mode 1

        call Axon_KDr TABREAD tabAxonKDr.dat

        call Axon_KDr TABFILL X 3000 0
        call Axon_KDr TABFILL Y 3000 0
	end

end
