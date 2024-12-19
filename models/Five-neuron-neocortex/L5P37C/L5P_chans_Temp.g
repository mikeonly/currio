//genesis 
//Tabchannel implementation of conductances based on Traub et al. (2003): Fast rhythmic bursting can be induced in layer 2/3 cortical neurons by enhancing persistent Na+ conductance or by blocking BK channels.

include L5P_const.g

include Axon_chans.g


int i
float x,dx,dx_h,XA,XB,Xinf,Xtau,YA,YB,Yinf,Ytau, ZA, ZB, Zinf, Ztau,dcai, cai
dx = (tab_xmax-tab_xmin)/tab_xdivs  
dcai = (cai_max-cai_min)/tab_xdivs

cd channels // all tables (.dat) and curves (.test) stored in channels subdirectory 

    /* Transient Na conductance*/
    create tabchannel T03_NaF 
    setfield T03_NaF Ek {ENa} Gbar {GNa} Ik 0 Gk 0 Xpower 3 Ypower 1 Zpower 0
    call T03_NaF TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}     
    call T03_NaF TABCREATE Y {tab_xdivs} {tab_xmin} {tab_xmax}

    openfile NaF_a_max.test w
    openfile NaF_a_tau.test w
    openfile NaF_i_max.test w
    openfile NaF_i_tau.test w

    x = {tab_xmin} 
    for (i = 0 ; i <= {tab_xdivs} ; i = i + 1)    

        if ( x <= -0.032 )
           Xtau = 0.0125e-3 + (0.007e-3 * {exp {(x + 0.030)/0.008}})
        else
           Xtau = 0.01e-3 + (0.0725e-3 * {exp {(-x - 0.030)/0.008}})
        end
 
        Xinf = 1/(1 + {exp {(-x - 0.038)/0.008}})
 
        Ytau = 0.75e-3 + (5.75e-3/(1 + {exp {(x + 0.0335)/0.01}}))

        Yinf = 1/(1 + {exp {(x + 0.0574)/0.007}})

        setfield T03_NaF X_A->table[{i}] {{Xtau} * {Temp_corr_factor}}
        setfield T03_NaF X_B->table[{i}] {Xinf}
        setfield T03_NaF Y_A->table[{i}] {{Ytau} * {Temp_corr_factor}}
        setfield T03_NaF Y_B->table[{i}] {Yinf}

        writefile NaF_a_max.test {x} {getfield T03_NaF X_B->table[{i}]}
        writefile NaF_a_tau.test {x} {getfield T03_NaF X_A->table[{i}]}
        writefile NaF_i_max.test {x} {getfield T03_NaF Y_B->table[{i}]}
        writefile NaF_i_tau.test {x} {getfield T03_NaF Y_A->table[{i}]}

        x = x + dx
    end

    closefile NaF_a_max.test 
    closefile NaF_a_tau.test 
    closefile NaF_i_max.test 
    closefile NaF_i_tau.test 

    setfield T03_NaF X_A->calc_mode 1  X_B->calc_mode 1
    setfield T03_NaF Y_A->calc_mode 1  Y_B->calc_mode 1

    tweaktau T03_NaF X
    tweaktau T03_NaF Y

    call T03_NaF TABSAVE tabNaF.dat

    call T03_NaF TABFILL X 3000 0
    call T03_NaF TABFILL Y 3000 0



    /* Persistant Na conductance*/
    create tabchannel T03_NaP 
    setfield T03_NaP Ek {ENa} Gbar {GNa} Ik 0 Gk 0 Xpower 1 Ypower 0 Zpower 0
    call T03_NaP TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

    openfile NaP_a_max.test w
    openfile NaP_a_tau.test w

    x = {tab_xmin} 
    for (i = 0 ; i <= {tab_xdivs} ; i = i + 1)    

        if ( x <= -0.027 )
           Xtau = 0.025e-3 + (0.014e-3 * {exp {(x + 0.027)/0.01}})
        else
           Xtau = 0.02e-3 + (0.145e-3 * {exp {(-x - 0.027)/0.01}})
        end
 
        Xinf = 1/(1 + {exp {(-x - 0.035)/0.01}})

        setfield T03_NaP X_A->table[{i}] {{Xtau} * {Temp_corr_factor}}
        setfield T03_NaP X_B->table[{i}] {Xinf}

        writefile NaP_a_max.test {x} {getfield T03_NaP X_B->table[{i}]}
        writefile NaP_a_tau.test {x} {getfield T03_NaP X_A->table[{i}]}

        x = x + dx
    end

    closefile NaP_a_max.test 
    closefile NaP_a_tau.test 

    setfield T03_NaP X_A->calc_mode 1  X_B->calc_mode 1

    tweaktau T03_NaP X

    call T03_NaP TABSAVE tabNaP.dat

    call T03_NaP TABFILL X 3000 0



    /* Delayed rectifier potassium conductance*/
    create tabchannel T03_KDr 
    setfield T03_KDr Ek {EK} Gbar {GK} Ik 0 Gk 0 Xpower 4 Ypower 0 Zpower 0
    call T03_KDr TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

    openfile KDr_a_max.test w
    openfile KDr_a_tau.test w

    x = {tab_xmin} 
    for (i = 0 ; i <= {tab_xdivs} ; i = i + 1)    

        if ( x <= -0.010 )
           Xtau = 0.75e-3 + (13.05e-3 * {exp {(x + 0.01)/0.01}})
        else
           Xtau = 0.75e-3 + (13.05e-3 * {exp {(-x - 0.01)/0.01}})
        end
 
        Xinf = 1/(1 + {exp {(-x - 0.0295)/0.01}})

        setfield T03_KDr X_A->table[{i}] {{Xtau} * {Temp_corr_factor}}
        setfield T03_KDr X_B->table[{i}] {Xinf}

        writefile KDr_a_max.test {x} {getfield T03_KDr X_B->table[{i}]}
        writefile KDr_a_tau.test {x} {getfield T03_KDr X_A->table[{i}]}

        x = x + dx
    end

    closefile KDr_a_max.test 
    closefile KDr_a_tau.test 

    setfield T03_KDr X_A->calc_mode 1  X_B->calc_mode 1

    tweaktau T03_KDr X

    call T03_KDr TABSAVE tabKDr.dat

    call T03_KDr TABFILL X 3000 0


    /* Transient A-type potassium conductance*/
    create tabchannel T03_KA 
    setfield T03_KA Ek {EK} Gbar {GK} Ik 0 Gk 0 Xpower 4 Ypower 1 Zpower 0
    call T03_KA TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}
    call T03_KA TABCREATE Y {tab_xdivs} {tab_xmin} {tab_xmax}

    openfile KA_a_max.test w
    openfile KA_a_tau.test w
    openfile KA_i_max.test w
    openfile KA_i_tau.test w

    x = {tab_xmin} 
    for (i = 0 ; i <= {tab_xdivs} ; i = i + 1)    

       Xtau = 0.185e-3 + (0.5e-3/({exp {(x + 0.0358)/0.0197}} + {exp {(-x - 0.0797)/0.0127}}))
 
       Xinf = 1/(1 + {exp {(-x - 0.060)/0.0085}})

       if ( x <= -0.063 )
           Ytau = 0.5e-3/({exp {(x + 0.046)/0.005}} + {exp {(-x - 0.238)/0.0375}})
       else
            Ytau= 9.5e-3
       end

       Yinf = 1/(1 + {exp {(x + 0.078)/0.006}})

       setfield T03_KA X_A->table[{i}] {{Xtau} * {Temp_corr_factor}}
       setfield T03_KA X_B->table[{i}] {Xinf}
       setfield T03_KA Y_A->table[{i}] {{Ytau} * {Temp_corr_factor}}
       setfield T03_KA Y_B->table[{i}] {Yinf}

       writefile KA_a_max.test {x} {getfield T03_KA X_B->table[{i}]}
       writefile KA_a_tau.test {x} {getfield T03_KA X_A->table[{i}]}
       writefile KA_i_max.test {x} {getfield T03_KA Y_B->table[{i}]}
       writefile KA_i_tau.test {x} {getfield T03_KA Y_A->table[{i}]}

       x = x + dx
    end

    closefile KA_a_max.test 
    closefile KA_a_tau.test 
    closefile KA_i_max.test 
    closefile KA_i_tau.test 

    setfield T03_KA X_A->calc_mode 1  X_B->calc_mode 1
    setfield T03_KA Y_A->calc_mode 1  Y_B->calc_mode 1

    tweaktau T03_KA X
    tweaktau T03_KA Y

    call T03_KA TABSAVE tabKA.dat

    call T03_KA TABFILL X 3000 0
    call T03_KA TABFILL Y 3000 0


    /* K2-type potassium conductance*/
    create tabchannel T03_K2 
    setfield T03_K2 Ek {EK} Gbar {GK} Ik 0 Gk 0 Xpower 1 Ypower 1 Zpower 0
    call T03_K2 TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}
    call T03_K2 TABCREATE Y {tab_xdivs} {tab_xmin} {tab_xmax}

    openfile K2_a_max.test w
    openfile K2_a_tau.test w
    openfile K2_i_max.test w
    openfile K2_i_tau.test w

    x = {tab_xmin} 
    for (i = 0 ; i <= {tab_xdivs} ; i = i + 1)    
       
       Xtau = 4.95e-3 + (0.5e-3/({exp {(x + 0.081)/0.0256}} + {exp {(-x - 0.132)/0.018}}))
 
       Xinf = 1/(1 + {exp {(-x - 0.010)/0.017}})

       Ytau = 60e-3 + (0.5e-3/({exp {(x + 0.00133)/0.2}} + {exp {(-x - 0.130)/0.0071}}))

       Yinf = 1/(1 + {exp {(x + 0.058)/0.0106}})

       setfield T03_K2 X_A->table[{i}] {{Xtau} * {Temp_corr_factor}}
       setfield T03_K2 X_B->table[{i}] {Xinf}
       setfield T03_K2 Y_A->table[{i}] {{Ytau} * {Temp_corr_factor}}
       setfield T03_K2 Y_B->table[{i}] {Yinf}

       writefile K2_a_max.test {x} {getfield T03_K2 X_B->table[{i}]}
       writefile K2_a_tau.test {x} {getfield T03_K2 X_A->table[{i}]}
       writefile K2_i_max.test {x} {getfield T03_K2 Y_B->table[{i}]}
       writefile K2_i_tau.test {x} {getfield T03_K2 Y_A->table[{i}]}
 
      x = x + dx
    end

    closefile K2_a_max.test 
    closefile K2_a_tau.test 
    closefile K2_i_max.test 
    closefile K2_i_tau.test 

    setfield T03_K2 X_A->calc_mode 1  X_B->calc_mode 1
    setfield T03_K2 Y_A->calc_mode 1  Y_B->calc_mode 1

    tweaktau T03_K2 X
    tweaktau T03_K2 Y

    call T03_K2 TABSAVE tabK2.dat

    call T03_K2 TABFILL X 3000 0
    call T03_K2 TABFILL Y 3000 0



    /* Low voltage threshold calcium conductance*/
    create tabchannel T03_CaT 
    setfield T03_CaT Ek {ECa} Gbar {GCa} Ik 0 Gk 0 Xpower 2 Ypower 1 Zpower 0
    call T03_CaT TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}
    call T03_CaT TABCREATE Y {tab_xdivs} {tab_xmin} {tab_xmax}

    openfile CaT_a_max.test w
    openfile CaT_a_tau.test w
    openfile CaT_i_max.test w
    openfile CaT_i_tau.test w

    x = {tab_xmin} 
    for (i = 0 ; i <= {tab_xdivs} ; i = i + 1)    

        Xtau = 0.204e-3 + (0.333e-3/({exp {(x + 0.0158)/0.0182}} + {exp {(-x - 0.131)/0.0167}}))
 
        Xinf = 1/(1 + {exp {(-x - 0.056)/0.0062}})

        if ( x <= -0.081 )
           Ytau = 0.333e-3 * {exp {(x + 0.466)/0.0666}}
        else
           Ytau = 9.32e-3 + (0.333e-3 * {exp {(-x - 0.021)/0.0105}})
        end

        Yinf = 1/(1 + {exp {(x + 0.085)/0.004}})

        setfield T03_CaT X_A->table[{i}] {{Xtau} * {Temp_corr_factor}}
        setfield T03_CaT X_B->table[{i}] {Xinf}
        setfield T03_CaT Y_A->table[{i}] {{Ytau} * {Temp_corr_factor}}
        setfield T03_CaT Y_B->table[{i}] {Yinf}
  
        writefile CaT_a_max.test {x} {getfield T03_CaT X_B->table[{i}]}
        writefile CaT_a_tau.test {x} {getfield T03_CaT X_A->table[{i}]}
        writefile CaT_i_max.test {x} {getfield T03_CaT Y_B->table[{i}]}
        writefile CaT_i_tau.test {x} {getfield T03_CaT Y_A->table[{i}]}
 
        x = x + dx
    end

    closefile CaT_a_max.test 
    closefile CaT_a_tau.test 
    closefile CaT_i_max.test 
    closefile CaT_i_tau.test 

    setfield T03_CaT X_A->calc_mode 1  X_B->calc_mode 1
    setfield T03_CaT Y_A->calc_mode 1  Y_B->calc_mode 1

    tweaktau T03_CaT X
    tweaktau T03_CaT Y

    call T03_CaT TABSAVE tabCaT.dat

    call T03_CaT TABFILL X 3000 0
    call T03_CaT TABFILL Y 3000 0


    /* Anomalous rectifier conductance H*/
    create tabchannel T03_H 
    setfield T03_H Ek {EH} Gbar {GH} Ik 0 Gk 0 Xpower 1 Ypower 0 Zpower 0
    call T03_H TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

    openfile H_a_max.test w
    openfile H_a_tau.test w

    x = {tab_xmin} 
    for (i = 0 ; i <= {tab_xdivs} ; i = i + 1)    

        Xtau = 1e-3/({exp {(-14.6 - 86*x)}} + {exp {(-1.87 - 70*x)}})

        Xinf = 1/(1 + {exp {(x + 0.075)/0.0055}})

        setfield T03_H X_A->table[{i}] {{Xtau} * {Temp_corr_factor}}
        setfield T03_H X_B->table[{i}] {Xinf}

        writefile H_a_max.test {x} {getfield T03_H X_B->table[{i}]}
        writefile H_a_tau.test {x} {getfield T03_H X_A->table[{i}]}

       x = x + dx
    end

    closefile H_a_max.test 
    closefile H_a_tau.test 

    setfield T03_H X_A->calc_mode 1  
    setfield T03_H X_B->calc_mode 1

    tweaktau T03_H X

    call T03_H TABSAVE tabH.dat

    call T03_H TABFILL X 3000 0


