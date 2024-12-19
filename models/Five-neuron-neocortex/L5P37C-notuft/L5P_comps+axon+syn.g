//genesis - script for generating prototype compartments

// this is the file of Jonas from NeuronDB
// supplemented by Reinoud Maex in June 2007 with
// an axon borrowed from Maex & De Schutter 2007
// synaptic channels borrowed from Solinas et al. 2006 (AMPA, GABAA) 
// and from Maex & De Schutter 1998 (NMDA, GABAB) 

include ../L5P37C-notuft/Axon_comps.g

// include L5P_synchan.g // already included in main script

	float surf // the compartment's surface area
	float dia, len

	float attenuation_factor = 0.05 // 0 // 0.05 // 0.1 // 0.3 //  0 // 0.3 // 0.05 // 0.1 // 0.3 // 0.4  // 0.5


	if ({!{exists /library}})
          	create neutral /library 
          	disable /library
   	end
        ce /library

	if ({!{exists L5P-notuft}})
          	create neutral L5P-notuft 
   	end
        ce L5P-notuft


	create compartment soma
	dia = 1
	len = 0 
	setfield soma Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia {dia} len {len} // 1
// when len != 0 the compartment is considered cylindrical
	surf = {dia * dia * PI}

   	copy T03_NaF soma/NaF
   	addmsg soma soma/NaF VOLTAGE Vm
   	addmsg soma/NaF soma CHANNEL Gk Ek
   	setfield soma/NaF Gbar {GNaF_s * surf}

   	copy T03_NaP soma/NaP
   	addmsg soma soma/NaP VOLTAGE Vm
   	addmsg soma/NaP soma CHANNEL Gk Ek
   	setfield soma/NaP Gbar 0 // {GNaP_s * surf}

   	copy T03_KDr soma/KDr
   	addmsg soma soma/KDr VOLTAGE Vm
   	addmsg soma/KDr soma CHANNEL Gk Ek
   	setfield soma/KDr Gbar {GKDr_s * surf}

   	copy T03_KA soma/KA
   	addmsg soma soma/KA VOLTAGE Vm
   	addmsg soma/KA soma CHANNEL Gk Ek
   	setfield soma/KA Gbar {GKA_s * surf}

   	copy T03_KC soma/KC
   	addmsg soma soma/KC VOLTAGE Vm
   	addmsg soma/KC soma CHANNEL Gk Ek
   	setfield soma/KC Gbar {GKC_s * surf}

   	copy T03_KAHP soma/KAHP
   	addmsg soma soma/KAHP VOLTAGE Vm
   	addmsg soma/KAHP soma CHANNEL Gk Ek
   	setfield soma/KAHP Gbar {GKAHP_s * surf} 

   	copy T03_K2 soma/K2
   	addmsg soma soma/K2 VOLTAGE Vm
   	addmsg soma/K2 soma CHANNEL Gk Ek
   	setfield soma/K2 Gbar {GK2_s * surf}

   	copy T03_KM soma/KM
   	addmsg soma soma/KM VOLTAGE Vm
   	addmsg soma/KM soma CHANNEL Gk Ek
   	setfield soma/KM Gbar {GKM_s * surf}

   	copy T03_CaT soma/CaT
   	addmsg soma soma/CaT VOLTAGE Vm
   	addmsg soma/CaT soma CHANNEL Gk Ek
   	setfield soma/CaT Gbar {GCaT_s * surf * attenuation_factor}

   	copy T03_CaL soma/CaL
   	addmsg soma soma/CaL VOLTAGE Vm
   	addmsg soma/CaL soma CHANNEL Gk Ek
   	setfield soma/CaL Gbar {GCaL_s * surf * 0.5} // 1.0}

   	copy WS_H soma/H
   	addmsg soma soma/H VOLTAGE Vm
   	addmsg soma/H soma CHANNEL Gk Ek
   	setfield soma/H Gbar {GH_s * surf}

   	create Ca_concen soma/Ca_pool
   	setfield soma/Ca_pool tau {CaTau_s} B {B} Ca_base 0 thick 2.0e-9
   	addmsg soma/CaT soma/Ca_pool I_Ca Ik
   	addmsg soma/CaL soma/Ca_pool I_Ca Ik
   	addmsg soma/Ca_pool soma/KC CONCEN Ca
   	addmsg soma/Ca_pool soma/KAHP CONCEN Ca

//   create synchan soma/Glu
//   setfield soma/Glu tau1 1.0e-4 tau2 15.0e-3 gmax {G_Glu} Ek 0.0
//   addmsg soma soma/Glu VOLTAGE Vm
//   addmsg soma/Glu soma CHANNEL Gk Ek

  
   	copy AMPA soma/AMPA
   	addmsg soma/AMPA soma CHANNEL Gk Ek
   	addmsg soma soma/AMPA VOLTAGE Vm

/*
   copy NMDA soma/NMDA
   addmsg  soma/NMDA soma/NMDA/Mg_BLOCK CHANNEL Gk Ek
   addmsg  soma/NMDA/Mg_BLOCK soma CHANNEL Gk Ek
   addmsg soma/NMDA soma CHANNEL Gk Ek
   addmsg soma soma/NMDA VOLTAGE Vm
   setfield soma/NMDA gmax {G_NMDA * surf} 
*/

   	copy GABA soma/GABA
   	addmsg soma/GABA soma CHANNEL Gk Ek
   	addmsg soma soma/GABA VOLTAGE Vm
   	setfield soma/GABA gmax {G_GABA * surf} 
   echo G_GABA = {G_GABA}

