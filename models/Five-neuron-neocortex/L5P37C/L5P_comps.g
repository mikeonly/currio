//genesis - script for generating prototype compartments

create compartment soma
setfield soma Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia 1 len 0 // 1

   copy T03_NaF soma/NaF
   addmsg soma soma/NaF VOLTAGE Vm
   addmsg soma/NaF soma CHANNEL Gk Ek
   setfield soma/NaF Gbar {GNaF_s}

   copy T03_NaP soma/NaP
   addmsg soma soma/NaP VOLTAGE Vm
   addmsg soma/NaP soma CHANNEL Gk Ek
   setfield soma/NaP Gbar {GNaP_s}

   copy T03_KDr soma/KDr
   addmsg soma soma/KDr VOLTAGE Vm
   addmsg soma/KDr soma CHANNEL Gk Ek
   setfield soma/KDr Gbar {GKDr_s}

   copy T03_KA soma/KA
   addmsg soma soma/KA VOLTAGE Vm
   addmsg soma/KA soma CHANNEL Gk Ek
   setfield soma/KA Gbar {GKA_s}

   copy T03_KC soma/KC
   addmsg soma soma/KC VOLTAGE Vm
   addmsg soma/KC soma CHANNEL Gk Ek
   setfield soma/KC Gbar {GKC_s}

   copy T03_KAHP soma/KAHP
   addmsg soma soma/KAHP VOLTAGE Vm
   addmsg soma/KAHP soma CHANNEL Gk Ek
   setfield soma/KAHP Gbar {GKAHP_s}

   copy T03_K2 soma/K2
   addmsg soma soma/K2 VOLTAGE Vm
   addmsg soma/K2 soma CHANNEL Gk Ek
   setfield soma/K2 Gbar {GK2_s}

   copy T03_KM soma/KM
   addmsg soma soma/KM VOLTAGE Vm
   addmsg soma/KM soma CHANNEL Gk Ek
   setfield soma/KM Gbar {GKM_s}

   copy T03_CaT soma/CaT
   addmsg soma soma/CaT VOLTAGE Vm
   addmsg soma/CaT soma CHANNEL Gk Ek
   setfield soma/CaT Gbar {GCaT_s}

   copy T03_CaL soma/CaL
   addmsg soma soma/CaL VOLTAGE Vm
   addmsg soma/CaL soma CHANNEL Gk Ek
   setfield soma/CaL Gbar {GCaL_s}

   copy WS_H soma/H
   addmsg soma soma/H VOLTAGE Vm
   addmsg soma/H soma CHANNEL Gk Ek
   setfield soma/H Gbar {GH_s}

   create Ca_concen soma/Ca_pool
   setfield soma/Ca_pool tau {CaTau_s} B {B} Ca_base 0 thick 2.0e-9
   addmsg soma/CaT soma/Ca_pool I_Ca Ik
   addmsg soma/CaL soma/Ca_pool I_Ca Ik
   addmsg soma/Ca_pool soma/KC CONCEN Ca
   addmsg soma/Ca_pool soma/KAHP CONCEN Ca

   create synchan soma/Glu
   setfield soma/Glu tau1 1.0e-4 tau2 15.0e-3 gmax {G_Glu} Ek 0.0
   addmsg soma soma/Glu VOLTAGE Vm
   addmsg soma/Glu soma CHANNEL Gk Ek
   

create compartment Dend_Bas
setfield Dend_Bas Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia 1 len 1