/* KC-type calcium dependent potassium conductance*/
    create tabchannel T03_KC 
    setfield T03_KC Ek {EK} Gbar {GK} Ik 0 Gk 0 Xpower 1 Ypower 0 Zpower 1
    call T03_KC TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}
    call T03_KC TABCREATE Z {tab_xdivs} {cai_min} {cai_max}

    openfile KC_a_max.test w
    openfile KC_a_tau.test w
    openfile KC_C_max.test w
    openfile KC_C_tau.test w

    x = {tab_xmin} 
    cai = {cai_min}
    for (i = 0 ; i <= {tab_xdivs} ; i = i + 1)    
       
        if ( x <= -0.010 )
          XA = 0.053*{exp {((x + 0.05)/0.011) - ((x + 0.0535)/0.027)}}
        else
          XA = 2*{exp {(-x - 0.0535)/0.027}}
        end

        if ( x <= -0.010 )
          XB = (2*{exp {(-x - 0.0535)/0.027}}) - {XA}
        else
          XB = 0
        end

        if ( cai <= 250 )
          Zinf = 0.004 * cai
        else
          Zinf = 1.0
        end

        Xtau = 1.0e-3 / ({XA} + {XB})
        Xinf = {XA} / ({XA} + {XB})

        setfield T03_KC X_A->table[{i}] {{Xtau} * {Temp_corr_factor}}
        setfield T03_KC X_B->table[{i}] {Xinf}
        setfield T03_KC Z_A->table[{i}] {Zinf}  // is this right ?
        setfield T03_KC Z_B->table[{i}] 1.0
  
        writefile KC_a_max.test {x} {getfield T03_KC X_B->table[{i}]}
        writefile KC_a_tau.test {x} {getfield T03_KC X_A->table[{i}]}
        writefile KC_C_max.test {x} {getfield T03_KC Z_B->table[{i}]}
        writefile KC_C_tau.test {x} {getfield T03_KC Z_A->table[{i}]}

        x = x + dx
        cai = cai + dcai
    end

    closefile KC_a_max.test 
    closefile KC_a_tau.test 
    closefile KC_C_max.test 
    closefile KC_C_tau.test 

    setfield T03_KC X_A->calc_mode 1  X_B->calc_mode 1
    setfield T03_KC Z_A->calc_mode 1  Z_B->calc_mode 1

    setfield T03_KC instant {INSTANTZ}

