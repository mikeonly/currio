import pyvista as pv
import numpy as np
import numbers
import pint
import matplotlib.pyplot as plt

import currio
import random
import string

_PINT_REGISTRY = pint.UnitRegistry()


def _normalize_unit(unit_like) -> "pint.Unit":
    return _PINT_REGISTRY.Unit(unit_like)


def _build_unit_state(units):
    normalized = {}
    pints_map = {}
    for name, unit_like in units.items():
        unit = _normalize_unit(unit_like)
        normalized[name] = str(unit)
        pints_map[name] = unit
    return normalized, pints_map


def _is_quantity(value) -> bool:
    return isinstance(value, pint.Quantity)


def _coerce_quantity_sequence(values, target_unit):
    target_name = str(_normalize_unit(target_unit))
    arr = np.asarray(values, dtype=object)
    if arr.dtype != object or arr.size == 0:
        return None
    flat = arr.reshape(-1)
    if not all(_is_quantity(item) for item in flat):
        return None
    return np.asarray(
        [float(item.to(target_name).magnitude) for item in flat],
        dtype=float,
    ).reshape(arr.shape)


def _convert_values(values, source_unit, target_unit) -> np.ndarray:
    target = _normalize_unit(target_unit)
    target_name = str(target)
    if _is_quantity(values):
        return np.asarray(values.to(target_name).magnitude, dtype=float)

    converted = _coerce_quantity_sequence(values, target)
    if converted is not None:
        return converted

    arr = np.asarray(values, dtype=float)
    source = _normalize_unit(source_unit)
    if str(source) == str(target):
        return arr

    factor = (1.0 * source).to(target).magnitude
    return arr * float(factor)