/*
   copy GABAB soma/GABAB
   addmsg soma/GABAB soma CHANNEL Gk Ek
   addmsg soma soma/GABAB VOLTAGE Vm
   setfield soma/GABAB gmax {G_GABAB * surf} 
*/


	create compartment Dend_Bas
	dia = 1
	len = 1
	setfield Dend_Bas Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia {dia} len {len}
	surf = {dia * len * PI}

	copy T03_NaF Dend_Bas/NaF
   	addmsg Dend_Bas Dend_Bas/NaF VOLTAGE Vm
   	addmsg Dend_Bas/NaF Dend_Bas CHANNEL Gk Ek
   	setfield Dend_Bas/NaF Gbar {GNaF_bd * surf * attenuation_factor}

   	copy T03_NaP Dend_Bas/NaP
   	addmsg Dend_Bas Dend_Bas/NaP VOLTAGE Vm
   	addmsg Dend_Bas/NaP Dend_Bas CHANNEL Gk Ek
   	setfield Dend_Bas/NaP Gbar {GNaP_bd * surf * attenuation_factor}

   	copy T03_KDr Dend_Bas/KDr
   	addmsg Dend_Bas Dend_Bas/KDr VOLTAGE Vm
   	addmsg Dend_Bas/KDr Dend_Bas CHANNEL Gk Ek
   	setfield Dend_Bas/KDr Gbar {GKDr_bd * surf}

   	copy T03_KA Dend_Bas/KA
   	addmsg Dend_Bas Dend_Bas/KA VOLTAGE Vm
   	addmsg Dend_Bas/KA Dend_Bas CHANNEL Gk Ek
   	setfield Dend_Bas/KA Gbar {GKA_bd * surf}

   	copy T03_KC Dend_Bas/KC
   	addmsg Dend_Bas Dend_Bas/KC VOLTAGE Vm
   	addmsg Dend_Bas/KC Dend_Bas CHANNEL Gk Ek
   	setfield Dend_Bas/KC Gbar {GKC_bd * surf * 2}

   	copy T03_KAHP Dend_Bas/KAHP
   	addmsg Dend_Bas Dend_Bas/KAHP VOLTAGE Vm
   	addmsg Dend_Bas/KAHP Dend_Bas CHANNEL Gk Ek
   	setfield Dend_Bas/KAHP Gbar {GKAHP_bd * surf}
  
   	copy T03_K2 Dend_Bas/K2
   	addmsg Dend_Bas Dend_Bas/K2 VOLTAGE Vm
   	addmsg Dend_Bas/K2 Dend_Bas CHANNEL Gk Ek
   	setfield Dend_Bas/K2 Gbar {GK2_bd * surf}

   	copy T03_KM Dend_Bas/KM
   	addmsg Dend_Bas Dend_Bas/KM VOLTAGE Vm
   	addmsg Dend_Bas/KM Dend_Bas CHANNEL Gk Ek
   	setfield Dend_Bas/KM Gbar {GKM_bd * surf}

   	copy T03_CaT Dend_Bas/CaT
   	addmsg Dend_Bas Dend_Bas/CaT VOLTAGE Vm
   	addmsg Dend_Bas/CaT Dend_Bas CHANNEL Gk Ek
   	setfield Dend_Bas/CaT Gbar {GCaT_bd * surf * attenuation_factor}

   	copy T03_CaL Dend_Bas/CaL
   	addmsg Dend_Bas Dend_Bas/CaL VOLTAGE Vm
   	addmsg Dend_Bas/CaL Dend_Bas CHANNEL Gk Ek
   	setfield Dend_Bas/CaL Gbar {GCaL_bd * surf * attenuation_factor} // 0.5} // 1.0}

   	copy WS_H Dend_Bas/H
   	addmsg Dend_Bas Dend_Bas/H VOLTAGE Vm
   	addmsg Dend_Bas/H Dend_Bas CHANNEL Gk Ek
   	setfield Dend_Bas/H Gbar {GH_d * surf}

   	create Ca_concen Dend_Bas/Ca_pool
   	setfield Dend_Bas/Ca_pool tau {CaTau_d} B {B} Ca_base 0 thick 2.0e-9
   	addmsg Dend_Bas/CaT Dend_Bas/Ca_pool I_Ca Ik
   	addmsg Dend_Bas/CaL Dend_Bas/Ca_pool I_Ca Ik
   	addmsg Dend_Bas/Ca_pool Dend_Bas/KC CONCEN Ca
   	addmsg Dend_Bas/Ca_pool Dend_Bas/KAHP CONCEN Ca

//   create synchan Dend_Bas/Glu
//   setfield Dend_Bas/Glu tau1 1.0e-4 tau2 15.0e-3 gmax {G_Glu} Ek 0.00
//   addmsg Dend_Bas Dend_Bas/Glu VOLTAGE Vm
//   addmsg Dend_Bas/Glu Dend_Bas CHANNEL Gk Ek


   	copy AMPA Dend_Bas/AMPA
   	addmsg Dend_Bas/AMPA Dend_Bas CHANNEL Gk Ek
   	addmsg Dend_Bas Dend_Bas/AMPA VOLTAGE Vm

/*
   copy NMDA Dend_Bas/NMDA
   addmsg  Dend_Bas/NMDA Dend_Bas/NMDA/Mg_BLOCK CHANNEL Gk Ek
   addmsg  Dend_Bas/NMDA/Mg_BLOCK Dend_Bas CHANNEL Gk Ek
   addmsg Dend_Bas/NMDA Dend_Bas CHANNEL Gk Ek
   addmsg Dend_Bas Dend_Bas/NMDA VOLTAGE Vm
   setfield Dend_Bas/NMDA gmax {G_NMDA * surf} 
*/
   	copy GABA Dend_Bas/GABA
   	addmsg Dend_Bas/GABA Dend_Bas CHANNEL Gk Ek
   	addmsg Dend_Bas Dend_Bas/GABA VOLTAGE Vm
   	setfield Dend_Bas/GABA gmax {G_GABA * surf} 

