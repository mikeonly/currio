
echo making windows for xcell

//Display of Vm in all compartments of layer 5 pyramidal cell morphology


create xform /cellform [0%, 0%, 40%, 80%]
create xdraw /cellform/draw [0,0,100%,100%]
setfield /cellform/draw xmin -2.5e-4 xmax 2.5e-4 \
                        ymin -8.0e-4 ymax 12.0e-4 \
                        zmin -20e-5 zmax 50e-6 bg white transform y
xshow /cellform

//create xcell /cellform/draw/cell
//setfield /cellform/draw/cell colmin -0.1 colmax 0.05 path /L5P/##[TYPE=compartment] field Vm
//useclock /cellform/draw/cell 1

xcolorscale hot


function add_xcell (pathname)

	str pathname

	create xcell /cellform/draw{pathname}
	setfield /cellform/draw{pathname} colmin -0.1 colmax 0.05 path {pathname}/##[TYPE=compartment] field Vm
	useclock /cellform/draw{pathname} 1

end





