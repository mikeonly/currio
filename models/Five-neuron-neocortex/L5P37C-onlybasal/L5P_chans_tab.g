//genesis 
//Tabchannel implementation of conductances based on Traub et al. (2003): Fast rhythmic bursting can be induced in layer 2/3 cortical neurons by enhancing persistent Na+ conductance or by blocking BK channels.

//include L5P_const.g
include ../L5P37C-onlybasal/Axon_chans_tab.g

	int i
	float x,dx,dx_h,XA,XB,Xinf,Xtau,YA,YB,Yinf,Ytau, ZA, ZB, Zinf, Ztau,dcai, cai
	dx = (tab_xmax-tab_xmin)/tab_xdivs  
	dcai = (cai_max-cai_min)/tab_xdivs

cd ../L5P37C-onlybasal/channels

// Make library prototypes *****

	if ({!{exists /library}})
          	create neutral /library 
          	disable /library
   	end

        ce /library

	if ({!{exists L5P-onlybasal}})
          	create neutral L5P-onlybasal 
   	end

        ce L5P-onlybasal


    /* Transient Na conductance*/
    	create tabchannel T03_NaF 
    	setfield T03_NaF Ek {ENa} Gbar {GNa} Ik 0 Gk 0 Xpower 3 Ypower 1 Zpower 0
    	call T03_NaF TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}     
    	call T03_NaF TABCREATE Y {tab_xdivs} {tab_xmin} {tab_xmax}

    	setfield T03_NaF X_A->calc_mode 1  X_B->calc_mode 1
    	setfield T03_NaF Y_A->calc_mode 1  Y_B->calc_mode 1

    	call T03_NaF TABREAD tabNaF.dat

    	call T03_NaF TABFILL X 3000 0
    	call T03_NaF TABFILL Y 3000 0


    /* Persistant Na conductance*/
    	create tabchannel T03_NaP 
    	setfield T03_NaP Ek {ENa} Gbar {GNa} Ik 0 Gk 0 Xpower 1 Ypower 0 Zpower 0
    	call T03_NaP TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

    	setfield T03_NaP X_A->calc_mode 1  X_B->calc_mode 1

    	call T03_NaP TABREAD tabNaP.dat
    	call T03_NaP TABFILL X 3000 0


    /* Delayed rectifier potassium conductance*/
    	create tabchannel T03_KDr 
    	setfield T03_KDr Ek {EK} Gbar {GK} Ik 0 Gk 0 Xpower 4 Ypower 0 Zpower 0
    	call T03_KDr TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

    	setfield T03_KDr X_A->calc_mode 1  X_B->calc_mode 1

    	call T03_KDr TABREAD tabKDr.dat
    	call T03_KDr TABFILL X 3000 0


    /* Transient A-type potassium conductance*/
    	create tabchannel T03_KA 
    	setfield T03_KA Ek {EK} Gbar {GK} Ik 0 Gk 0 Xpower 4 Ypower 1 Zpower 0
    	call T03_KA TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}
    	call T03_KA TABCREATE Y {tab_xdivs} {tab_xmin} {tab_xmax}

    	setfield T03_KA X_A->calc_mode 1  X_B->calc_mode 1
    	setfield T03_KA Y_A->calc_mode 1  Y_B->calc_mode 1

    	call T03_KA TABREAD tabKA.dat
    	call T03_KA TABFILL X 3000 0
    	call T03_KA TABFILL Y 3000 0


    /* K2-type potassium conductance*/
    	create tabchannel T03_K2 
    	setfield T03_K2 Ek {EK} Gbar {GK} Ik 0 Gk 0 Xpower 1 Ypower 1 Zpower 0
    	call T03_K2 TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}
    	call T03_K2 TABCREATE Y {tab_xdivs} {tab_xmin} {tab_xmax}

    	setfield T03_K2 X_A->calc_mode 1  X_B->calc_mode 1
    	setfield T03_K2 Y_A->calc_mode 1  Y_B->calc_mode 1

    	call T03_K2 TABREAD tabK2.dat
    	call T03_K2 TABFILL X 3000 0
    	call T03_K2 TABFILL Y 3000 0


    /* Low voltage threshold calcium conductance*/
    	create tabchannel T03_CaT 
    	setfield T03_CaT Ek {ECa} Gbar {GCa} Ik 0 Gk 0 Xpower 2 Ypower 1 Zpower 0
    	call T03_CaT TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}
    	call T03_CaT TABCREATE Y {tab_xdivs} {tab_xmin} {tab_xmax}

    	setfield T03_CaT X_A->calc_mode 1  X_B->calc_mode 1
    	setfield T03_CaT Y_A->calc_mode 1  Y_B->calc_mode 1

    	call T03_CaT TABREAD tabCaT.dat
    	call T03_CaT TABFILL X 3000 0
    	call T03_CaT TABFILL Y 3000 0


    /* Anomalous rectifier conductance H*/
    	create tabchannel T03_H 
    	setfield T03_H Ek {EH} Gbar {GH} Ik 0 Gk 0 Xpower 1 Ypower 0 Zpower 0
    	call T03_H TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

    	setfield T03_H X_A->calc_mode 1
    	setfield T03_H X_B->calc_mode 1

    	call T03_H TABREAD tabH.dat
    	call T03_H TABFILL X 3000 0


    /* KC-type calcium dependent potassium conductance*/
    	create tabchannel T03_KC 
    	setfield T03_KC Ek {EK} Gbar {GK} Ik 0 Gk 0 Xpower 1 Ypower 0 Zpower 1
    	call T03_KC TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}
    	call T03_KC TABCREATE Z {tab_xdivs} {cai_min} {cai_max}

    	setfield T03_KC X_A->calc_mode 1  X_B->calc_mode 1
    	setfield T03_KC Z_A->calc_mode 1  Z_B->calc_mode 1
    	setfield T03_KC instant {INSTANTZ}

    	call T03_KC TABREAD tabKC.dat
    	call T03_KC TABFILL X 3000 0
    	call T03_KC TABFILL Z 3000 0


    /* KM-type potassium conductance*/
    	create tabchannel T03_KM 
    	setfield T03_KM Ek {EK} Gbar {GK} Ik 0 Gk 0 Xpower 1 Ypower 0 Zpower 0
    	call T03_KM TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

    	setfield T03_KM X_A->calc_mode 1  X_B->calc_mode 1

    	call T03_KM TABREAD tabKM.dat
    	call T03_KM TABFILL X 3000 0


    /*Afterhypolarizing calcium dependent potassium conductance*/
    	create tabchannel T03_KAHP 
    	setfield T03_KAHP Ek {EK} Gbar {GK} Ik 0 Gk 0 Xpower 0 Ypower 0 Zpower 1
    	call T03_KAHP TABCREATE Z {tab_xdivs} {cai_min} {cai_max}

    	setfield T03_KAHP Z_A->calc_mode 1  Z_B->calc_mode 1

    	call T03_KAHP TABREAD tabKAHP.dat
    	call T03_KAHP TABFILL Z 3000 0


    /* High threshold L-type calcium conductance*/
    	create tabchannel T03_CaL 
    	setfield T03_CaL Ek {ECa} Gbar {GCa} Ik 0 Gk 0 Xpower 1 Ypower 0 Zpower 0
    	call T03_CaL TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

    	setfield T03_CaL X_A->calc_mode 1  X_B->calc_mode 1

    	call T03_CaL TABREAD tabCaL.dat
    	call T03_CaL TABFILL X 3000 0


    /* H-current channel based on Williams and Stuart (2000): 
       Site independence of EPSP time course is mediated by dendritic 
       Ih in neocortical pyramidal neurons. */


    	float tab_xmin = -0.1
    	float tab_xmax = 0.05
    	int tab_xdivs = 149

    	int i
    	float x,dx,XA,XB,YA,YB,YAA,YAB
    	dx = (1e3 * (tab_xmax-tab_xmin))/tab_xdivs  //mV, tables are in V
    	echo {dx}

    // only used for proto channels
    	float G_WS_H = 1
    	float EH = -0.043 

    	create tabchannel WS_H 
    	setfield WS_H Ek {EH} Gbar {G_WS_H} Ik 0 Gk 0 Xpower 1 Ypower 0 Zpower 0
    	call WS_H TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

    	setfield WS_H X_A->calc_mode 1  X_B->calc_mode 1

    	call WS_H TABREAD tabWS_H.dat
    	call WS_H TABFILL X 3000 0

make_Axon_chans_tab

cd ..