/*
   copy GABAB Dend_Bas/GABAB
   addmsg Dend_Bas/GABAB Dend_Bas CHANNEL Gk Ek
   addmsg Dend_Bas Dend_Bas/GABAB VOLTAGE Vm
   setfield Dend_Bas/GABAB gmax {G_GABAB * surf} 
*/
 
	create compartment Dend_Ap_Shaft
	dia = 1
	len = 1
	setfield Dend_Ap_Shaft Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia {dia} len {len}
	surf = {dia * len * PI}

   	copy T03_NaF Dend_Ap_Shaft/NaF
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/NaF VOLTAGE Vm
   	addmsg Dend_Ap_Shaft/NaF Dend_Ap_Shaft CHANNEL Gk Ek
//   setfield Dend_Ap_Shaft/NaF Gbar {GNaF_shaft * surf}

   	setfield Dend_Ap_Shaft/NaF Gbar {GNaF_shaft * surf * attenuation_factor}

   	copy T03_NaP Dend_Ap_Shaft/NaP
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/NaP VOLTAGE Vm
   	addmsg Dend_Ap_Shaft/NaP Dend_Ap_Shaft CHANNEL Gk Ek
   	setfield Dend_Ap_Shaft/NaP Gbar {GNaP_shaft * surf * attenuation_factor}

   	copy T03_KDr Dend_Ap_Shaft/KDr
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/KDr VOLTAGE Vm
   	addmsg Dend_Ap_Shaft/KDr Dend_Ap_Shaft CHANNEL Gk Ek
   	setfield Dend_Ap_Shaft/KDr Gbar {GKDr_shaft * surf} //  * 20}

   	copy T03_KA Dend_Ap_Shaft/KA
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/KA VOLTAGE Vm
   	addmsg Dend_Ap_Shaft/KA Dend_Ap_Shaft CHANNEL Gk Ek
   	setfield Dend_Ap_Shaft/KA Gbar {GKA_shaft * surf}

   	copy T03_KC Dend_Ap_Shaft/KC
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/KC VOLTAGE Vm
   	addmsg Dend_Ap_Shaft/KC Dend_Ap_Shaft CHANNEL Gk Ek
   	setfield Dend_Ap_Shaft/KC Gbar {GKC_shaft * surf}

   	copy T03_KAHP Dend_Ap_Shaft/KAHP
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/KAHP VOLTAGE Vm
   	addmsg Dend_Ap_Shaft/KAHP Dend_Ap_Shaft CHANNEL Gk Ek
   	setfield Dend_Ap_Shaft/KAHP Gbar {GKAHP_shaft * surf}

   	copy T03_K2 Dend_Ap_Shaft/K2
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/K2 VOLTAGE Vm
   	addmsg Dend_Ap_Shaft/K2 Dend_Ap_Shaft CHANNEL Gk Ek
   	setfield Dend_Ap_Shaft/K2 Gbar {GK2_shaft * surf}

   	copy T03_KM Dend_Ap_Shaft/KM
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/KM VOLTAGE Vm
   	addmsg Dend_Ap_Shaft/KM Dend_Ap_Shaft CHANNEL Gk Ek
   	setfield Dend_Ap_Shaft/KM Gbar {GKM_shaft * surf}

   	copy T03_CaT Dend_Ap_Shaft/CaT
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/CaT VOLTAGE Vm
   	addmsg Dend_Ap_Shaft/CaT Dend_Ap_Shaft CHANNEL Gk Ek
   	setfield Dend_Ap_Shaft/CaT Gbar {GCaT_shaft * surf * attenuation_factor}

   	copy T03_CaL Dend_Ap_Shaft/CaL
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/CaL VOLTAGE Vm
   	addmsg Dend_Ap_Shaft/CaL Dend_Ap_Shaft CHANNEL Gk Ek
   	setfield Dend_Ap_Shaft/CaL Gbar {GCaL_shaft * surf * attenuation_factor} // 0.5} // 1.0}

   	copy WS_H Dend_Ap_Shaft/H
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/H VOLTAGE Vm
   	addmsg Dend_Ap_Shaft/H Dend_Ap_Shaft CHANNEL Gk Ek
   	setfield Dend_Ap_Shaft/H Gbar {GH_d * surf}

   	create Ca_concen Dend_Ap_Shaft/Ca_pool
   	setfield Dend_Ap_Shaft/Ca_pool tau {CaTau_d} B {B} Ca_base 0 thick 2.0e-9
   	addmsg Dend_Ap_Shaft/CaT Dend_Ap_Shaft/Ca_pool I_Ca Ik
   	addmsg Dend_Ap_Shaft/CaL Dend_Ap_Shaft/Ca_pool I_Ca Ik
   	addmsg Dend_Ap_Shaft/Ca_pool Dend_Ap_Shaft/KC CONCEN Ca
   	addmsg Dend_Ap_Shaft/Ca_pool Dend_Ap_Shaft/KAHP CONCEN Ca

//   create synchan Dend_Ap_Shaft/Glu
//   setfield Dend_Ap_Shaft/Glu tau1 1.0e-4 tau2 15.0e-3 gmax {G_Glu} Ek 0.0
//   addmsg Dend_Ap_Shaft Dend_Ap_Shaft/Glu VOLTAGE Vm
//   addmsg Dend_Ap_Shaft/Glu Dend_Ap_Shaft CHANNEL Gk Ek


   	copy AMPA Dend_Ap_Shaft/AMPA
   	addmsg Dend_Ap_Shaft/AMPA Dend_Ap_Shaft CHANNEL Gk Ek
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/AMPA VOLTAGE Vm