// hence variable set to A/B instead of solving ODE

    tweaktau T03_KC X

    call T03_KC TABSAVE tabKC.dat

    call T03_KC TABFILL X 3000 0
    call T03_KC TABFILL Z 3000 0



    /* KM-type potassium conductance*/
    create tabchannel T03_KM 
    setfield T03_KM Ek {EK} Gbar {GK} Ik 0 Gk 0 Xpower 1 Ypower 0 Zpower 0
    call T03_KM TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

    openfile KM_a_max.test w
    openfile KM_a_tau.test w

    x = {tab_xmin} 
    for (i = 0 ; i <= {tab_xdivs} ; i = i + 1)    

        XA = 0.02/(1 + {exp {(-x - 0.02)/0.005}})

        XB = 0.01*{exp {(-x - 0.043)/0.018}}

        Xtau = 0.75e-3 / ({XA} + {XB})
        Xinf = {XA} / ({XA} + {XB})

        setfield T03_KM X_A->table[{i}] {{Xtau} * {Temp_corr_factor}}
        setfield T03_KM X_B->table[{i}] {Xinf}

        writefile KM_a_max.test {x} {getfield T03_KM X_B->table[{i}]}
        writefile KM_a_tau.test {x} {getfield T03_KM X_A->table[{i}]}

      x = x + dx
    end

    closefile KM_a_max.test 
    closefile KM_a_tau.test 

    setfield T03_KM X_A->calc_mode 1  X_B->calc_mode 1

    tweaktau T03_KM X

    call T03_KM TABSAVE tabKM.dat

    call T03_KM TABFILL X 3000 0



