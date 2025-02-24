import pyvista as pv
import numpy as np

import currio
import random
import string

class Sensor(pv.PolyData):
    def __init__(self, points):
        super().__init__(points)
        
        # generate a uuid with 3 symbols
        self.id = "".join(random.choices(string.ascii_letters + string.digits, k=2) + \
            random.choices(string.ascii_letters, k=1)).lower()
        
    def __repr__(self):
        """Custom string representation extending PolyData's repr with organized B fields."""
        # Get base PolyData representation
        base_repr = super().__repr__()
        
        # Extract point data section
        header, *sections = base_repr.split('\n\n')
        point_data_section = next((s for s in sections if 'Point Data' in s), '')
        other_sections = [s for s in sections if 'Point Data' not in s]
        
        if 'Point Data' in point_data_section:
            # Organize fields
            b_fields = []
            other_fields = []
            
            # Parse existing point data fields
            for line in point_data_section.split('\n')[1:]:  # Skip 'Point Data:' header
                if line.strip():
                    field_name = line.strip().split(':')[0]
                    if field_name.startswith('B_'):
                        b_fields.append(line)
                    else:
                        other_fields.append(line)
            
            # Sort and format B fields
            b_fields.sort(key=lambda x: float(x.split('_')[-1].split(':')[0]) 
                         if x.split('_')[-1].split(':')[0].replace('.','',1).isdigit() else x)
            
            if len(b_fields) > 5:
                b_fields = b_fields[:2] + ['    ...'] + b_fields[-2:]
                b_fields_str = ''.join(f'    {f}\n' for f in b_fields)
                other_fields_str = ''.join(f'    {f}\n' for f in other_fields)
                point_data = (
                    'Point Data:\n'
                    f'  B fields ({len(b_fields)} total):\n'
                    f'{b_fields_str}'
                    '  Other fields:\n'
                    f'{other_fields_str}'
                )
            else:
                fields_str = ''.join(f'  {f}\n' for f in b_fields + other_fields)
                point_data = f'Point Data:\n{fields_str}'
        else:
            point_data = point_data_section
        
        # Reconstruct full representation
        return '\n\n'.join([header] + [point_data] + other_sections)
        
    def propagate(self, neuron):
        neuron.propagate_B(self)
        
    def clear(self):
        self.point_data.clear()
        self.field_data.clear()
        self.cell_data.clear()

    def _repr_html_(self):
        """HTML representation for Jupyter notebooks."""
        # Get base HTML representation from PolyData
        base_html = super()._repr_html_()
        
        # If there are B fields, modify the Point Data section
        if any(k.startswith('B_') for k in self.point_data.keys()):
            try:
                # Find Point Data section more robustly
                parts = base_html.split('<tr><th>Point Data</th><td>')
                if len(parts) < 2:
                    return base_html
                
                pre_point = parts[0]
                point_data = parts[1]
                
                parts = point_data.split('</td></tr>')
                if len(parts) < 2:
                    return base_html
                
                point_data = parts[0]
                post_point = '</td></tr>'.join(parts[1:])
                
                # Organize and format B fields
                b_fields = []
                other_fields = []
                
                for line in point_data.split('<br>'):
                    if 'B_' in line:
                        b_fields.append(line)
                    else:
                        other_fields.append(line)
                    
                # Sort B fields by time
                b_fields.sort(key=lambda x: float(x.split('_')[-1].split()[0]) 
                             if x.split('_')[-1].split()[0].replace('.','',1).isdigit() else x)
                
                # Format with ellipsis if needed
                if len(b_fields) > 5:
                    formatted_fields = (
                        f"B fields ({len(b_fields)} total):<br>"
                        f"&nbsp;&nbsp;{b_fields[0]}<br>"
                        f"&nbsp;&nbsp;{b_fields[1]}<br>"
                        f"&nbsp;&nbsp;...<br>"
                        f"&nbsp;&nbsp;{b_fields[-2]}<br>"
                        f"&nbsp;&nbsp;{b_fields[-1]}<br>"
                        f"Other fields:<br>"
                        + '<br>'.join(other_fields)
                    )
                else:
                    formatted_fields = '<br>'.join(b_fields + other_fields)
                    
                # Reconstruct HTML
                return pre_point + '<tr><th>Point Data</th><td>' + formatted_fields + '</td></tr>' + post_point
                
            except Exception:
                # If anything goes wrong, fall back to base representation
                return base_html
            
        return base_html

class RegularGridSensor(Sensor):
    def __init__(self, bounds, resolution=None, spacing=None):
        """
        Create a sensor with a regular grid of points.

        Parameters
        ----------
        bounds : tuple of floats
            The bounds of the sensor in the format (x_min, x_max, y_min, y_max, z_min, z_max).
        resolution : tuple of ints
            The number of points in each dimension. If `spacing` is provided, this is not needed.
        spacing : tuple of floats (optional)
            The spacing between points in each dimension. If provided, `resolution` is not needed.
        """
        if isinstance(spacing, (int, float)):
            # if only one number is provided, use the same spacing specification for all dimensions
            spacing = (spacing, spacing, spacing)
        if spacing is not None and resolution is not None:
            # Provide a warning, but prefer spacing over resolution.
            raise Warning("Either `spacing` or `resolution` must be provided, but not both. Using \
                          `spacing` only.")    
        if spacing is not None:
            resolution = np.array((
                (bounds[1] - bounds[0]) / spacing[0] + 1, 
                (bounds[3] - bounds[2]) / spacing[1] + 1,
                (bounds[5] - bounds[4]) / spacing[2] + 1)).astype(int)
        
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