class Sensor(pv.PolyData):
    DEFAULT_UNITS = {
        "coordinates": "m",
        "field": "T",
        "background": "T",
    }

    def __init__(self, points, 
                 background: float = 50e-6, 
                 background_direction: np.ndarray = np.array([0, 1, 0])):
        """
        Args:
            points: numpy array of shape (n_points, 3)
            background: float, background magnetic field in T
            background_direction: numpy array of shape (3,) or str, background magnetic field direction. 
                                    If str, it is assumed to be one of the following: 'x', 'y', 'z'.
        """
        super().__init__(_convert_values(points, "m", "m"))
        self._init_units()
        self.background = float(self._coerce_scalar(background, unit_key="background"))
        if isinstance(background_direction, str):
            basis = {
                "x": np.array([1.0, 0.0, 0.0]),
                "y": np.array([0.0, 1.0, 0.0]),
                "z": np.array([0.0, 0.0, 1.0]),
            }
            self.background_direction = basis[background_direction.lower()]
        else:
            self.background_direction = np.asarray(background_direction, dtype=float)
        
        # generate a uuid with 3 symbols
        self.id = "".join(random.choices(string.ascii_letters + string.digits, k=2) + \
            random.choices(string.ascii_letters, k=1)).lower()

    def _init_units(self, **overrides):
        unit_spec = dict(self.DEFAULT_UNITS)
        unit_spec.update(overrides)
        self._units, self._pints = _build_unit_state(unit_spec)
        return self

    def _copy_units_from(self, other):
        return self._init_units(**getattr(other, "_units", self.DEFAULT_UNITS))

    @property
    def units(self):
        return dict(self._units)

    @property
    def pints(self):
        return dict(self._pints)

    def set_units(self, **units):
        unknown = sorted(set(units) - set(self._units))
        if unknown:
            raise KeyError(f"Unsupported unit keys for Sensor: {unknown}. Available: {sorted(self._units)}")

        updated = dict(self._units)
        updated.update(units)
        self._units, self._pints = _build_unit_state(updated)
        return self

    def _coerce_scalar(self, value, *, unit_key="coordinates", target_unit=None) -> float:
        target = self._units[unit_key] if target_unit is None else str(_normalize_unit(target_unit))
        return float(_convert_values(value, self._units[unit_key], target))

    def _coerce_points(self, values, *, source_unit=None, target_unit=None) -> np.ndarray:
        source = self._units["coordinates"] if source_unit is None else str(_normalize_unit(source_unit))
        target = self._units["coordinates"] if target_unit is None else str(_normalize_unit(target_unit))
        return np.asarray(_convert_values(values, source, target), dtype=float)
        
    @property
    def mesh(self):
        """Returns the 3D mesh of the sensor.
        
        Since the sensor is a PolyData object, it returns self, but can optimize mesh depending
        on the availability of the field data in `B` point data."""
        return self
        
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

    def _resolve_plot_scalars(self, scalars):
        if scalars is None:
            if not self.point_data:
                raise ValueError("No point_data arrays available to plot.")
            return next(iter(self.point_data.keys())), np.asarray(next(iter(self.point_data.values())))

        if isinstance(scalars, str):
            if scalars not in self.point_data:
                raise KeyError(f"Point-data array '{scalars}' not found. Available: {list(self.point_data.keys())}")
            return scalars, np.asarray(self.point_data[scalars])

        return "values", np.asarray(scalars)

    @staticmethod
    def _component_label(component):
        labels = {0: "x", 1: "y", 2: "z", "x": "x", "y": "y", "z": "z"}
        return labels.get(component, str(component))

    def _coerce_plot_component(self, values, component=None):
        arr = np.asarray(values)
        if arr.ndim == 1:
            return arr, None

        if arr.ndim != 2:
            raise ValueError(f"Expected scalar or vector point-data array, got shape {arr.shape!r}.")

        if arr.shape[1] == 1:
            return arr[:, 0], None

        if arr.shape[1] != 3:
            raise ValueError(f"Expected vector data with shape (N, 3), got {arr.shape!r}.")

        if component is None or component == "magnitude":
            return np.linalg.norm(arr, axis=1), "magnitude"

        component_map = {"x": 0, "y": 1, "z": 2, 0: 0, 1: 1, 2: 2}
        if component not in component_map:
            raise ValueError("component must be one of None, 'magnitude', 'x', 'y', 'z', 0, 1, 2.")
        idx = component_map[component]
        return arr[:, idx], self._component_label(component)

    def plot(self, *args, method=None, **kwargs):
        if method is None:
            return super().plot(*args, **kwargs)

        method_key = str(method).lower()
        if method_key == "imshow":
            if not hasattr(self, "_plot_imshow"):
                raise TypeError("method='imshow' is only supported for RegularGridSensor.")
            return self._plot_imshow(*args, **kwargs)

        raise ValueError(f"Unsupported plot method '{method}'.")
        
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
        bounds = tuple(_convert_values(bounds, "m", "m"))
        if isinstance(spacing, (int, float)):
            # if only one number is provided, use the same spacing specification for all dimensions
            spacing = (spacing, spacing, spacing)
        elif spacing is not None:
            spacing = tuple(_convert_values(spacing, "m", "m"))
        if spacing is not None and resolution is not None:
            # Provide a warning, but prefer spacing over resolution.
            raise Warning("Either `spacing` or `resolution` must be provided, but not both. Using \
                          `spacing` only.")    
        if spacing is not None:
            resolution = np.array((
                (bounds[1] - bounds[0]) / spacing[0] + 1, 
                (bounds[3] - bounds[2]) / spacing[1] + 1,
                (bounds[5] - bounds[4]) / spacing[2] + 1)).astype(int)
        self.resolution = tuple(int(v) for v in resolution)
        
        x = np.linspace(bounds[0], bounds[1], self.resolution[0])
        y = np.linspace(bounds[2], bounds[3], self.resolution[1])
        z = np.linspace(bounds[4], bounds[5], self.resolution[2])
        X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
        points = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T
        super().__init__(points)

    @property
    def centroid(self) -> np.ndarray:
        """
        Geometric center of the sensor grid in 3D.

        This uses the current bounds, so it stays valid after moves.
        """
        return self.get_centroid()

    def get_centroid(self, z: float | None = None, mode: str = "xyz") -> np.ndarray:
        """
        Compute the sensor centroid from its bounds.

        If z is provided, or mode is 'xy', the centroid is placed at that z
        while keeping x/y in the middle of the grid. `z` may be a raw float in
        `units['coordinates']` or a Pint quantity.
        """
        mode_l = mode.lower()
        if z is not None and mode_l == "xyz":
            mode_l = "xy"

        xmin, xmax, ymin, ymax, zmin, zmax = self.bounds
        xc = 0.5 * (xmin + xmax)
        yc = 0.5 * (ymin + ymax)

        if mode_l == "xy":
            zc = 0.0 if z is None else self._coerce_scalar(z)
        else:
            zc = 0.5 * (zmin + zmax) if z is None else self._coerce_scalar(z)

        return np.array([xc, yc, zc], dtype=float)

    def move(self, to: np.ndarray, by: str = "centroid") -> "RegularGridSensor":
        """
        Translate the sensor so that a given reference point coincides with `to`.

        When by='centroid', the current centroid is moved to `to`, which is
        convenient for aligning the grid with a trace centroid.
        """
        ref = by.lower()
        if ref == "centroid":
            origin = self.get_centroid()
        else:
            raise ValueError(f"Unsupported move reference '{by}', expected 'centroid'.")

        target = np.asarray(self._coerce_points(to), dtype=float)
        if target.shape != (3,):
            raise ValueError(f"'to' must be a 3-vector, got shape {target.shape!r}.")

        delta = target - origin
        self.points += delta
        return self

    def _scaled_bounds(self, scale):
        if isinstance(scale, float):
            scale = (scale, scale, scale)
            
        sx, sy, sz = scale
        b = self.bounds  # (xmin, xmax, ymin, ymax, zmin, zmax)
        return (
            b[0] * sx, b[1] * sx,
            b[2] * sy, b[3] * sy,
            b[4] * sz, b[5] * sz,
        )

    def __mul__(self, scale):
        new_bounds = self._scaled_bounds(scale)
        scaled = RegularGridSensor(bounds=new_bounds, resolution=self.resolution)
        scaled._copy_units_from(self)
        return scaled

    def __rmul__(self, scale):
        return self.__mul__(scale)

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
