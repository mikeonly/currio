import numpy as np
from typing import Union, Tuple
import pyvista as pv

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
                 gamma: float = 2.8e6,  # Hz/G, gyromagnetic ratio
                 linewidth: float = 5e6,  # Hz
                 contrast: float = 0.1):
        """Initialize diamond sensor parameters.
        
        Args:
            plane_normal: Crystal plane normal direction ('100', '110', '111' etc)
                        or vector [h,k,l]
            position: NV center position in um
            D: Zero-field splitting in Hz
            gamma: Gyromagnetic ratio in Hz/G
            linewidth: ODMR resonance linewidth in Hz
            contrast: ODMR contrast
        """
        self.plane_normal = self._parse_direction(plane_normal)
        self.position = np.array(position)
        self.D = D
        self.gamma = gamma
        self.linewidth = linewidth
        self.contrast = contrast
        
        # Calculate NV axes based on diamond crystal orientation
        self.nv_axes = self._calculate_nv_axes()
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
    
    def _calculate_nv_axes(self) -> np.ndarray:
        """Calculate NV axis direction based on crystal orientation.
        
        Returns:
            ndarray: NV axis direction (normalized)
        """
        # TODO: Implement proper crystallographic transformation
        # For now, returning a placeholder
        return np.array([1, 1, 1]) / np.sqrt(3)
    
    def calculate_odmr(self,
                      B_field: np.ndarray,
                      freq_range: Tuple[float, float] = (2.7e9, 3.0e9),
                      n_points: int = 1001) -> Tuple[np.ndarray, np.ndarray]:
        """Calculate ODMR spectrum for array of B-field vectors.
        
        Args:
            B_field: Magnetic field vectors, shape (N, 3) where N is number of points
            freq_range: (min_freq, max_freq) in Hz
            n_points: Number of frequency points
        
        Returns:
            frequencies: Array of frequencies
            spectra: ODMR spectra for each point, shape (N, n_points)
        """
        frequencies = np.linspace(*freq_range, n_points)
        
        # Ensure B_field is 2D array
        if B_field.ndim == 1:
            B_field = B_field[np.newaxis, :]
            
        # Calculate projection of B-field onto NV axis for all points
        B_projected = np.dot(B_field, self.nv_axes)
        
        # Calculate frequency shifts
        # TODO: Implement actual ODMR physics here
        spectra = np.zeros((len(B_field), n_points))
        
        return frequencies, spectra 