copy T03_NaF Dend_Bas/NaF
   addmsg Dend_Bas Dend_Bas/NaF VOLTAGE Vm
   addmsg Dend_Bas/NaF Dend_Bas CHANNEL Gk Ek
   setfield Dend_Bas/NaF Gbar {GNaF_bd}

   copy T03_NaP Dend_Bas/NaP
   addmsg Dend_Bas Dend_Bas/NaP VOLTAGE Vm
   addmsg Dend_Bas/NaP Dend_Bas CHANNEL Gk Ek
   setfield Dend_Bas/NaP Gbar {GNaP_bd}

   copy T03_KDr Dend_Bas/KDr
   addmsg Dend_Bas Dend_Bas/KDr VOLTAGE Vm
   addmsg Dend_Bas/KDr Dend_Bas CHANNEL Gk Ek
   setfield Dend_Bas/KDr Gbar {GKDr_bd}

   copy T03_KA Dend_Bas/KA
   addmsg Dend_Bas Dend_Bas/KA VOLTAGE Vm
   addmsg Dend_Bas/KA Dend_Bas CHANNEL Gk Ek
   setfield Dend_Bas/KA Gbar {GKA_bd}

   copy T03_KC Dend_Bas/KC
   addmsg Dend_Bas Dend_Bas/KC VOLTAGE Vm
   addmsg Dend_Bas/KC Dend_Bas CHANNEL Gk Ek
   setfield Dend_Bas/KC Gbar {GKC_bd}

   copy T03_KAHP Dend_Bas/KAHP
   addmsg Dend_Bas Dend_Bas/KAHP VOLTAGE Vm
   addmsg Dend_Bas/KAHP Dend_Bas CHANNEL Gk Ek
   setfield Dend_Bas/KAHP Gbar {GKAHP_bd}

   copy T03_K2 Dend_Bas/K2
   addmsg Dend_Bas Dend_Bas/K2 VOLTAGE Vm
   addmsg Dend_Bas/K2 Dend_Bas CHANNEL Gk Ek
   setfield Dend_Bas/K2 Gbar {GK2_bd}

   copy T03_KM Dend_Bas/KM
   addmsg Dend_Bas Dend_Bas/KM VOLTAGE Vm
   addmsg Dend_Bas/KM Dend_Bas CHANNEL Gk Ek
   setfield Dend_Bas/KM Gbar {GKM_bd}

   copy T03_CaT Dend_Bas/CaT
   addmsg Dend_Bas Dend_Bas/CaT VOLTAGE Vm
   addmsg Dend_Bas/CaT Dend_Bas CHANNEL Gk Ek
   setfield Dend_Bas/CaT Gbar {GCaT_bd}

   copy T03_CaL Dend_Bas/CaL
   addmsg Dend_Bas Dend_Bas/CaL VOLTAGE Vm
   addmsg Dend_Bas/CaL Dend_Bas CHANNEL Gk Ek
   setfield Dend_Bas/CaL Gbar {GCaL_bd}

   copy WS_H Dend_Bas/H
   addmsg Dend_Bas Dend_Bas/H VOLTAGE Vm
   addmsg Dend_Bas/H Dend_Bas CHANNEL Gk Ek
   setfield Dend_Bas/H Gbar {GH_d}

   create Ca_concen Dend_Bas/Ca_pool
   setfield Dend_Bas/Ca_pool tau {CaTau_d} B {B} Ca_base 0 thick 2.0e-9
   addmsg Dend_Bas/CaT Dend_Bas/Ca_pool I_Ca Ik
   addmsg Dend_Bas/CaL Dend_Bas/Ca_pool I_Ca Ik
   addmsg Dend_Bas/Ca_pool Dend_Bas/KC CONCEN Ca
   addmsg Dend_Bas/Ca_pool Dend_Bas/KAHP CONCEN Ca

   create synchan Dend_Bas/Glu
   setfield Dend_Bas/Glu tau1 1.0e-4 tau2 15.0e-3 gmax {G_Glu} Ek 0.00
   addmsg Dend_Bas Dend_Bas/Glu VOLTAGE Vm
   addmsg Dend_Bas/Glu Dend_Bas CHANNEL Gk Ek