/*
   copy NMDA Dend_Ap_Shaft/NMDA
   addmsg  Dend_Ap_Shaft/NMDA Dend_Ap_Shaft/NMDA/Mg_BLOCK CHANNEL Gk Ek
   addmsg  Dend_Ap_Shaft/NMDA/Mg_BLOCK Dend_Ap_Shaft CHANNEL Gk Ek
   addmsg Dend_Ap_Shaft/NMDA Dend_Ap_Shaft CHANNEL Gk Ek
   addmsg Dend_Ap_Shaft Dend_Ap_Shaft/NMDA VOLTAGE Vm
   setfield Dend_Ap_Shaft/NMDA gmax {G_NMDA * surf} 
*/

   	copy GABA Dend_Ap_Shaft/GABA
   	addmsg Dend_Ap_Shaft/GABA Dend_Ap_Shaft CHANNEL Gk Ek
   	addmsg Dend_Ap_Shaft Dend_Ap_Shaft/GABA VOLTAGE Vm
   	setfield Dend_Ap_Shaft/GABA gmax {G_GABA * surf} 

/*
   copy GABAB Dend_Ap_Shaft/GABAB
   addmsg Dend_Ap_Shaft/GABAB Dend_Ap_Shaft CHANNEL Gk Ek
   addmsg Dend_Ap_Shaft Dend_Ap_Shaft/GABAB VOLTAGE Vm
   setfield Dend_Ap_Shaft/GABAB gmax {G_GABAB * surf} 
*/


	create compartment Dend_Ap
	dia = 1
	len = 1
	setfield Dend_Ap Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia {dia} len {len}
	surf = {dia * len * PI}

   	copy T03_NaF Dend_Ap/NaF
   	addmsg Dend_Ap Dend_Ap/NaF VOLTAGE Vm
   	addmsg Dend_Ap/NaF Dend_Ap CHANNEL Gk Ek
   	setfield Dend_Ap/NaF Gbar {GNaF_pad * surf * attenuation_factor}

   	copy T03_NaP Dend_Ap/NaP
   	addmsg Dend_Ap Dend_Ap/NaP VOLTAGE Vm
   	addmsg Dend_Ap/NaP Dend_Ap CHANNEL Gk Ek
   	setfield Dend_Ap/NaP Gbar {GNaP_pad * surf * attenuation_factor}

   	copy T03_KDr Dend_Ap/KDr
   	addmsg Dend_Ap Dend_Ap/KDr VOLTAGE Vm
   	addmsg Dend_Ap/KDr Dend_Ap CHANNEL Gk Ek
   	setfield Dend_Ap/KDr Gbar {GKDr_pad * surf}

   	copy T03_KA Dend_Ap/KA
   	addmsg Dend_Ap Dend_Ap/KA VOLTAGE Vm
   	addmsg Dend_Ap/KA Dend_Ap CHANNEL Gk Ek
   	setfield Dend_Ap/KA Gbar {GKA_pad * surf}

   	copy T03_KC Dend_Ap/KC
   	addmsg Dend_Ap Dend_Ap/KC VOLTAGE Vm
   	addmsg Dend_Ap/KC Dend_Ap CHANNEL Gk Ek
   	setfield Dend_Ap/KC Gbar {GKC_pad * surf}

   	copy T03_KAHP Dend_Ap/KAHP
   	addmsg Dend_Ap Dend_Ap/KAHP VOLTAGE Vm
   	addmsg Dend_Ap/KAHP Dend_Ap CHANNEL Gk Ek
   	setfield Dend_Ap/KAHP Gbar {GKAHP_pad * surf}

   	copy T03_K2 Dend_Ap/K2
   	addmsg Dend_Ap Dend_Ap/K2 VOLTAGE Vm
   	addmsg Dend_Ap/K2 Dend_Ap CHANNEL Gk Ek
   	setfield Dend_Ap/K2 Gbar {GK2_pad * surf}

   	copy T03_KM Dend_Ap/KM
   	addmsg Dend_Ap Dend_Ap/KM VOLTAGE Vm
   	addmsg Dend_Ap/KM Dend_Ap CHANNEL Gk Ek
   	setfield Dend_Ap/KM Gbar {GKM_pad * surf}

   	copy T03_CaT Dend_Ap/CaT
   	addmsg Dend_Ap Dend_Ap/CaT VOLTAGE Vm
   	addmsg Dend_Ap/CaT Dend_Ap CHANNEL Gk Ek
   	setfield Dend_Ap/CaT Gbar {GCaT_pad * surf * attenuation_factor}

   	copy T03_CaL Dend_Ap/CaL
   	addmsg Dend_Ap Dend_Ap/CaL VOLTAGE Vm
   	addmsg Dend_Ap/CaL Dend_Ap CHANNEL Gk Ek
   	setfield Dend_Ap/CaL Gbar {GCaL_pad * surf * attenuation_factor} // 0.5} // 1.0}

   	copy WS_H Dend_Ap/H
   	addmsg Dend_Ap Dend_Ap/H VOLTAGE Vm
   	addmsg Dend_Ap/H Dend_Ap CHANNEL Gk Ek
   	setfield Dend_Ap/H Gbar {GH_d * surf}

   	create Ca_concen Dend_Ap/Ca_pool
   	setfield Dend_Ap/Ca_pool tau {CaTau_d} B {B} Ca_base 0 thick 2.0e-9
   	addmsg Dend_Ap/CaT Dend_Ap/Ca_pool I_Ca Ik
   	addmsg Dend_Ap/CaL Dend_Ap/Ca_pool I_Ca Ik
   	addmsg Dend_Ap/Ca_pool Dend_Ap/KC CONCEN Ca
   	addmsg Dend_Ap/Ca_pool Dend_Ap/KAHP CONCEN Ca

