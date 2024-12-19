//genesis


/* Setup the hines solver  */


function make_hsolve (pathname)

	str pathname
	ce {pathname}
	echo preparing hines solver...
	create hsolve solve
	ce solve

// if this is set then reset will NOT change Vm in Hines
 	setfield . path "../##[][TYPE=compartment]" comptmode 1 chanmode 5 
	call . SETUP

	setmethod 11
//setmethod 0

// this is added because program crash when msgs are laid outside hines solver
/*
      	if ({exists {pathname}/soma})
		name = {findsolvefield . {pathname}/soma Vm}
		addmsg . {pathname}-form{pathname} PLOT {name} *Soma_Vm *red
	end

      	if ({exists {pathname}/axon[19]})
		name = {findsolvefield .  {pathname}/axon[19] Vm}
		addmsg . {pathname}-form{pathname} PLOT {name} *Axon_Vm *blue
	end

      	if ({exists {pathname}/p0b1b2b1b1b1b2b1b2b1b2b1b2b1b1b1b2b1b2b1b2b1b2b1b2b1b2b1b1[8]})
		name = {findsolvefield . {pathname}/p0b1b2b1b1b1b2b1b2b1b2b1b2b1b1b1b2b1b2b1b2b1b2b1b2b1b2b1b1[8] Vm}
		addmsg . {pathname}-form{pathname} PLOT {name} *Dend_Vm *black 
	end
*/
end