create compartment Dend_Ap_shaft
setfield Dend_Ap_shaft Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia 1 len 1

   copy T03_NaF Dend_Ap_shaft/NaF
   addmsg Dend_Ap_shaft Dend_Ap_shaft/NaF VOLTAGE Vm
   addmsg Dend_Ap_shaft/NaF Dend_Ap_shaft CHANNEL Gk Ek
   setfield Dend_Ap_shaft/NaF Gbar {GNaF_shaft}

   copy T03_NaP Dend_Ap_shaft/NaP
   addmsg Dend_Ap_shaft Dend_Ap_shaft/NaP VOLTAGE Vm
   addmsg Dend_Ap_shaft/NaP Dend_Ap_shaft CHANNEL Gk Ek
   setfield Dend_Ap_shaft/NaP Gbar {GNaP_shaft}

   copy T03_KDr Dend_Ap_shaft/KDr
   addmsg Dend_Ap_shaft Dend_Ap_shaft/KDr VOLTAGE Vm
   addmsg Dend_Ap_shaft/KDr Dend_Ap_shaft CHANNEL Gk Ek
   setfield Dend_Ap_shaft/KDr Gbar {GKDr_shaft}

   copy T03_KA Dend_Ap_shaft/KA
   addmsg Dend_Ap_shaft Dend_Ap_shaft/KA VOLTAGE Vm
   addmsg Dend_Ap_shaft/KA Dend_Ap_shaft CHANNEL Gk Ek
   setfield Dend_Ap_shaft/KA Gbar {GKA_shaft}

   copy T03_KC Dend_Ap_shaft/KC
   addmsg Dend_Ap_shaft Dend_Ap_shaft/KC VOLTAGE Vm
   addmsg Dend_Ap_shaft/KC Dend_Ap_shaft CHANNEL Gk Ek
   setfield Dend_Ap_shaft/KC Gbar {GKC_shaft}

   copy T03_KAHP Dend_Ap_shaft/KAHP
   addmsg Dend_Ap_shaft Dend_Ap_shaft/KAHP VOLTAGE Vm
   addmsg Dend_Ap_shaft/KAHP Dend_Ap_shaft CHANNEL Gk Ek
   setfield Dend_Ap_shaft/KAHP Gbar {GKAHP_shaft}

   copy T03_K2 Dend_Ap_shaft/K2
   addmsg Dend_Ap_shaft Dend_Ap_shaft/K2 VOLTAGE Vm
   addmsg Dend_Ap_shaft/K2 Dend_Ap_shaft CHANNEL Gk Ek
   setfield Dend_Ap_shaft/K2 Gbar {GK2_shaft}

   copy T03_KM Dend_Ap_shaft/KM
   addmsg Dend_Ap_shaft Dend_Ap_shaft/KM VOLTAGE Vm
   addmsg Dend_Ap_shaft/KM Dend_Ap_shaft CHANNEL Gk Ek
   setfield Dend_Ap_shaft/KM Gbar {GKM_shaft}

   copy T03_CaT Dend_Ap_shaft/CaT
   addmsg Dend_Ap_shaft Dend_Ap_shaft/CaT VOLTAGE Vm
   addmsg Dend_Ap_shaft/CaT Dend_Ap_shaft CHANNEL Gk Ek
   setfield Dend_Ap_shaft/CaT Gbar {GCaT_shaft}

   copy T03_CaL Dend_Ap_shaft/CaL
   addmsg Dend_Ap_shaft Dend_Ap_shaft/CaL VOLTAGE Vm
   addmsg Dend_Ap_shaft/CaL Dend_Ap_shaft CHANNEL Gk Ek
   setfield Dend_Ap_shaft/CaL Gbar {GCaL_shaft}

   copy WS_H Dend_Ap_shaft/H
   addmsg Dend_Ap_shaft Dend_Ap_shaft/H VOLTAGE Vm
   addmsg Dend_Ap_shaft/H Dend_Ap_shaft CHANNEL Gk Ek
   setfield Dend_Ap_shaft/H Gbar {GH_d}

   create Ca_concen Dend_Ap_shaft/Ca_pool
   setfield Dend_Ap_shaft/Ca_pool tau {CaTau_d} B {B} Ca_base 0 thick 2.0e-9
   addmsg Dend_Ap_shaft/CaT Dend_Ap_shaft/Ca_pool I_Ca Ik
   addmsg Dend_Ap_shaft/CaL Dend_Ap_shaft/Ca_pool I_Ca Ik
   addmsg Dend_Ap_shaft/Ca_pool Dend_Ap_shaft/KC CONCEN Ca
   addmsg Dend_Ap_shaft/Ca_pool Dend_Ap_shaft/KAHP CONCEN Ca

   create synchan Dend_Ap_shaft/Glu
   setfield Dend_Ap_shaft/Glu tau1 1.0e-4 tau2 15.0e-3 gmax {G_Glu} Ek 0.0
   addmsg Dend_Ap_shaft Dend_Ap_shaft/Glu VOLTAGE Vm
   addmsg Dend_Ap_shaft/Glu Dend_Ap_shaft CHANNEL Gk Ek