//   create synchan Dend_Ap/Glu
//   setfield Dend_Ap/Glu tau1 1.0e-4 tau2 15.0e-3 gmax {G_Glu} Ek 0.0
//   addmsg Dend_Ap Dend_Ap/Glu VOLTAGE Vm
//   addmsg Dend_Ap/Glu Dend_Ap CHANNEL Gk Ek


   	copy AMPA Dend_Ap/AMPA
   	addmsg Dend_Ap/AMPA Dend_Ap CHANNEL Gk Ek
   	addmsg Dend_Ap Dend_Ap/AMPA VOLTAGE Vm

/*
   copy NMDA Dend_Ap/NMDA
   addmsg  Dend_Ap/NMDA Dend_Ap/NMDA/Mg_BLOCK CHANNEL Gk Ek
   addmsg  Dend_Ap/NMDA/Mg_BLOCK Dend_Ap CHANNEL Gk Ek
   addmsg Dend_Ap/NMDA Dend_Ap CHANNEL Gk Ek
   addmsg Dend_Ap Dend_Ap/NMDA VOLTAGE Vm
   setfield Dend_Ap/NMDA gmax {G_NMDA * surf} 
*/

   	copy GABA Dend_Ap/GABA
   	addmsg Dend_Ap/GABA Dend_Ap CHANNEL Gk Ek
   	addmsg Dend_Ap Dend_Ap/GABA VOLTAGE Vm
   	setfield Dend_Ap/GABA gmax {G_GABA * surf} 

/*
   copy GABAB Dend_Ap/GABAB
   addmsg Dend_Ap/GABAB Dend_Ap CHANNEL Gk Ek
   addmsg Dend_Ap Dend_Ap/GABAB VOLTAGE Vm
   setfield Dend_Ap/GABAB gmax {G_GABAB * surf} 
*/


	create compartment Dend_Ap_Med
	dia = 1
	len = 1
	setfield Dend_Ap_Med Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia {dia} len {len}
	surf = {dia * len * PI}

   	copy T03_NaF Dend_Ap_Med/NaF
   	addmsg Dend_Ap_Med Dend_Ap_Med/NaF VOLTAGE Vm
   	addmsg Dend_Ap_Med/NaF Dend_Ap_Med CHANNEL Gk Ek
   	setfield Dend_Ap_Med/NaF Gbar {GNaF_mad * surf * attenuation_factor}

   	copy T03_NaP Dend_Ap_Med/NaP
   	addmsg Dend_Ap_Med Dend_Ap_Med/NaP VOLTAGE Vm
   	addmsg Dend_Ap_Med/NaP Dend_Ap_Med CHANNEL Gk Ek
   	setfield Dend_Ap_Med/NaP Gbar {GNaP_mad * surf * attenuation_factor}

   	copy T03_KDr Dend_Ap_Med/KDr
   	addmsg Dend_Ap_Med Dend_Ap_Med/KDr VOLTAGE Vm
   	addmsg Dend_Ap_Med/KDr Dend_Ap_Med CHANNEL Gk Ek
   	setfield Dend_Ap_Med/KDr Gbar {GKDr_mad * surf}

   	copy T03_KA Dend_Ap_Med/KA
   	addmsg Dend_Ap_Med Dend_Ap_Med/KA VOLTAGE Vm
   	addmsg Dend_Ap_Med/KA Dend_Ap_Med CHANNEL Gk Ek
   	setfield Dend_Ap_Med/KA Gbar {GKA_mad * surf}

   	copy T03_KC Dend_Ap_Med/KC
   	addmsg Dend_Ap_Med Dend_Ap_Med/KC VOLTAGE Vm
   	addmsg Dend_Ap_Med/KC Dend_Ap_Med CHANNEL Gk Ek
   	setfield Dend_Ap_Med/KC Gbar {GKC_mad * surf}

   	copy T03_KAHP Dend_Ap_Med/KAHP
   	addmsg Dend_Ap_Med Dend_Ap_Med/KAHP VOLTAGE Vm
   	addmsg Dend_Ap_Med/KAHP Dend_Ap_Med CHANNEL Gk Ek
   	setfield Dend_Ap_Med/KAHP Gbar {GKAHP_mad * surf}

   	copy T03_K2 Dend_Ap_Med/K2
   	addmsg Dend_Ap_Med Dend_Ap_Med/K2 VOLTAGE Vm
   	addmsg Dend_Ap_Med/K2 Dend_Ap_Med CHANNEL Gk Ek
   	setfield Dend_Ap_Med/K2 Gbar {GK2_mad * surf}

   	copy T03_KM Dend_Ap_Med/KM
   	addmsg Dend_Ap_Med Dend_Ap_Med/KM VOLTAGE Vm
   	addmsg Dend_Ap_Med/KM Dend_Ap_Med CHANNEL Gk Ek
   	setfield Dend_Ap_Med/KM Gbar {GKM_mad * surf}

   	copy T03_CaT Dend_Ap_Med/CaT
   	addmsg Dend_Ap_Med Dend_Ap_Med/CaT VOLTAGE Vm
   	addmsg Dend_Ap_Med/CaT Dend_Ap_Med CHANNEL Gk Ek
   	setfield Dend_Ap_Med/CaT Gbar {GCaT_mad * surf * attenuation_factor}

   	copy T03_CaL Dend_Ap_Med/CaL
   	addmsg Dend_Ap_Med Dend_Ap_Med/CaL VOLTAGE Vm
   	addmsg Dend_Ap_Med/CaL Dend_Ap_Med CHANNEL Gk Ek
   	setfield Dend_Ap_Med/CaL Gbar {GCaL_mad * surf * attenuation_factor} // 0.5} // 1.0}

   	copy WS_H Dend_Ap_Med/H
   	addmsg Dend_Ap_Med Dend_Ap_Med/H VOLTAGE Vm
   	addmsg Dend_Ap_Med/H Dend_Ap_Med CHANNEL Gk Ek
   	setfield Dend_Ap_Med/H Gbar {GH_d * surf}

   	create Ca_concen Dend_Ap_Med/Ca_pool
   	setfield Dend_Ap_Med/Ca_pool tau {CaTau_d} B {B} Ca_base 0 thick 2.0e-9
   	addmsg Dend_Ap_Med/CaT Dend_Ap_Med/Ca_pool I_Ca Ik
   	addmsg Dend_Ap_Med/CaL Dend_Ap_Med/Ca_pool I_Ca Ik
   	addmsg Dend_Ap_Med/Ca_pool Dend_Ap_Med/KC CONCEN Ca
   	addmsg Dend_Ap_Med/Ca_pool Dend_Ap_Med/KAHP CONCEN Ca

