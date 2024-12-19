//genesis

float dt = 20e-6

str disk = "results/"

int amp = {1 / dt}
str a = (amp)
int i, k, l
str el, name
float t

/*********************************************************************
** Simple Granule cell model script  (#1)
** Carl Piaf BBF 1994
*********************************************************************/

str filename = (disk) @ "G_GABA_I60_w15_0.333"
//str filename = (disk) @ "G_GABA0.332"
/* always include these default definitions! */
include defaults 
str cellpath = "/Granule"

/* Purkinje cell constants */
include Gran_const.g 

/* special scripts  to create the prototypes */
include Gran_chan_tab.g
//include Gran_synchan2_biexpGABA.g
include Gran_synchan.g 
//include Gran_comp.g 
include Gran_comp_soma_dend.g


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

//make_Granule_comps
make_Granule_comps_soma_dend

/*
call Gran_InNa TABSAVE tabInNa37.data
call Gran_KDr  TABSAVE tabKDr37.data
call Gran_KA   TABSAVE tabKA37.data
call Gran_CaHVA TABSAVE tabCaHVA37.data
call Gran_H    TABSAVE tabH37.data
call Moczyd_KC TABSAVE tabKCa37.data
*/

//make_Vmgraph

setfield /library/granule/soma/GABAA \
            tau1 {{getfield /library/granule/soma/GABAA  tau1} / 3} \
            tau2 {{getfield /library/granule/soma/GABAA  tau2} / 3} \
            gmax {{getfield /library/granule/soma/GABAA  gmax} * 15}  

//setfield /library/granule/soma/InNa Gbar {{getfield /library/granule/soma/InNa Gbar} * 5.0}
//setfield /library/granule/soma/KDr  Gbar {{getfield /library/granule/soma/KDr  Gbar} * 5.0}


/* create the model and set up the run cell mode */
// read cell data from .p file
readcell Gran1M0_dend.p  {cellpath}  // Gran1M0.p {cellpath}


   setfield /Granule/soma/InNa Gbar {{getfield /Granule/soma/InNa Gbar} * 6.0}
   setfield /Granule/soma/KDr  Gbar {{getfield /Granule/soma/KDr  Gbar} * 6.0}

create neutral /library/granule/soma/mf_presyn
disable /library/granule/soma/mf_presyn
setfield /library/granule/soma/mf_presyn z 0
// Comment out whichever one to switch it off 
addmsg /library/granule/soma/mf_presyn /Granule/soma/GABAA ACTIVATION z
//addmsg /library/granule/soma/mf_presyn /Granule/soma/GABAB ACTIVATION z
//addmsg /library/granule/soma/mf_presyn /Granule/soma/mf_NMDA ACTIVATION z
//addmsg /library/granule/soma/mf_presyn /Granule/soma/mf_AMPA ACTIVATION z



/* Create the output element */
create asc_file /output/plot_out
useclock /output/plot_out 8
enable /output
enable /output/plot_out

ce {cellpath}

// setup the hines solver

echo preparing hines solver...


create hsolve solve
ce solve
// if this is set then reset will NOT change Vm in Hines
setfield . path "../##[][TYPE=compartment]" comptmode 1 chanmode 4  
call . SETUP


setmethod 11



// addmsg {cellpath}/soma /output/plot_out SAVE Vm


el = ({findsolvefield {cellpath}/solve soma Vm})       //#4
addmsg {cellpath}/solve /output/plot_out SAVE {el}

/*
el = ({findsolvefield {cellpath}/solve soma/GABAA Gk})
addmsg {cellpath}/solve /output/plot_out SAVE {el}    //

el = ({findsolvefield {cellpath}/solve soma/GABAA Ik})
addmsg {cellpath}/solve /output/plot_out SAVE {el}    //
*/

setfield /output/plot_out filename {filename} initialize 1 leave_open 1  \
    flush 1
echo Output to {filename}

//check
reset



// Synaptic stimulation protocol

setfield {cellpath}/soma inject 60.0e-12
call {cellpath}/solve HPUT {cellpath}/soma
step 0.333 -time


setfield /library/granule/soma/mf_presyn z {amp}
step 1
setfield /library/granule/soma/mf_presyn z 0


step 100e-3 -time


//step 0.3 -t

exit




