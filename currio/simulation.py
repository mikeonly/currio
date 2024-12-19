import pyvista as pv
from currio.neuron import Neuron
from currio.utils import explode_3d_vt_dict
from currio.compiled import get_b_njit

class NeuronSimulation:
    def __init__(self, model_name):
        self.env = Neuron(model_name)
        self.vt_dict = self.env.extract_vt()
        self.res_dict = explode_3d_vt_dict(self.vt_dict)
    
    def run_simulation(self, sensor):
        B = get_b_njit(self.res_dict, sensor.points)
        sensor.add_field(B, self.res_dict["t"])
        return sensor