//   create synchan Dend_Ap_Med/Glu
//   setfield Dend_Ap_Med/Glu tau1 1.0e-4 tau2 15.0e-3 gmax {G_Glu} Ek 0.06
//   addmsg Dend_Ap_Med Dend_Ap_Med/Glu VOLTAGE Vm
//   addmsg Dend_Ap_Med/Glu Dend_Ap_Med CHANNEL Gk Ek


   	copy AMPA Dend_Ap_Med/AMPA
   	addmsg Dend_Ap_Med/AMPA Dend_Ap_Med CHANNEL Gk Ek
   	addmsg Dend_Ap_Med Dend_Ap_Med/AMPA VOLTAGE Vm

/*
   copy NMDA Dend_Ap_Med/NMDA
   addmsg  Dend_Ap_Med/NMDA Dend_Ap_Med/NMDA/Mg_BLOCK CHANNEL Gk Ek
   addmsg  Dend_Ap_Med/NMDA/Mg_BLOCK Dend_Ap_Med CHANNEL Gk Ek
   addmsg Dend_Ap_Med/NMDA Dend_Ap_Med CHANNEL Gk Ek
   addmsg Dend_Ap_Med Dend_Ap_Med/NMDA VOLTAGE Vm
   setfield Dend_Ap_Med/NMDA gmax {G_NMDA * surf} 
*/

   	copy GABA Dend_Ap_Med/GABA
   	addmsg Dend_Ap_Med/GABA Dend_Ap_Med CHANNEL Gk Ek
   	addmsg Dend_Ap_Med Dend_Ap_Med/GABA VOLTAGE Vm
   	setfield Dend_Ap_Med/GABA gmax {G_GABA * surf} 

/*
   copy GABAB Dend_Ap_Med/GABAB
   addmsg Dend_Ap_Med/GABAB Dend_Ap_Med CHANNEL Gk Ek
   addmsg Dend_Ap_Med Dend_Ap_Med/GABAB VOLTAGE Vm
   setfield Dend_Ap_Med/GABAB gmax {G_GABAB * surf} 
*/


	create compartment Dend_Ap_Obl
	dia = 1
	len = 1
	setfield Dend_Ap_Obl Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia {dia} len {len}
	surf = {dia * len * PI}

   	copy T03_NaF Dend_Ap_Obl/NaF
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/NaF VOLTAGE Vm
   	addmsg Dend_Ap_Obl/NaF Dend_Ap_Obl CHANNEL Gk Ek
   	setfield Dend_Ap_Obl/NaF Gbar {GNaF_pad * surf * attenuation_factor}

   	copy T03_NaP Dend_Ap_Obl/NaP
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/NaP VOLTAGE Vm
   	addmsg Dend_Ap_Obl/NaP Dend_Ap_Obl CHANNEL Gk Ek
   	setfield Dend_Ap_Obl/NaP Gbar {GNaP_pad * surf * attenuation_factor}

   	copy T03_KDr Dend_Ap_Obl/KDr
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/KDr VOLTAGE Vm
   	addmsg Dend_Ap_Obl/KDr Dend_Ap_Obl CHANNEL Gk Ek
   	setfield Dend_Ap_Obl/KDr Gbar {GKDr_pad * surf}

   	copy T03_KA Dend_Ap_Obl/KA
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/KA VOLTAGE Vm
   	addmsg Dend_Ap_Obl/KA Dend_Ap_Obl CHANNEL Gk Ek
   	setfield Dend_Ap_Obl/KA Gbar {GKA_pad * surf}

   	copy T03_KC Dend_Ap_Obl/KC
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/KC VOLTAGE Vm
   	addmsg Dend_Ap_Obl/KC Dend_Ap_Obl CHANNEL Gk Ek
   	setfield Dend_Ap_Obl/KC Gbar {GKC_pad * surf}

   	copy T03_KAHP Dend_Ap_Obl/KAHP
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/KAHP VOLTAGE Vm
   	addmsg Dend_Ap_Obl/KAHP Dend_Ap_Obl CHANNEL Gk Ek
   	setfield Dend_Ap_Obl/KAHP Gbar {GKAHP_pad * surf}

   	copy T03_K2 Dend_Ap_Obl/K2
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/K2 VOLTAGE Vm
   	addmsg Dend_Ap_Obl/K2 Dend_Ap_Obl CHANNEL Gk Ek
   	setfield Dend_Ap_Obl/K2 Gbar {GK2_pad * surf}

   	copy T03_KM Dend_Ap_Obl/KM
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/KM VOLTAGE Vm
   	addmsg Dend_Ap_Obl/KM Dend_Ap_Obl CHANNEL Gk Ek
   	setfield Dend_Ap_Obl/KM Gbar {GKM_pad * surf}

   	copy T03_CaT Dend_Ap_Obl/CaT
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/CaT VOLTAGE Vm
   	addmsg Dend_Ap_Obl/CaT Dend_Ap_Obl CHANNEL Gk Ek
   	setfield Dend_Ap_Obl/CaT Gbar {GCaT_pad * surf * attenuation_factor}

   	copy T03_CaL Dend_Ap_Obl/CaL
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/CaL VOLTAGE Vm
   	addmsg Dend_Ap_Obl/CaL Dend_Ap_Obl CHANNEL Gk Ek
   	setfield Dend_Ap_Obl/CaL Gbar {GCaL_pad * surf * attenuation_factor} // 0.5} // 1.0}

   	copy WS_H Dend_Ap_Obl/H
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/H VOLTAGE Vm
   	addmsg Dend_Ap_Obl/H Dend_Ap_Obl CHANNEL Gk Ek
   	setfield Dend_Ap_Obl/H Gbar {GH_d * surf}

   	create Ca_concen Dend_Ap_Obl/Ca_pool
   	setfield Dend_Ap_Obl/Ca_pool tau {CaTau_d} B 5.2e5 Ca_base 0 thick 2.0e-9
   	addmsg Dend_Ap_Obl/CaT Dend_Ap_Obl/Ca_pool I_Ca Ik
   	addmsg Dend_Ap_Obl/CaL Dend_Ap_Obl/Ca_pool I_Ca Ik
   	addmsg Dend_Ap_Obl/Ca_pool Dend_Ap_Obl/KC CONCEN Ca
   	addmsg Dend_Ap_Obl/Ca_pool Dend_Ap_Obl/KAHP CONCEN Ca

