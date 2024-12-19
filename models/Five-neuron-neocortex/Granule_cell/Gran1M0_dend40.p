// Morphology file for Golgi cell
// A single compartment neuron with a spherical soma yielding
// an Rin (78 MegaOhm) and a time-constant (24 msec) as tabulated in Midtgaard (1992).
// The resulting Cm is 0.31 nF, assuming a specific membrane capacitance of 0.01 (F/m^2).
// The resulting surface area is 0.31e5 um^2.
// Written by RM (27/11/95).
// changed /library/soma to /library/interneuron/soma on 16/4/96 MAEX

   
*relative

*set_compt_param ELEAK {ELEAK}
*set_compt_param EREST_ACT {EREST_ACT}
   *set_compt_param RM	3.03 // 2.4000	// 24 000 ohm.cm^2
*set_compt_param RA	1.0000 	// 
*set_compt_param CM	0.0100	// 1microF/cm^2


// The entire neuron has now about the same membrane surface area
// as the original single soma compartment. In addition, all
// compartments have the same area.

   
*compt /library/granule/soma
   soma		none		0.000	0.000	0.000	12.25 // 30.0 // 99.33

*compt /library/granule/dend
   dend[0]        soma              0.0       3.75     0.0      5.0
   dend[1]        dend[0]           0.0       3.75     0.0      5.0
   dend[2]        dend[1]           0.0       3.75     0.0      5.0
   dend[3]        dend[2]           0.0       3.75     0.0      5.0
   dend[4]        dend[3]           0.0       3.75     0.0      5.0
   dend[5]        dend[4]           0.0       3.75     0.0      5.0
   dend[6]        dend[5]           0.0       3.75     0.0      5.0
   dend[7]        dend[6]           0.0       3.75     0.0      5.0
   dend[8]        dend[7]           0.0       4.6875   0.0      4.0
   dend[9]        dend[8]           0.0       4.6875   0.0      4.0
   dend[10]       dend[9]           0.0       4.6875   0.0      4.0
   dend[11]       dend[10]          0.0       4.6875   0.0      4.0
   dend[12]       dend[11]          0.0       4.6875   0.0      4.0
   dend[13]       dend[12]          0.0       4.6875   0.0      4.0
   dend[14]       dend[13]          0.0       4.6875   0.0      4.0
   dend[15]       dend[14]          0.0       4.6875   0.0      4.0
   dend[16]       dend[15]          0.0       6.25     0.0      3.0
   dend[17]       dend[16]          0.0       6.25     0.0      3.0
   dend[18]       dend[17]          0.0       6.25     0.0      3.0
   dend[19]       dend[18]          0.0       6.25     0.0      3.0
   dend[20]       dend[19]          0.0       6.25     0.0      3.0
   dend[21]       dend[20]          0.0       6.25     0.0      3.0
   dend[22]       dend[21]          0.0       6.25     0.0      3.0
   dend[23]       dend[22]          0.0       6.25     0.0      3.0
   dend[24]       dend[23]          0.0       9.375    0.0      2.0
   dend[25]       dend[24]          0.0       9.375    0.0      2.0
   dend[26]       dend[25]          0.0       9.375    0.0      2.0
   dend[27]       dend[26]          0.0       9.375    0.0      2.0
   dend[28]       dend[27]          0.0       9.375    0.0      2.0
   dend[29]       dend[28]          0.0       9.375    0.0      2.0
   dend[30]       dend[29]          0.0       9.375    0.0      2.0
   dend[31]       dend[30]          0.0       9.375    0.0      2.0
   dend[32]       dend[31]          0.0      18.75     0.0      1.0
   dend[33]       dend[32]          0.0      18.75     0.0      1.0
   dend[34]       dend[33]          0.0      18.75     0.0      1.0
   dend[35]       dend[34]          0.0      18.75     0.0      1.0
   dend[36]       dend[35]          0.0      18.75     0.0      1.0
   dend[37]       dend[36]          0.0      18.75     0.0      1.0
   dend[38]       dend[37]          0.0      18.75     0.0      1.0
   dend[39]       dend[38]          0.0      18.75     0.0      1.0
