//genesis

float dt = 20e-6

str disk = "results_gap/"

int amp = {1 / dt}
str a = (amp)
int i, k, l
str el, name
float t

/*********************************************************************
** Simple Granule cell model script  (#1)
** Carl Piaf BBF 1994
*********************************************************************/

str filename = (disk) @ "test3"
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


   createmap {cellpath} /granule_cell_layer \
             2  1 -delta 1.0 0.0 -origin 0.0 0.0

   disable {cellpath}


   create diffamp /granule_cell_layer/Granule[1]/diffamp
   setfield /granule_cell_layer/Granule[1]/diffamp gain 1e-9  saturation 10e8
   addmsg /granule_cell_layer/Granule[1]/soma /granule_cell_layer/Granule[1]/diffamp PLUS Vm
   addmsg /granule_cell_layer/Granule[0]/soma /granule_cell_layer/Granule[1]/diffamp MINUS Vm

//   addmsg /granule_cell_layer/Granule[1]/diffamp /granule_cell_layer/Granule[0]/soma INJECT output
   

create neutral /library/granule/soma/mf_presyn
disable /library/granule/soma/mf_presyn
setfield /library/granule/soma/mf_presyn z 0
// Comment out whichever one to switch it off 
//addmsg /library/granule/soma/mf_presyn /Granule/soma/GABAA ACTIVATION z
//addmsg /library/granule/soma/mf_presyn /Granule/soma/GABAB ACTIVATION z
//addmsg /library/granule/soma/mf_presyn /Granule/soma/mf_NMDA ACTIVATION z
//addmsg /library/granule/soma/mf_presyn /Granule/soma/mf_AMPA ACTIVATION z


/* Create the output element */
create asc_file /output/plot_out
//create disk_out /output/plot_out
useclock /output/plot_out 8
enable /output
enable /output/plot_out

ce {cellpath}

// setup the hines solver

echo preparing hines solver...

       create hsolve /granule_cell_layer/Granule[0]/solve
       ce /granule_cell_layer/Granule[0]/solve
       setfield . path "../##[][TYPE=compartment]" comptmode 1 chanmode 4
       call . SETUP


       create hsolve /granule_cell_layer/Granule[1]/solve
       ce /granule_cell_layer/Granule[1]/solve
       setfield . path "../##[][TYPE=compartment]" comptmode 1 chanmode 4
       call . SETUP

// el = {findsolvefield /granule_cell_layer/Granule[1]/solve soma Vm}
// addmsg /granule_cell_layer/Granule[1]/solve /granule_cell_layer/Granule[1]/diffamp PLUS {el}

// el = {findsolvefield /granule_cell_layer/Granule[0]/solve soma Vm}
// addmsg /granule_cell_layer/Granule/solve /granule_cell_layer/Granule[1]/diffamp MINUS {el}


create script_out /gap_junction
setfield /gap_junction command "process_gap_junction"
useclock /gap_junction 0


function process_gap_junction
       ce /granule_cell_layer/Granule[0]/solve
       setfield  . \      
                 {findsolvefield . soma inject} \
                 {getfield /granule_cell_layer/Granule[1]/diffamp output}
       end

setmethod 11

reset

// setmethod 0


// addmsg {cellpath}/soma /output/plot_out SAVE Vm


el = ({findsolvefield /granule_cell_layer/Granule[0]/solve soma Vm})       //#1
addmsg /granule_cell_layer/Granule[0]/solve /output/plot_out SAVE {el}


el = ({findsolvefield /granule_cell_layer/Granule[1]/solve soma Vm})       //#1
addmsg /granule_cell_layer/Granule[1]/solve /output/plot_out SAVE {el}


setfield /output/plot_out filename {filename} initialize 1 leave_open 1  \
    flush 1
echo Output to {filename}

//check
reset



// Synaptic stimulation protocol
/*
setfield {cellpath}/soma inject 20.0e-12
call {cellpath}/solve HPUT {cellpath}/soma
step 0.3 -time
*/

/*
setfield {cellpath}/soma Em -0.065
setfield {cellpath}/soma Vm -0.0625
setfield {cellpath}/soma initVm -0.0625


call {cellpath}/solve HPUT {cellpath}/soma

*/

/*
// step 0.05 -time
setfield /library/granule/soma/mf_presyn z {amp}
step 1
setfield /library/granule/soma/mf_presyn z 0
step 100e-3 -time
*/

step 0.3 -t

// Current injection protocol

step 0.1 -time

setfield /granule_cell_layer/Granule[1]/soma inject 20.0e-12
call /granule_cell_layer/Granule[1]/solve HPUT /granule_cell_layer/Granule[1]/soma
step 0.5 -time

call /granule_cell_layer/Granule[1]/solve HSAVE /granule_cell_layer/Granule[1]/soma
setfield /granule_cell_layer/Granule[1]/soma inject 0.0e-12
call /granule_cell_layer/Granule[1]/solve HPUT /granule_cell_layer/Granule[1]/soma
step 0.2 -time