//   create synchan Dend_Ap_Obl/Glu
//   setfield Dend_Ap_Obl/Glu tau1 1.0e-4 tau2 15.0e-3 gmax {G_Glu} Ek 0.0
//   addmsg Dend_Ap_Obl Dend_Ap_Obl/Glu VOLTAGE Vm
//   addmsg Dend_Ap_Obl/Glu Dend_Ap_Obl CHANNEL Gk Ek


   	copy AMPA Dend_Ap_Obl/AMPA
   	addmsg Dend_Ap_Obl/AMPA Dend_Ap_Obl CHANNEL Gk Ek
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/AMPA VOLTAGE Vm

/*
   copy NMDA Dend_Ap_Obl/NMDA
   addmsg  Dend_Ap_Obl/NMDA Dend_Ap_Obl/NMDA/Mg_BLOCK CHANNEL Gk Ek
   addmsg  Dend_Ap_Obl/NMDA/Mg_BLOCK Dend_Ap_Obl CHANNEL Gk Ek
   addmsg Dend_Ap_Obl/NMDA Dend_Ap_Obl CHANNEL Gk Ek
   addmsg Dend_Ap_Obl Dend_Ap_Obl/NMDA VOLTAGE Vm
   setfield Dend_Ap_Obl/NMDA gmax {G_NMDA * surf} 
*/

   	copy GABA Dend_Ap_Obl/GABA
   	addmsg Dend_Ap_Obl/GABA Dend_Ap_Obl CHANNEL Gk Ek
   	addmsg Dend_Ap_Obl Dend_Ap_Obl/GABA VOLTAGE Vm
   	setfield Dend_Ap_Obl/GABA gmax {G_GABA * surf} 

