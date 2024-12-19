//genesis

float dt = 2e-6

str disk = "results/"

int amp = 1/{dt} 
str a = (amp)
int i, k, l
str el, name
float t

/*********************************************************************
** Simple Granule cell model script  (#1)
** Carl Piaf BBF 1994
*********************************************************************/

str filename = (disk) @ "G_soma_test_exp"
/* always include these default definitions! */
include defaults 
str cellpath = "/Granule"

/* Purkinje cell constants */
include Gran_const.g 

/* special scripts  to create the prototypes */
include Gran_chan_tab.g
//include Gran_synchan2_biexpGABA.g
include Gran_synchan.g 
include Gran_comp.g 


/* Set the clocks */
for (i = 0; i <= 7; i = i + 1)
	setclock {i} {dt}
end
setclock 8 2.0e-5
setclock 9 1

/* To ensure that all subsequent elements are made in the library */
if (! {exists /library/granule})
    create neutral /library/granule
end

ce /library/granule

/* These make the prototypes of channels and compartments that can be
**  invoked in .p files */

make_Granule_chans

make_Granule_syns

make_Granule_comps
/*
call Gran_InNa TABSAVE tabInNa37.data
call Gran_KDr  TABSAVE tabKDr37.data
call Gran_KA   TABSAVE tabKA37.data
call Gran_CaHVA TABSAVE tabCaHVA37.data
call Gran_H    TABSAVE tabH37.data
call Moczyd_KC TABSAVE tabKCa37.data
*/

//make_Vmgraph

/* create the model and set up the run cell mode */
// read cell data from .p file
readcell Gran1M0.p  {cellpath}  // Gran1M0.p {cellpath}


create neutral /library/granule/soma/mf_presyn
disable /library/granule/soma/mf_presyn
setfield /library/granule/soma/mf_presyn z 0
// Comment out whichever one to switch it off 
//addmsg /library/granule/soma/mf_presyn /Granule/soma/GABAA ACTIVATION z
//addmsg /library/granule/soma/mf_presyn /Granule/soma/GABAB ACTIVATION z
//addmsg /library/granule/soma/mf_presyn /Granule/soma/mf_NMDA ACTIVATION z
addmsg /library/granule/soma/mf_presyn /Granule/soma/mf_AMPA ACTIVATION z




/* Create the output element */
create asc_file /output/plot_out
//create disk_out /output/plot_out
useclock /output/plot_out 8
enable /output
enable /output/plot_out

ce {cellpath}

setmethod 0


// addmsg {cellpath}/soma /output/plot_out SAVE Vm

/* currents through voltage-dependent channels */

// addmsg {cellpath}/soma/H /output/plot_out SAVE Ik
// addmsg {cellpath}/soma/InNa /output/plot_out SAVE Ik
// addmsg {cellpath}/soma/KDr /output/plot_out SAVE Ik
// addmsg {cellpath}/soma/KA /output/plot_out SAVE Ik
// addmsg {cellpath}/soma/Moczyd_KC /output/plot_out SAVE Ik
// addmsg {cellpath}/soma/CaHVA /output/plot_out SAVE Ik

/* conductances of voltage-dependent channels */

// addmsg {cellpath}/soma/H /output/plot_out SAVE Gk
// addmsg {cellpath}/soma/InNa /output/plot_out SAVE Gk
// addmsg {cellpath}/soma/KDr /output/plot_out SAVE Gk
// addmsg {cellpath}/soma/KA /output/plot_out SAVE Gk
// addmsg {cellpath}/soma/Moczyd_KC /output/plot_out SAVE Gk
// addmsg {cellpath}/soma/CaHVA /output/plot_out SAVE Gk

/* currents through synaptic channels */

 addmsg {cellpath}/soma/mf_AMPA /output/plot_out SAVE Ik
// addmsg {cellpath}/soma/mf_NMDA /output/plot_out SAVE Ik
// addmsg {cellpath}/soma/mf_GABAAA /output/plot_out SAVE Ik

/* conductances of synaptic channels */

// addmsg {cellpath}/soma/mf_AMPA /output/plot_out SAVE Gk
// addmsg {cellpath}/soma/mf_NMDA /output/plot_out SAVE Gk
// addmsg {cellpath}/soma/mf_GABAAA /output/plot_out SAVE Gk

/* varia */

// addmsg {cellpath}/soma/Ca_pool /output/plot_out SAVE Ca


setfield /output/plot_out filename {filename} initialize 1 leave_open 1  \
    flush 1
echo Output to {filename}


reset



// Synaptic stimulation protocol
/*
setfield {cellpath}/soma inject -4.0e-12
step 0.3 -time
*/

/*
setfield {cellpath}/soma Em -0.065
setfield {cellpath}/soma Vm -0.0625
setfield {cellpath}/soma initVm -0.0625
*/

/*
step 0.05 -time
setfield /library/granule/soma/mf_presyn z {amp}
step 1
setfield /library/granule/soma/mf_presyn z 0
step 100e-3 -time
*/


// Current injection protocol
/*
step 0.1 -time

setfield {cellpath}/soma inject 10.0e-12
step 0.5 -time

setfield {cellpath}/soma inject 0.0e-12
step 0.2 -time

setfield {cellpath}/soma inject 0.0e-12
step 1.0 -time
*/