create compartment Dend_Ap
setfield Dend_Ap Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia 1 len 1

   copy T03_NaF Dend_Ap/NaF
   addmsg Dend_Ap Dend_Ap/NaF VOLTAGE Vm
   addmsg Dend_Ap/NaF Dend_Ap CHANNEL Gk Ek
   setfield Dend_Ap/NaF Gbar {GNaF_pad}

   copy T03_NaP Dend_Ap/NaP
   addmsg Dend_Ap Dend_Ap/NaP VOLTAGE Vm
   addmsg Dend_Ap/NaP Dend_Ap CHANNEL Gk Ek
   setfield Dend_Ap/NaP Gbar {GNaP_pad}

   copy T03_KDr Dend_Ap/KDr
   addmsg Dend_Ap Dend_Ap/KDr VOLTAGE Vm
   addmsg Dend_Ap/KDr Dend_Ap CHANNEL Gk Ek
   setfield Dend_Ap/KDr Gbar {GKDr_pad}

   copy T03_KA Dend_Ap/KA
   addmsg Dend_Ap Dend_Ap/KA VOLTAGE Vm
   addmsg Dend_Ap/KA Dend_Ap CHANNEL Gk Ek
   setfield Dend_Ap/KA Gbar {GKA_pad}

   copy T03_KC Dend_Ap/KC
   addmsg Dend_Ap Dend_Ap/KC VOLTAGE Vm
   addmsg Dend_Ap/KC Dend_Ap CHANNEL Gk Ek
   setfield Dend_Ap/KC Gbar {GKC_pad}

   copy T03_KAHP Dend_Ap/KAHP
   addmsg Dend_Ap Dend_Ap/KAHP VOLTAGE Vm
   addmsg Dend_Ap/KAHP Dend_Ap CHANNEL Gk Ek
   setfield Dend_Ap/KAHP Gbar {GKAHP_pad}

   copy T03_K2 Dend_Ap/K2
   addmsg Dend_Ap Dend_Ap/K2 VOLTAGE Vm
   addmsg Dend_Ap/K2 Dend_Ap CHANNEL Gk Ek
   setfield Dend_Ap/K2 Gbar {GK2_pad}

   copy T03_KM Dend_Ap/KM
   addmsg Dend_Ap Dend_Ap/KM VOLTAGE Vm
   addmsg Dend_Ap/KM Dend_Ap CHANNEL Gk Ek
   setfield Dend_Ap/KM Gbar {GKM_pad}

   copy T03_CaT Dend_Ap/CaT
   addmsg Dend_Ap Dend_Ap/CaT VOLTAGE Vm
   addmsg Dend_Ap/CaT Dend_Ap CHANNEL Gk Ek
   setfield Dend_Ap/CaT Gbar {GCaT_pad}

   copy T03_CaL Dend_Ap/CaL
   addmsg Dend_Ap Dend_Ap/CaL VOLTAGE Vm
   addmsg Dend_Ap/CaL Dend_Ap CHANNEL Gk Ek
   setfield Dend_Ap/CaL Gbar {GCaL_pad}

   copy WS_H Dend_Ap/H
   addmsg Dend_Ap Dend_Ap/H VOLTAGE Vm
   addmsg Dend_Ap/H Dend_Ap CHANNEL Gk Ek
   setfield Dend_Ap/H Gbar {GH_d}

   create Ca_concen Dend_Ap/Ca_pool
   setfield Dend_Ap/Ca_pool tau {CaTau_d} B {B} Ca_base 0 thick 2.0e-9
   addmsg Dend_Ap/CaT Dend_Ap/Ca_pool I_Ca Ik
   addmsg Dend_Ap/CaL Dend_Ap/Ca_pool I_Ca Ik
   addmsg Dend_Ap/Ca_pool Dend_Ap/KC CONCEN Ca
   addmsg Dend_Ap/Ca_pool Dend_Ap/KAHP CONCEN Ca

   create synchan Dend_Ap/Glu
   setfield Dend_Ap/Glu tau1 1.0e-4 tau2 15.0e-3 gmax {G_Glu} Ek 0.0
   addmsg Dend_Ap Dend_Ap/Glu VOLTAGE Vm
   addmsg Dend_Ap/Glu Dend_Ap CHANNEL Gk Ek

