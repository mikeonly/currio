
str filename = "./"

// tabchannel indices
float tab_xmin = -0.10
float tab_xmax = 0.05
int tab_xdivs = 149

float cai_min = 1.0
float cai_max = 300


// only used for proto channels
float GNa = 1
float GCa = 1
float GK = 1
float GH = 1

float ENa = 0.050
float ECa = 0.125
float EK = -0.09 
float EH = -0.035

float Temp = 37

float I_inj = -700e-12
str inj_label = "h700pA"
float Q10 = 2.3
float t_sim = 32


//Base H-current conductances before distribution
float GH_s = 0.15
float GH_d = 0.15


//Ca-pool parameters
float B = 5.2e4
float CaTau_s = 100.0e-3
float CaTau_d = 20.0e-3

//Conductance scaling parameters
float DNaP = 1.0
float DKC = 0.30
float DKM = 0.56

//somatic conductances
float GNaF_s = 4800
float GNaP_s = 0.0032 * {GNaF_s} * {DNaP}
float GKDr_s = 1250
float GKA_s = 300
float GKC_s = 75 * {DKC}
float GKAHP_s = 1.0
float GK2_s = 1.0
float GKM_s = 50.0 * {DKM}
float GCaL_s = 5.0
float GCaT_s = 1.0

//Apical shaft
float GNaF_shaft = 350
float GKA_shaft = 300.0
float GNaP_shaft = 0.0032 * {GNaF_shaft} * {DNaP}
float GKDr_shaft = 350
float GKC_shaft = 75 * {DKC}
float GKAHP_shaft = 1.0
float GK2_shaft = 1.0
float GKM_shaft = 50.0 * {DKM}
float GCaL_shaft = 3.0
float GCaT_shaft = 1.0

//basal dendritic conductances
float GNaF_bd = 350
float GNaP_bd = 0.0032 * {GNaF_bd} * {DNaP}
float GKDr_bd = 350
float GKA_bd = 20.0
float GKC_bd = 75 * {DKC}
float GKAHP_bd = 1.0
float GK2_bd = 1.0
float GKM_bd = 50.0 * {DKM}
float GCaL_bd = 3.0
float GCaT_bd = 1.0

//proximal apical dendritic conductances
float GNaF_pad = 350
float GNaP_pad = 0.0032 * {GNaF_pad} * {DNaP}
float GKDr_pad = 350
float GKA_pad = 20.0
float GKC_pad = 75 * {DKC}
float GKAHP_pad = 1.0
float GK2_pad = 1.0
float GKM_pad = 50.0 * {DKM}
float GCaL_pad = 3.0
float GCaT_pad = 1.0

//medial apical dendritic conductances
float GNaF_mad = 350
float GNaP_mad = 0.0032 * {GNaF_mad} * {DNaP}
float GKDr_mad = 350
float GKA_mad = 20.0
float GKC_mad = 75 * {DKC}
float GKAHP_mad = 1.0
float GK2_mad = 1.0
float GKM_mad = 43.0 * {DKM}
float GCaL_mad = 3.0
float GCaT_mad = 1.0

//distal conductances
float GNaF_dd = 62.5
float GNaP_dd = 0.0032 * {GNaF_dd} * {DNaP}
float GKDr_dd = 0.0
float GKA_dd = 20
float GKC_dd = 0
float GKAHP_dd = 1.0
float GK2_dd = 1.0
float GKM_dd = 9.25
//float GCaL_dd = 15.0
float GCaL_dd = 15.0
float GCaT_dd = 1.0


// axonal conductances, from Granule cell model and axon-junction paper
float scaling_f = 314.15 / 2012.67 // surface soma over surface full Gabbiani model,
// scaling needed because active channels only on soma in Gabbiani model

float GInNa_a = 2.5       \  //   correction for 10 mV shift of (in-)activation rates
             * 2         \  //   correction for 37 deg. Celsius
             * scaling_f \  //   conversion to single compartment
             * 10        \  //   conversion to SI units (S/m^2)
             * 70           //   the Gabbiani value
float GKDr_a   = 1.5  * 2 * scaling_f * 10 * 19

/* preset constants */
// Ek value used for the leak conductance
float EREST_ACT = -0.0650
// !!Change!!Ek value used for the RESET
float RESET_ACT = -0.0650
float ELEAK = -0.07 // -0.065 // -0.07 // -0.0650


/* cable parameters */
float CM = 0.01
float RMs =  3.0300
float RA = 1.0 
// CAVE : the values of CM, RMs and RA are overwritten by the cell
// description file 


//Synaptic parameters
float G_Glu = -0.75e-8
float Glu_tau1 = 5.0e-3
float Glu_tau2 = 30.0e-3


/*
//New synaptic parameters copied from Purkinje cell model
//for GABAA and AMPA channels 
float E_GABA = -0.080  // CAVE was -0.07 in granule cell model
float G_GABA = 70.0
float GB_GABA = 20.0
float GB_GABAs = 20.0
float G_GABAm, G_GABAs
float E_AMPA = 0.000
float G_par_syn = 750.0


//New synaptic parameters copied from granule cell model
//for NMDA and GABAB channels
float E_NMDA = 0.0
float G_NMDA =  1200.0e-12 / 2012.67e-12   // the Gabbiani value expressed as conductance density
float E_GABAB = -0.070
float G_GABAB = 1.0 
float G_GABAAs = G_GABAA
float GNMDAs = G_NMDA
float GAMPAs = G_AMPA
float G_GABABs = G_GABAB
*/










