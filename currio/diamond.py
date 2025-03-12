import numpy as np
from typing import Union, Tuple
import pyvista as pv
from currio.compiled import get_odmr_shifts

class NV(object):
    """Nitrogen-Vacancy (NV) center in diamond. Represents NV center orientation and position. 
    Handles ODMR calculations for diamond NV centers with specific crystal orientation. Can 
    visualize the tetrahedral structure showing the four possible NV axes in diamond crystal 
    structure."""
    
    # Four possible NV orientations in diamond crystal structure
    # These are unit vectors along <111> directions
    NV_AXES = np.array([
        [ 1,  1,  1],  # [111]
        [ 1, -1, -1],  # [1̄1̄1]
        [-1,  1, -1],  # [1̄11̄]
        [-1, -1,  1]   # [11̄1̄]
    ]) / np.sqrt(3)
    
    def __init__(self, 
                 plane_normal: Union[str, list] = '100',  # Diamond surface normal
                 position=(0,0,0),
                 D: float = 2.87e9,  # Hz, zero-field splitting
                 gamma: float = 28e9,  # Hz/T, gyromagnetic ratio
                 linewidth: float = 5e6,  # Hz
                 contrast: float = 0.1,
                 amplitude: float = 0.1,
                 background: float = 50e-6,  # T, Earth's magnetic field
                 background_direction: np.ndarray = np.array([0, 1, 0]),
                 single: bool = False):
        """Initialize diamond sensor parameters.
        
        Args:
            plane_normal: Crystal plane normal direction ('100', '110', '111' etc)
                        or vector [h,k,l]
            position: NV center position in um
            D: Zero-field splitting in Hz
            gamma: Gyromagnetic ratio in Hz/G
            linewidth: ODMR resonance linewidth in Hz
            contrast: ODMR contrast
            background: Background magnetic field in T  
            background_direction: (np.array or str) Background magnetic field direction, 
                        by default it is assumed to be in the y-direction
            single: Whether to calculate ODMR for a single NV center or for all four possible NV orientations
        """
        self.plane_normal = self._parse_direction(plane_normal)
        self.position = np.array(position)
        self.D = D
        self.gamma = gamma
        self.linewidth = linewidth
        self.contrast = contrast
        self.amplitude = amplitude
        
        self.background = background 
        """Background magnetic field in T. Earth's magnetic field is about 50 µT (0.5 Gauss)."""
        
        if isinstance(background_direction, str):
            if background_direction == 'x':
                self.background_direction = np.array([1, 0, 0])
            elif background_direction == 'y':
                self.background_direction = np.array([0, 1, 0])
            elif background_direction == 'z':
                self.background_direction = np.array([0, 0, 1])
                
        self.background_direction = background_direction 
        """Background magnetic field direction. By default it is assumed to be in the y-direction."""
        
        # Calculate NV axes based on diamond crystal orientation
        self.axes = self._calculate_nv_axes(single=single)
        self._mesh = None
        
    @property
    def axis(self):
        """Get the orientation axis of this NV center."""
        return self.NV_AXES[self.axis_index]
    
    @property 
    def mesh(self):
        """Get the visualization mesh showing the tetrahedral structure."""
        if self._mesh is None:
            self.create_mesh()
        return self._mesh
    
    @property
    def visual_properties(self):
        """Get visualization properties for this NV center."""
        return {
            'tetrahedron': {
                'opacity': 0.2,
                'color': 'lightgray'
            },
            'axes': {
                'color': [(1,0,0), (0,1,0), (0,0,1)],  # RGB for XYZ
                'scale': 0.5,  # Relative to tetrahedron
                'offset': [-1, -1, -1]  # Relative to tetrahedron
            },
            'radii': {
                'color': 'white',
                'width': 3
            },
            'center': {
                'color': 'black',
                'size': 0.1  # Relative to tetrahedron
            }
        }
    
    def create_mesh(self, scale=1.0):
        """Create basic tetrahedral mesh showing NV axes."""
        # Create tetrahedron vertices and faces
        vertices = self.NV_AXES * scale + self.position
        center = self.position
        faces = np.array([
            [3, 0, 1, 2], [3, 1, 3, 2], 
            [3, 0, 2, 3], [3, 0, 3, 1]
        ])
        
        # Create separate meshes for tetrahedron and axes
        tetra = pv.PolyData(vertices, faces)
        axes = pv.MultiBlock()  # Container for axis lines
        
        # Add radii (tetrahedral axes)
        for i, axis in enumerate(self.NV_AXES):
            line = pv.Line(center, center + axis * scale)
            axes.append(line)
        
        # Store both parts
        self._mesh = {'tetrahedron': tetra, 'axes': axes}
        return self
    
    def _parse_direction(self, direction) -> np.ndarray:
        """Convert crystallographic direction to normalized vector."""
        if isinstance(direction, str):
            vec = [int(c) for c in direction]
        else:
            vec = direction
        return np.array(vec) / np.sqrt(np.sum(np.array(vec)**2))
    
    def _calculate_nv_axes(self, single: bool = False) -> np.ndarray:
        """Calculate NV фчуі directionі based on crystal orientation.
        
        Returns:
            ndarray: NV axis direction (normalized)
        """
        # TODO: Implement proper crystallographic transformation
        # For now, returning a placeholder
        if single:
            return np.array([1, 1, 1]) / np.sqrt(3)
        else:
            return self.NV_AXES
    
    def get_frequency_shifts(self, sensor, include_background=False):
        """Calculate ODMR frequency shifts for a sensor.
        
        Args:
            sensor: Sensor object with B-field data at various points
            include_background: Whether to include background magnetic field
            
        Returns:
            shifts: Array of frequency shifts, shape (n_points, n_times, n_axes)
        """
        # Collect B-field data from all time points in sensor
        B_fields = []
        time_points = []
        
        for key in sensor.point_data.keys():
            if key.startswith('B_'):
                time_points.append(float(key.split('_')[1]))
                B_fields.append(sensor.point_data[key])
        
        if not B_fields:
            raise ValueError("No B-field data found in sensor")
            
        # Sort by time
        sorted_indices = np.argsort(time_points)
        B_fields = np.array([B_fields[i] for i in sorted_indices])
        
        # Reshape to (n_points, n_times, 3)
        B_fields = np.transpose(B_fields, (1, 0, 2))
        
        # Add background field if requested
        if include_background:
            B_fields = B_fields + self.background * self.background_direction
        
        # Calculate shifts
        shifts = get_odmr_shifts(B_fields, self.axes, self.gamma)
        
        return shifts
    
    def get_odmr_spectrum(self, shifts, freq_range=(2.7e9, 3.0e9), n_points=1001):
        """Calculate ODMR spectrum from frequency shifts.
        
        Args:
            shifts: Frequency shifts, shape (n_points, n_times, n_axes)
            freq_range: (min_freq, max_freq) in Hz
            n_points: Number of frequency points
            
        Returns:
            frequencies: Array of frequencies
            spectra: ODMR spectra, shape (n_points, n_times, n_freq)
        """
        freqs = np.linspace(*freq_range, n_points)
        n_sensor_points, n_times, n_axes = shifts.shape
        
        # Output spectra
        spectra = np.ones((n_sensor_points, n_times, n_points))
        
        # For each point, time, and NV axis
        for p in range(n_sensor_points):
            for t in range(n_times):
                for a in range(n_axes):
                    shift = shifts[p, t, a]
                    f_plus = self.D + shift
                    f_minus = self.D - shift
                    
                    # Add Lorentzian dips
                    dip_plus = self.amplitude / (1 + ((freqs - f_plus) / self.linewidth)**2)
                    dip_minus = self.amplitude / (1 + ((freqs - f_minus) / self.linewidth)**2)
                    
                    spectra[p, t] -= dip_plus + dip_minus
        
        return freqs, spectra
    
    def set_linewidth(self, linewidth: float):
        """Set the linewidth of the ODMR spectrum."""
        self.linewidth = linewidth
        
    def set_amplitude(self, amplitude: float):
        """Set the amplitude of the ODMR spectrum."""
        self.amplitude = amplitude

    def get_frequency_shifts_at_time(self, sensor, time_idx, include_background=False):
        """Calculate ODMR frequency shifts for a sensor at a specific time index.
        
        Args:
            sensor: Sensor object with B-field data
            time_idx: Time index or key (e.g., 'B_10.5')
            include_background: Whether to include background magnetic field
            
        Returns:
            shifts: Array of frequency shifts, shape (n_points, n_axes)
        """
        # Get B-field data for specified time
        if isinstance(time_idx, str) and time_idx.startswith('B_'):
            B_field = sensor.point_data[time_idx]
        elif isinstance(time_idx, int) or isinstance(time_idx, float):
            # Find the closest time point
            time_points = []
            for key in sensor.point_data.keys():
                if key.startswith('B_'):
                    time_points.append((float(key.split('_')[1]), key))
            
            # Sort by time and find closest
            time_points.sort()
            closest_time = min(time_points, key=lambda x: abs(x[0] - time_idx))
            B_field = sensor.point_data[closest_time[1]]
        else:
            raise ValueError(f"Invalid time index: {time_idx}")
        
        # Add background if requested
        if include_background:
            B_field = B_field + self.background * self.background_direction
        
        # Calculate shifts
        shifts = get_odmr_shifts(B_field, self.axes, self.gamma)
        
        return shifts