
echo making windows for graphics

// now distribured over statements and functions



function add_xgraph (pathname)

	str pathname

        str windowname = "/output" @ {pathname} @ "_window"
	create xform {windowname} [0%, 0%, 33%, 33%] -fg black -bg white
	xshow ^

        str graphname = {windowname} @ {pathname} @ "_graph"
	create xgraph {graphname}

	setfield ^ XUnits sec YUnits Volts
	setfield ^ xmax {tmax} ymin -0.11 ymax 0.04 bg white
	useclock ^ 1	
	xshow ^

// this is added because program crashes when msgs are laid outside hines solver
/*
      	if ({exists {pathname}/soma})
		name = {findsolvefield . {pathname}/soma Vm}
		addmsg . {graphname} PLOT {name} *Soma_Vm *red
	end

      	if ({exists {pathname}/axon[19]})
		name = {findsolvefield .  {pathname}/axon[19] Vm}
		addmsg . {graphname} PLOT {name} *Axon_Vm *blue
	end

      	if ({exists {pathname}/p0b1b2b1b1b1b2b1b2b1b2b1b2b1b1b1b2b1b2b1b2b1b2b1b2b1b2b1b1[8]})
		name = {findsolvefield . {pathname}/p0b1b2b1b1b1b2b1b2b1b2b1b2b1b1b1b2b1b2b1b2b1b2b1b2b1b2b1b1[8] Vm}
		addmsg . {graphname} PLOT {name} *Dend_Vm *black 
	end
*/
        ce {pathname}
      	if ({exists soma})
		name = {findsolvefield solve soma Vm}
		addmsg solve {graphname} PLOT {name} *Soma_Vm *red
	end

      	if ({exists axon[19]})
		name = {findsolvefield solve  axon[19] Vm}
		addmsg solve {graphname} PLOT {name} *Axon_Vm *blue
	end

      	if ({exists p0b1b2b1b1b1b2b1b2b1b2b1b2b1b1b1b2b1b2b1b2b1b2b1b2b1b2b1b1[8]})
		name = {findsolvefield solve p0b1b2b1b1b1b2b1b2b1b2b1b2b1b1b1b2b1b2b1b2b1b2b1b2b1b2b1b1[8] Vm}
		addmsg solve {graphname} PLOT {name} *Dend_Vm *black 
	end

end









