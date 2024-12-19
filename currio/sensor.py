import pyvista as pv
import numpy as np

class Sensor(pv.PolyData):
    def __init__(self, points):
        super().__init__(points)
    
    def add_field(self, B, times):
        self.point_data['B'] = B.transpose(1, 0, 2)
        self.field_data['TIME'] = times

class RegularGridSensor(Sensor):
    def __init__(self, bounds, resolution):
        x = np.linspace(bounds[0], bounds[1], resolution[0])
        y = np.linspace(bounds[2], bounds[3], resolution[1])
        z = np.linspace(bounds[4], bounds[5], resolution[2])
        X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
        points = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T
        super().__init__(points)

class IrregularGridSensor(Sensor):
    def __init__(self, points):
        super().__init__(points)

class VolumeSensor(Sensor):
    def __init__(self, volume):
        points = volume.points
        super().__init__(points)

class PointSensor(Sensor):
    def __init__(self, points):
        super().__init__(points)
