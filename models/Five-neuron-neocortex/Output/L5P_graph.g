
echo making windows for graphics

// now distribured over statements and functions


//Graph of somatic Vm
//create xform /data1 [0%, 0%, 33%, 33%] -fg black -bg white
//create xgraph /data1/DS1_141099

//setfield /data1/DS1_141099 XUnits sec YUnits Volts
//setfield /data1/DS1_141099 xmax {tmax} ymin -0.11 ymax 0.04 bg white
//useclock /data1/DS1_141099 1	
//xshow /data1


function add_xgraph (pathname)

	str pathname

	create xform {pathname}-form [0%, 0%, 33%, 33%] -fg black -bg white
	xshow ^

	create xgraph ^{pathname}

	setfield ^ XUnits sec YUnits Volts
	setfield ^ xmax {tmax} ymin -0.11 ymax 0.04 bg white
	useclock ^ 1	
	xshow ^

	addmsg {pathname}/soma ^ PLOT Vm *Soma_Vm *red
	addmsg {pathname}/axon[1] ^ PLOT Vm *Axon_Vm *blue
//	addmsg {pathname}/p0b1b2b1b1b1b2b1b2b1b2b1b2b1b1b1b2b1b2b1b2b1b2b1b2b1b2b1b1[8] ^ PLOT Vm *Dend_Vm *black 
//	addmsg {pathname}/p4b2b1[15] ^ PLOT Vm *Dend_Vm *black 

end




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




