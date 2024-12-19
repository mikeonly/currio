// genesis

// this is a copy of the channels of the granule cell model
// used also for the axons in Maex & De Schutter 2007

/*********************************************************************
**               The current equations themselves 
*********************************************************************/


float offset = 0.010 // 0.0 // 0.010

function make_Axon_chans

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

    /* Equations specific to the Granule cell, made by CP */
    /* Inactivating Na current */

	create tabchannel Axon_InNa
	setfield Axon_InNa Ek {ENa} Gbar 70 Ik 0 Gk 0 Xpower 3 Ypower 1  \
	    Zpower 0

	call Axon_InNa TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

	x = {tab_xmin} - {offset}
	dx = ({tab_xmax} - {tab_xmin})/{tab_xdivs}
	mintau = (1e-3*0.05)
	temp1 = (1e3*1.5)

        openfile Axon_InNa_a_max_37.test w
        openfile Axon_InNa_a_tau_37.test w

	for (i = 0; i <= ({tab_xdivs}); i = i + 1)
		temp2 = ((x) + 39e-3) // instead of ((x) + 39e-3)
		a = (temp1)*({exp {0.081e3*(temp2)}})
		b = (temp1)*({exp {-0.066e3*(temp2)}})
		tau = 1/(a + b)

		if (tau  < (mintau))		// tau_min is 0.05*5e-3 

			setfield Axon_InNa X_A->table[{i}] {mintau / temperature}
		else
			setfield Axon_InNa X_A->table[{i}] {tau / temperature}
		end
		//Xinf
		setfield Axon_InNa X_B->table[{i}] {a*tau}

                writefile Axon_InNa_a_max_37.test {x} {getfield Axon_InNa X_B->table[{i}]}
                writefile Axon_InNa_a_tau_37.test {x} {getfield Axon_InNa X_A->table[{i}]}

		x = x + dx
	end
	tweaktau Axon_InNa X
	setfield Axon_InNa X_A->calc_mode 1 X_B->calc_mode 1

        closefile Axon_InNa_a_max_37.test
        closefile Axon_InNa_a_tau_37.test

	call Axon_InNa TABCREATE Y {tab_xdivs} {tab_xmin} {tab_xmax}
	x = {tab_xmin} - {offset}
	mintau = (1e-3*0.225)
	temp1 = (1e3*0.12)

        openfile Axon_InNa_i_max_37.test w
        openfile Axon_InNa_i_tau_37.test w

// trying to increase threshold

	for (i = 0; i <= ({tab_xdivs}); i = i + 1)
		temp2 = (0.089e3)*(((x) + 50e-3)) // instead of (0.089e3)*(((x) + 50e-3))
		a = (temp1)*({exp {-(temp2)}})
		b = (temp1)*({exp {temp2}})
		tau = 1/(a + b)

		if (tau < mintau)		// tau_min is 0.225*5e-3 

			setfield Axon_InNa Y_A->table[{i}] {mintau / temperature}
		else
			//Xinf
			setfield Axon_InNa Y_A->table[{i}] {tau / temperature}
		end
		setfield Axon_InNa Y_B->table[{i}] {a*tau}

                writefile Axon_InNa_i_max_37.test {x} {getfield Axon_InNa Y_B->table[{i}]}
                writefile Axon_InNa_i_tau_37.test {x} {getfield Axon_InNa Y_A->table[{i}]}

		x = x + dx

	end
	tweaktau Axon_InNa Y
	setfield Axon_InNa Y_A->calc_mode 1 Y_B->calc_mode 1

        closefile Axon_InNa_i_max_37.test
        closefile Axon_InNa_i_tau_37.test

    call Axon_InNa TABSAVE tabAxonInNa.dat

    call Axon_InNa TABFILL X 3000 0
    call Axon_InNa TABFILL Y 3000 0


// Delayed Rectifier K current 

	create tabchannel Axon_KDr
	setfield Axon_KDr Ek {EK} Gbar 19 Ik 0 Gk 0 Xpower 4 Ypower 1  \
	    Zpower 0

	call Axon_KDr TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}
	x = {tab_xmin} - {offset}
	dx = ({tab_xmax} - {tab_xmin})/{tab_xdivs}
	temp1 = 1e3*0.17

        openfile Axon_Kdr_a_max.test w
        openfile Axon_Kdr_a_tau.test w

	for (i = 0; i <= ({tab_xdivs}); i = i + 1)
		temp2 = x + 38e-3
		a = temp1*({exp {0.073e3*(temp2)}})
		b = temp1*({exp {-0.018e3*(temp2)}})

		setfield Axon_KDr X_A->table[{i}] {temperature * a}
		setfield Axon_KDr X_B->table[{i}] {temperature * (a + b)}

                writefile Axon_Kdr_a_tau.test {x} {1 / (temperature * (a + b))}
                writefile Axon_Kdr_a_max.test {x} {a / (a + b)}

		x = x + dx
	end
	setfield Axon_KDr X_A->calc_mode 1 X_B->calc_mode 1

        closefile Axon_Kdr_a_max.test
        closefile Axon_Kdr_a_tau.test

	call Axon_KDr TABCREATE Y {tab_xdivs} {tab_xmin} {tab_xmax}
	x = {tab_xmin} - {offset}

        openfile Axon_KDr_i_max.test w
        openfile Axon_KDr_i_tau.test w

	for (i = 0; i <= ({tab_xdivs}); i = i + 1)
		if (x > -0.046)  
                          a = 0.76
                else      a = 1e3*(0.0007 + 0.000065*({exp {-0.08e3*(x + 46e-3)}}))
	        end
        	b = 1e3*(110e-5)/(1 + ({exp {-0.0807e3*(x + 44e-3)}}))

		setfield Axon_KDr Y_A->table[{i}] {temperature * a}
		setfield Axon_KDr Y_B->table[{i}] {temperature * (a + b)}

		writefile Axon_KDr_i_tau.test {x} {1 / (temperature * (a + b))}
                writefile Axon_KDr_i_max.test {x} {a / (a + b)}

                x = x + dx
	end
	setfield Axon_KDr Y_A->calc_mode 1 Y_B->calc_mode 1

        closefile Axon_KDr_i_tau.test
        closefile Axon_KDr_i_max.test

    call Axon_KDr TABSAVE tabAxonKDr.dat

    call Axon_KDr TABFILL X 3000 0
    call Axon_KDr TABFILL Y 3000 0

end