/*Afterhypolarizing calcium dependent potassium conductance*/
    create tabchannel T03_KAHP 
    setfield T03_KAHP Ek {EK} Gbar {GK} Ik 0 Gk 0 Xpower 0 Ypower 0 Zpower 1
    call T03_KAHP TABCREATE Z {tab_xdivs} {cai_min} {cai_max}

    openfile KAHP_C_max.test w
    openfile KAHP_C_tau.test w

    cai = {cai_min}
    for (i = 0 ; i <= {tab_xdivs} ; i = i + 1)    
       

        if ( cai <= 100 )
          ZA = 0.0001 * cai
        else
          ZA = 0.01
        end

        ZB = 0.01

        Ztau = 1.0e-3 / ({ZA} + {ZB})
        Zinf = {ZA} / ({ZA} + {ZB})

        setfield T03_KAHP Z_A->table[{i}] {{Ztau} * {Temp_corr_factor}}
        setfield T03_KAHP Z_B->table[{i}] {Zinf}
  
        writefile KAHP_C_max.test {x} {getfield T03_KAHP Z_B->table[{i}]}
        writefile KAHP_C_tau.test {x} {getfield T03_KAHP Z_A->table[{i}]}

        cai = cai + dcai
    end

    closefile KAHP_C_max.test 
    closefile KAHP_C_tau.test 

    setfield T03_KAHP Z_A->calc_mode 1  Z_B->calc_mode 1

    tweaktau T03_KAHP Z

    call T03_KAHP TABSAVE tabKAHP.dat

    call T03_KAHP TABFILL Z 3000 0


    /* High threshold L-type calcium conductance*/
    create tabchannel T03_CaL 
    setfield T03_CaL Ek {ECa} Gbar {GCa} Ik 0 Gk 0 Xpower 1 Ypower 0 Zpower 0
    call T03_CaL TABCREATE X {tab_xdivs} {tab_xmin} {tab_xmax}

    openfile CaL_a_max.test w
    openfile CaL_a_tau.test w

    x = {tab_xmin} 
    for (i = 0 ; i <= {tab_xdivs} ; i = i + 1)    

        XA = 1.6/(1 + {exp {-72*(x - 0.005)}})

        XB = (0.02e3*(x + 0.0089))/({exp {(x + 0.0089)/0.005}} - 1)

        Xtau = 1.0e-3 / ({XA} + {XB})
        Xinf = {XA} / ({XA} + {XB})

        setfield T03_CaL X_A->table[{i}] {{Xtau} * {Temp_corr_factor}}
        setfield T03_CaL X_B->table[{i}] {Xinf}

        writefile CaL_a_max.test {x} {getfield T03_CaL X_B->table[{i}]}
        writefile CaL_a_tau.test {x} {getfield T03_CaL X_A->table[{i}]}

       x = x + dx
    end

    closefile CaL_a_max.test 
    closefile CaL_a_tau.test 

    setfield T03_CaL X_A->calc_mode 1  X_B->calc_mode 1

    tweaktau T03_CaL X

    call T03_CaL TABSAVE tabCaL.dat

    call T03_CaL TABFILL X 3000 0