create compartment Dend_Ap_Med
setfield Dend_Ap_Med Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia 1 len 1

   copy T03_NaF Dend_Ap_Med/NaF
   addmsg Dend_Ap_Med Dend_Ap_Med/NaF VOLTAGE Vm
   addmsg Dend_Ap_Med/NaF Dend_Ap_Med CHANNEL Gk Ek
   setfield Dend_Ap_Med/NaF Gbar {GNaF_mad}

   copy T03_NaP Dend_Ap_Med/NaP
   addmsg Dend_Ap_Med Dend_Ap_Med/NaP VOLTAGE Vm
   addmsg Dend_Ap_Med/NaP Dend_Ap_Med CHANNEL Gk Ek
   setfield Dend_Ap_Med/NaP Gbar {GNaP_mad}

   copy T03_KDr Dend_Ap_Med/KDr
   addmsg Dend_Ap_Med Dend_Ap_Med/KDr VOLTAGE Vm
   addmsg Dend_Ap_Med/KDr Dend_Ap_Med CHANNEL Gk Ek
   setfield Dend_Ap_Med/KDr Gbar {GKDr_mad}

   copy T03_KA Dend_Ap_Med/KA
   addmsg Dend_Ap_Med Dend_Ap_Med/KA VOLTAGE Vm
   addmsg Dend_Ap_Med/KA Dend_Ap_Med CHANNEL Gk Ek
   setfield Dend_Ap_Med/KA Gbar {GKA_mad}

   copy T03_KC Dend_Ap_Med/KC
   addmsg Dend_Ap_Med Dend_Ap_Med/KC VOLTAGE Vm
   addmsg Dend_Ap_Med/KC Dend_Ap_Med CHANNEL Gk Ek
   setfield Dend_Ap_Med/KC Gbar {GKC_mad}

   copy T03_KAHP Dend_Ap_Med/KAHP
   addmsg Dend_Ap_Med Dend_Ap_Med/KAHP VOLTAGE Vm
   addmsg Dend_Ap_Med/KAHP Dend_Ap_Med CHANNEL Gk Ek
   setfield Dend_Ap_Med/KAHP Gbar {GKAHP_mad}

   copy T03_K2 Dend_Ap_Med/K2
   addmsg Dend_Ap_Med Dend_Ap_Med/K2 VOLTAGE Vm
   addmsg Dend_Ap_Med/K2 Dend_Ap_Med CHANNEL Gk Ek
   setfield Dend_Ap_Med/K2 Gbar {GK2_mad}

   copy T03_KM Dend_Ap_Med/KM
   addmsg Dend_Ap_Med Dend_Ap_Med/KM VOLTAGE Vm
   addmsg Dend_Ap_Med/KM Dend_Ap_Med CHANNEL Gk Ek
   setfield Dend_Ap_Med/KM Gbar {GKM_mad}

   copy T03_CaT Dend_Ap_Med/CaT
   addmsg Dend_Ap_Med Dend_Ap_Med/CaT VOLTAGE Vm
   addmsg Dend_Ap_Med/CaT Dend_Ap_Med CHANNEL Gk Ek
   setfield Dend_Ap_Med/CaT Gbar {GCaT_mad}

   copy T03_CaL Dend_Ap_Med/CaL
   addmsg Dend_Ap_Med Dend_Ap_Med/CaL VOLTAGE Vm
   addmsg Dend_Ap_Med/CaL Dend_Ap_Med CHANNEL Gk Ek
   setfield Dend_Ap_Med/CaL Gbar {GCaL_mad}

   copy WS_H Dend_Ap_Med/H
   addmsg Dend_Ap_Med Dend_Ap_Med/H VOLTAGE Vm
   addmsg Dend_Ap_Med/H Dend_Ap_Med CHANNEL Gk Ek
   setfield Dend_Ap_Med/H Gbar {GH_d}

   create Ca_concen Dend_Ap_Med/Ca_pool
   setfield Dend_Ap_Med/Ca_pool tau {CaTau_d} B {B} Ca_base 0 thick 2.0e-9
   addmsg Dend_Ap_Med/CaT Dend_Ap_Med/Ca_pool I_Ca Ik
   addmsg Dend_Ap_Med/CaL Dend_Ap_Med/Ca_pool I_Ca Ik
   addmsg Dend_Ap_Med/Ca_pool Dend_Ap_Med/KC CONCEN Ca
   addmsg Dend_Ap_Med/Ca_pool Dend_Ap_Med/KAHP CONCEN Ca

   create synchan Dend_Ap_Med/Glu
   setfield Dend_Ap_Med/Glu tau1 1.0e-4 tau2 15.0e-3 gmax {G_Glu} Ek 0.06
   addmsg Dend_Ap_Med Dend_Ap_Med/Glu VOLTAGE Vm
   addmsg Dend_Ap_Med/Glu Dend_Ap_Med CHANNEL Gk Ek