/*
   copy GABAB Dend_Ap_Obl/GABAB
   addmsg Dend_Ap_Obl/GABAB Dend_Ap_Obl CHANNEL Gk Ek
   addmsg Dend_Ap_Obl Dend_Ap_Obl/GABAB VOLTAGE Vm
   setfield Dend_Ap_Obl/GABAB gmax {G_GABAB * surf} 
*/


	create compartment Dend_Ap_Dis
	dia = 1
	len = 1
	setfield Dend_Ap_Dis Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia {dia} len {len}
	surf = {dia * len * PI}

   	copy T03_NaF Dend_Ap_Dis/NaF
   	addmsg Dend_Ap_Dis Dend_Ap_Dis/NaF VOLTAGE Vm
   	addmsg Dend_Ap_Dis/NaF Dend_Ap_Dis CHANNEL Gk Ek
   	setfield Dend_Ap_Dis/NaF Gbar {GNaF_dd * surf * attenuation_factor}

   	copy T03_NaP Dend_Ap_Dis/NaP
   	addmsg Dend_Ap_Dis Dend_Ap_Dis/NaP VOLTAGE Vm
   	addmsg Dend_Ap_Dis/NaP Dend_Ap_Dis CHANNEL Gk Ek
   	setfield Dend_Ap_Dis/NaP Gbar {GNaP_dd * surf * attenuation_factor}

   	copy T03_KA Dend_Ap_Dis/KA
   	addmsg Dend_Ap_Dis Dend_Ap_Dis/KA VOLTAGE Vm
   	addmsg Dend_Ap_Dis/KA Dend_Ap_Dis CHANNEL Gk Ek
   	setfield Dend_Ap_Dis/KA Gbar {GKA_dd * surf}

   	copy T03_KAHP Dend_Ap_Dis/KAHP
   	addmsg Dend_Ap_Dis Dend_Ap_Dis/KAHP VOLTAGE Vm
   	addmsg Dend_Ap_Dis/KAHP Dend_Ap_Dis CHANNEL Gk Ek
   	setfield Dend_Ap_Dis/KAHP Gbar {GKAHP_dd * surf}

   	copy T03_K2 Dend_Ap_Dis/K2
   	addmsg Dend_Ap_Dis Dend_Ap_Dis/K2 VOLTAGE Vm
   	addmsg Dend_Ap_Dis/K2 Dend_Ap_Dis CHANNEL Gk Ek
   	setfield Dend_Ap_Dis/K2 Gbar {GK2_dd * surf}

   	copy T03_KM Dend_Ap_Dis/KM
   	addmsg Dend_Ap_Dis Dend_Ap_Dis/KM VOLTAGE Vm
   	addmsg Dend_Ap_Dis/KM Dend_Ap_Dis CHANNEL Gk Ek
   	setfield Dend_Ap_Dis/KM Gbar {GKM_dd * surf}

   	copy T03_CaT Dend_Ap_Dis/CaT
   	addmsg Dend_Ap_Dis Dend_Ap_Dis/CaT VOLTAGE Vm
   	addmsg Dend_Ap_Dis/CaT Dend_Ap_Dis CHANNEL Gk Ek
   	setfield Dend_Ap_Dis/CaT Gbar {GCaT_dd * surf * attenuation_factor}

   	copy T03_CaL Dend_Ap_Dis/CaL
   	addmsg Dend_Ap_Dis Dend_Ap_Dis/CaL VOLTAGE Vm
   	addmsg Dend_Ap_Dis/CaL Dend_Ap_Dis CHANNEL Gk Ek
   	setfield Dend_Ap_Dis/CaL Gbar {GCaL_dd * surf * attenuation_factor} // 0.5} // 1.0}

   	copy WS_H Dend_Ap_Dis/H
   	addmsg Dend_Ap_Dis Dend_Ap_Dis/H VOLTAGE Vm
   	addmsg Dend_Ap_Dis/H Dend_Ap_Dis CHANNEL Gk Ek
   	setfield Dend_Ap_Dis/H Gbar {GH_d * surf}

   	create Ca_concen Dend_Ap_Dis/Ca_pool
   	setfield Dend_Ap_Dis/Ca_pool tau {CaTau_d} B {B} Ca_base 0 thick 2.0e-9
   	addmsg Dend_Ap_Dis/CaT Dend_Ap_Dis/Ca_pool I_Ca Ik
   	addmsg Dend_Ap_Dis/CaL Dend_Ap_Dis/Ca_pool I_Ca Ik
   	addmsg Dend_Ap_Dis/Ca_pool Dend_Ap_Dis/KAHP CONCEN Ca

//   create synchan Dend_Ap_Dis/Glu
//   setfield Dend_Ap_Dis/Glu tau1 1.0e-4 tau2 150e-3 gmax {G_Glu} Ek 0.0
//   addmsg Dend_Ap_Dis Dend_Ap_Dis/Glu VOLTAGE Vm
//   addmsg Dend_Ap_Dis/Glu Dend_Ap_Dis CHANNEL Gk Ek


   	copy AMPA Dend_Ap_Dis/AMPA
   	addmsg Dend_Ap_Dis/AMPA Dend_Ap_Dis CHANNEL Gk Ek
   	addmsg Dend_Ap_Dis Dend_Ap_Dis/AMPA VOLTAGE Vm
/*
   copy NMDA Dend_Ap_Dis/NMDA
   addmsg  Dend_Ap_Dis/NMDA Dend_Ap_Dis/NMDA/Mg_BLOCK CHANNEL Gk Ek
   addmsg  Dend_Ap_Dis/NMDA/Mg_BLOCK Dend_Ap_Dis CHANNEL Gk Ek
   addmsg Dend_Ap_Dis/NMDA Dend_Ap_Dis CHANNEL Gk Ek
   addmsg Dend_Ap_Dis Dend_Ap_Dis/NMDA VOLTAGE Vm
   setfield Dend_Ap_Dis/NMDA gmax {G_NMDA * surf} 
*/
   	copy GABA Dend_Ap_Dis/GABA
   	addmsg Dend_Ap_Dis/GABA Dend_Ap_Dis CHANNEL Gk Ek
   	addmsg Dend_Ap_Dis Dend_Ap_Dis/GABA VOLTAGE Vm
   	setfield Dend_Ap_Dis/GABA gmax {G_GABA * surf} 

/*
   copy GABAB Dend_Ap_Dis/GABAB
   addmsg Dend_Ap_Dis/GABAB Dend_Ap_Dis CHANNEL Gk Ek
   addmsg Dend_Ap_Dis Dend_Ap_Dis/GABAB VOLTAGE Vm
   setfield Dend_Ap_Dis/GABAB gmax {G_GABAB * surf} 

*/

   /* make cylindrical axon prototype */
	make_Axon_comps

//create compartment axon
//setfield axon Cm 1 Ra 1 Em -0.07 initVm -0.07 Rm 1 inject 0.0 dia 1 len 1


   /* 27Sep07 added spikegen and diffamp, the latter for scaling before feedback 
	to firing_rate_profile */

   

   	create spikegen soma/spike
   	setfield soma/spike thresh -0.01  \
                       abs_refract 0.0015 \
                       output_amp 1
   	addmsg soma soma/spike INPUT Vm

/*
// hsolve refuses to know diffamp

   	create diffamp soma/diffamp
   setfield soma/diffamp plus 0.08  minus 0 \
                         saturation 10e10 \
                         gain 1
   addmsg soma soma/diffamp PLUS Vm
*/