/* H-current channel based on Williams and Stuart (2000): 
Site independence of EPSP time course is mediated by dendritic Ih in neocortical pyramidal neurons. */


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

    openfile WS_H_a_max.test w
    openfile WS_H_a_tau.test w

    x = 1e3*{tab_xmin}
    for (i = 0 ; i <= {tab_xdivs} ; i = i + 1)    
          XB = 1 / (1 + {exp {((-85.0 - x) / -6.1)}})

//tau defined below and above -82 mV


// I am not sure how to correct this with Temp_corr_factor
// hence I substituted Temp for t_sim in the formula

        if (x <= -71)
           XA = ({exp {(0.025 * x) + 6.68}}) / (1.0e3 * (Q10**{({Temp}-34) / 10}))
        else
           XA = 5*({exp {(-0.027 * x) + 1.69}}) / (1.0e3 * (Q10**{({Temp} - 34) / 10}))
        end

        setfield WS_H X_A->table[{i}] {XA}
        setfield WS_H X_B->table[{i}] {XB}

        writefile WS_H_a_max.test {x} {getfield WS_H X_B->table[{i}]}
        writefile WS_H_a_tau.test {x} {getfield WS_H X_A->table[{i}]}

        x = x + dx
    end

    closefile WS_H_a_max.test 
    closefile WS_H_a_tau.test 

    setfield WS_H X_A->calc_mode 1  X_B->calc_mode 1

    tweaktau WS_H X

    call WS_H TABSAVE tabWS_H.dat

    call WS_H TABFILL X 3000 0

// the axonal channels

make_Axon_chans

cd ..