create compartment Dend_Ap_Obl
setfield Dend_Ap_Obl Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia 1 len 1

copy T03_NaF Dend_Ap_Obl/NaF
   addmsg Dend_Ap_Obl Dend_Ap_Obl/NaF VOLTAGE Vm
   addmsg Dend_Ap_Obl/NaF Dend_Ap_Obl CHANNEL Gk Ek
   setfield Dend_Ap_Obl/NaF Gbar {GNaF_pad}

   copy T03_NaP Dend_Ap_Obl/NaP
   addmsg Dend_Ap_Obl Dend_Ap_Obl/NaP VOLTAGE Vm
   addmsg Dend_Ap_Obl/NaP Dend_Ap_Obl CHANNEL Gk Ek
   setfield Dend_Ap_Obl/NaP Gbar {GNaP_pad}

   copy T03_KDr Dend_Ap_Obl/KDr
   addmsg Dend_Ap_Obl Dend_Ap_Obl/KDr VOLTAGE Vm
   addmsg Dend_Ap_Obl/KDr Dend_Ap_Obl CHANNEL Gk Ek
   setfield Dend_Ap_Obl/KDr Gbar {GKDr_pad}

   copy T03_KA Dend_Ap_Obl/KA
   addmsg Dend_Ap_Obl Dend_Ap_Obl/KA VOLTAGE Vm
   addmsg Dend_Ap_Obl/KA Dend_Ap_Obl CHANNEL Gk Ek
   setfield Dend_Ap_Obl/KA Gbar {GKA_pad}

   copy T03_KC Dend_Ap_Obl/KC
   addmsg Dend_Ap_Obl Dend_Ap_Obl/KC VOLTAGE Vm
   addmsg Dend_Ap_Obl/KC Dend_Ap_Obl CHANNEL Gk Ek
   setfield Dend_Ap_Obl/KC Gbar {GKC_pad}

   copy T03_KAHP Dend_Ap_Obl/KAHP
   addmsg Dend_Ap_Obl Dend_Ap_Obl/KAHP VOLTAGE Vm
   addmsg Dend_Ap_Obl/KAHP Dend_Ap_Obl CHANNEL Gk Ek
   setfield Dend_Ap_Obl/KAHP Gbar {GKAHP_pad}

   copy T03_K2 Dend_Ap_Obl/K2
   addmsg Dend_Ap_Obl Dend_Ap_Obl/K2 VOLTAGE Vm
   addmsg Dend_Ap_Obl/K2 Dend_Ap_Obl CHANNEL Gk Ek
   setfield Dend_Ap_Obl/K2 Gbar {GK2_pad}

   copy T03_KM Dend_Ap_Obl/KM
   addmsg Dend_Ap_Obl Dend_Ap_Obl/KM VOLTAGE Vm
   addmsg Dend_Ap_Obl/KM Dend_Ap_Obl CHANNEL Gk Ek
   setfield Dend_Ap_Obl/KM Gbar {GKM_pad}

   copy T03_CaT Dend_Ap_Obl/CaT
   addmsg Dend_Ap_Obl Dend_Ap_Obl/CaT VOLTAGE Vm
   addmsg Dend_Ap_Obl/CaT Dend_Ap_Obl CHANNEL Gk Ek
   setfield Dend_Ap_Obl/CaT Gbar {GCaT_pad}

   copy T03_CaL Dend_Ap_Obl/CaL
   addmsg Dend_Ap_Obl Dend_Ap_Obl/CaL VOLTAGE Vm
   addmsg Dend_Ap_Obl/CaL Dend_Ap_Obl CHANNEL Gk Ek
   setfield Dend_Ap_Obl/CaL Gbar {GCaL_pad}

   copy WS_H Dend_Ap_Obl/H
   addmsg Dend_Ap_Obl Dend_Ap_Obl/H VOLTAGE Vm
   addmsg Dend_Ap_Obl/H Dend_Ap_Obl CHANNEL Gk Ek
   setfield Dend_Ap_Obl/H Gbar {GH_d}

   create Ca_concen Dend_Ap_Obl/Ca_pool
   setfield Dend_Ap_Obl/Ca_pool tau {CaTau_d} B 5.2e5 Ca_base 0 thick 2.0e-9
   addmsg Dend_Ap_Obl/CaT Dend_Ap_Obl/Ca_pool I_Ca Ik
   addmsg Dend_Ap_Obl/CaL Dend_Ap_Obl/Ca_pool I_Ca Ik
   addmsg Dend_Ap_Obl/Ca_pool Dend_Ap_Obl/KC CONCEN Ca
   addmsg Dend_Ap_Obl/Ca_pool Dend_Ap_Obl/KAHP CONCEN Ca

   create synchan Dend_Ap_Obl/Glu
   setfield Dend_Ap_Obl/Glu tau1 1.0e-4 tau2 15.0e-3 gmax {G_Glu} Ek 0.0
   addmsg Dend_Ap_Obl Dend_Ap_Obl/Glu VOLTAGE Vm
   addmsg Dend_Ap_Obl/Glu Dend_Ap_Obl CHANNEL Gk Ek

