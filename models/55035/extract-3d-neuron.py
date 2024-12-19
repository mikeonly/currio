# Attempt to extract a structure with simulated voltage data from NEURON when 
# a neuron is loaded via some .hoc file.

from neuron import h, gui
from neuron import nrn_dll_sym, ctypes
from neuron import _WrapperPlot
from neuron.gui2.utilities import _segment_3d_pts

import os

def change_working_directory(new_path):
    # Save the current working directory
    cur_dir = os.getcwd()
    try:
        # Change the current working directory to 'new_path'
        # Resolve the absolute path of the new directory
        new_path = os.path.abspath(new_path)
        os.chdir(new_path)
        print(f"Successfully changed the working directory from {cur_dir} to {new_path}")
    except FileNotFoundError:
        print(f"The directory {new_path} does not exist")
    except PermissionError:
        print(f"Permission denied: unable to change to directory {new_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

class ShapeVariableExport(_WrapperPlot): 
    
    def get_3d_pts(self, **kwargs):
        """Get 3d points for a variable in a NEURON model.
        
        Adapted from 
        https://github.com/neuronsimulator/nrn/blob/c483af882ab62e93c416ceb37d52811033f3b8fe/share/lib/python/neuron/__init__.py#L1004
        which in turn adapted from
        https://github.com/ahwillia/PyNeuron-Toolbox/blob/master/PyNeuronToolbox/morphology.py
        """
        
        get_plotshape_data = nrn_dll_sym("get_plotshape_data")
        get_plotshape_data.restype = ctypes.py_object
        variable, varobj, lo, hi, secs = get_plotshape_data(
            ctypes.py_object(self._data)
        )
        if varobj is not None:
            variable = varobj
        if secs is None:
            secs = list(h.allsec())

        if variable is None:
            kwargs.setdefault("color", "black")

            data = []
            for sec in secs:
                xs = [sec.x3d(i) for i in range(sec.n3d())]
                ys = [sec.y3d(i) for i in range(sec.n3d())]
                zs = [sec.z3d(i) for i in range(sec.n3d())]
                data.append({
                    "x": xs,
                    "y": ys,
                    "z": zs,
                    }
                )

        else:
           
            # calculate bounds
            val_range = hi - lo

            data = []
            for sec in secs:
                all_seg_pts = _segment_3d_pts(sec)
                for seg, (xs, ys, zs, _, _) in zip(sec, all_seg_pts):
                    val = _get_variable_seg(seg, variable)
                    hover_template = str(seg)
                    if val is not None:
                        hover_template += "<br>" + ("%.3f" % val)
                    col = _get_color(variable, val, cmap, lo, hi, val_range)
                    if show_diam:
                        diam = seg.diam
                    else:
                        diam = 2
                    data.append(
                        go.Scatter3d(
                            x=xs,
                            y=ys,
                            z=zs,
                            name="",
                            hovertemplate=hover_template,
                            mode="lines",
                            line=go.scatter3d.Line(color=col, width=diam),
                        )
                    )

            return FigureWidgetWithNEURON(data=data, layout={"showlegend": False})

    
def _get_variable_seg(seg, variable):
        if isinstance(variable, str):
            try:
                if "." in variable:
                    mech, var = variable.split(".")
                    val = getattr(getattr(seg, mech), var)
                else:
                    val = getattr(seg, variable)
            except AttributeError:
                # leave default color if no variable found
                val = None
        else:
            try:
                vals = variable.nodes(seg).concentration
                val = sum(vals) / len(vals)
            except:
                val = None

        return val

if __name__ == "__main__":
    change_working_directory("./obliques")
    h.load_file("fig2A.hoc")
    # # Make python wait until h is closed
    # ps = h.PlotShape(False)
    e = ShapeVariableExport().get_3d_pts()
    wait = input("Press enter to close NEURON")