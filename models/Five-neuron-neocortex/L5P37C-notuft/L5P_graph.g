
echo making windows for graphics






//Display of Vm in all compartments of layer 5 pyramidal cell morphology

create xform /cellform [0%, 0%, 40%, 80%]
create xdraw /cellform/draw [0,0,100%,100%]
setfield /cellform/draw xmin -2.5e-4 xmax 2.5e-4 \
                        ymin -8.0e-4 ymax 12.0e-4 \
                        zmin -20e-5 zmax 50e-6 bg white transform y
xshow /cellform
create xcell /cellform/draw/cell
setfield /cellform/draw/cell colmin -0.1 colmax 0.05 path /L5P/##[TYPE=compartment] field Vm
useclock /cellform/draw/cell 1
xcolorscale hot


//Graph of somatic Vm
create xform /data1 [0%, 0%, 33%, 33%] -fg black -bg white
create xgraph /data1/DS1_141099 

setfield /data1/DS1_141099 XUnits sec YUnits Volts
setfield /data1/DS1_141099 xmax {tmax} ymin -0.11 ymax 0.04 bg white
useclock /data1/DS1_141099 1
	
xshow /data1

// for an unknown reason, the following three lines give an execution error
// strangely enough, the same code works for the other neuron models
// I now added thses msgs at the end of the main scipt
// addmsg /L5P/soma /data1/DS1_141099 PLOT Vm *Soma_Vm *red
//  addmsg /L5P/axon[19] /data1/DS1_141099 PLOT Vm *Axon_Vm *blue
// addmsg /L5P/p0b1b2b1b1b1b2b1b2b1b2b1b2b1b1b1b2b1b2b1b2b1b2b1b2b1b2b1b1[8] /data1/DS1_141099 PLOT Vm *Dend_Vm *black 



/*

//Graph of somatic conductances
create xform /data2 [0%, 0%, 100%, 100%]
create xgraph /data2/Conductance

setfield /data2/Conductance XUnits sec YUnits S
setfield /data2/Conductance xmax {tmax} ymin 0 ymax 1e-8 bg white
	
addmsg /L5P/soma/NaF /data2/Conductance PLOT Gk *NaF *red
addmsg /L5P/soma/NaP /data2/Conductance PLOT Gk *NaP *orange
addmsg /L5P/soma/KDr /data2/Conductance PLOT Gk *KDr *blue
addmsg /L5P/soma/KA /data2/Conductance PLOT Gk *KA *black
addmsg /L5P/soma/KC /data2/Conductance PLOT Gk *KC *purple
addmsg /L5P/soma/KAHP /data2/Conductance PLOT Gk *KAHP *green
addmsg /L5P/soma/K2 /data2/Conductance PLOT Gk *K2 *brown
addmsg /L5P/soma/KM /data2/Conductance PLOT Gk *KM *grey
addmsg /L5P/soma/CaT /data2/Conductance PLOT Gk *CaT *yellow
addmsg /L5P/soma/CaL /data2/Conductance PLOT Gk *CaL *pink
addmsg /L5P/soma/H /data2/Conductance PLOT Gk *H *cyan


xshow /data2


//Graph of somatic currents
create xform /data3 [0%, 0%, 100%, 100%]
create xgraph /data3/Currents

setfield /data3/Currents XUnits sec YUnits A
setfield /data3/Currents xmax {tmax} ymin -5e-10 ymax 5e-10 bg white

addmsg /L5P/soma/NaF /data3/Currents PLOT Ik *NaF *red
addmsg /L5P/soma/NaP /data3/Currents PLOT Ik *NaP *orange
addmsg /L5P/soma/KDr /data3/Currents PLOT Ik *KDr *blue
addmsg /L5P/soma/KA /data3/Currents PLOT Ik *KA *black
addmsg /L5P/soma/KC /data3/Currents PLOT Ik *KC *purple
addmsg /L5P/soma/KAHP /data3/Currents PLOT Ik *KAHP *green
addmsg /L5P/soma/K2 /data3/Currents PLOT Ik *K2 *brown
addmsg /L5P/soma/KM /data3/Currents PLOT Ik *KM *grey
addmsg /L5P/soma/CaT /data3/Currents PLOT Ik *CaT *yellow
addmsg /L5P/soma/CaL /data3/Currents PLOT Ik *CaL *pink
addmsg /L5P/soma/H /data3/Currents PLOT Ik *H *cyan
	
xshow /data3

*/