create compartment Dend_Ap_Dis
setfield Dend_Ap_Dis Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia 1 len 1

   copy T03_NaF Dend_Ap_Dis/NaF
   addmsg Dend_Ap_Dis Dend_Ap_Dis/NaF VOLTAGE Vm
   addmsg Dend_Ap_Dis/NaF Dend_Ap_Dis CHANNEL Gk Ek
   setfield Dend_Ap_Dis/NaF Gbar {GNaF_dd}

   copy T03_NaP Dend_Ap_Dis/NaP
   addmsg Dend_Ap_Dis Dend_Ap_Dis/NaP VOLTAGE Vm
   addmsg Dend_Ap_Dis/NaP Dend_Ap_Dis CHANNEL Gk Ek
   setfield Dend_Ap_Dis/NaP Gbar {GNaP_dd}

   copy T03_KA Dend_Ap_Dis/KA
   addmsg Dend_Ap_Dis Dend_Ap_Dis/KA VOLTAGE Vm
   addmsg Dend_Ap_Dis/KA Dend_Ap_Dis CHANNEL Gk Ek
   setfield Dend_Ap_Dis/KA Gbar {GKA_dd}

   copy T03_KAHP Dend_Ap_Dis/KAHP
   addmsg Dend_Ap_Dis Dend_Ap_Dis/KAHP VOLTAGE Vm
   addmsg Dend_Ap_Dis/KAHP Dend_Ap_Dis CHANNEL Gk Ek
   setfield Dend_Ap_Dis/KAHP Gbar {GKAHP_dd}

   copy T03_K2 Dend_Ap_Dis/K2
   addmsg Dend_Ap_Dis Dend_Ap_Dis/K2 VOLTAGE Vm
   addmsg Dend_Ap_Dis/K2 Dend_Ap_Dis CHANNEL Gk Ek
   setfield Dend_Ap_Dis/K2 Gbar {GK2_dd}

   copy T03_KM Dend_Ap_Dis/KM
   addmsg Dend_Ap_Dis Dend_Ap_Dis/KM VOLTAGE Vm
   addmsg Dend_Ap_Dis/KM Dend_Ap_Dis CHANNEL Gk Ek
   setfield Dend_Ap_Dis/KM Gbar {GKM_dd}

   copy T03_CaT Dend_Ap_Dis/CaT
   addmsg Dend_Ap_Dis Dend_Ap_Dis/CaT VOLTAGE Vm
   addmsg Dend_Ap_Dis/CaT Dend_Ap_Dis CHANNEL Gk Ek
   setfield Dend_Ap_Dis/CaT Gbar {GCaT_dd}

   copy T03_CaL Dend_Ap_Dis/CaL
   addmsg Dend_Ap_Dis Dend_Ap_Dis/CaL VOLTAGE Vm
   addmsg Dend_Ap_Dis/CaL Dend_Ap_Dis CHANNEL Gk Ek
   setfield Dend_Ap_Dis/CaL Gbar {GCaL_dd}

   copy WS_H Dend_Ap_Dis/H
   addmsg Dend_Ap_Dis Dend_Ap_Dis/H VOLTAGE Vm
   addmsg Dend_Ap_Dis/H Dend_Ap_Dis CHANNEL Gk Ek
   setfield Dend_Ap_Dis/H Gbar {GH_d}

   create Ca_concen Dend_Ap_Dis/Ca_pool
   setfield Dend_Ap_Dis/Ca_pool tau {CaTau_d} B {B} Ca_base 0 thick 2.0e-9
   addmsg Dend_Ap_Dis/CaT Dend_Ap_Dis/Ca_pool I_Ca Ik
   addmsg Dend_Ap_Dis/CaL Dend_Ap_Dis/Ca_pool I_Ca Ik
   addmsg Dend_Ap_Dis/Ca_pool Dend_Ap_Dis/KAHP CONCEN Ca

   create synchan Dend_Ap_Dis/Glu
   setfield Dend_Ap_Dis/Glu tau1 1.0e-4 tau2 150e-3 gmax {G_Glu} Ek 0.0
   addmsg Dend_Ap_Dis Dend_Ap_Dis/Glu VOLTAGE Vm
   addmsg Dend_Ap_Dis/Glu Dend_Ap_Dis CHANNEL Gk Ek







