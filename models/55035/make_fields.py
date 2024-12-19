# trace generated using paraview version 5.13.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
magnetic_fieldvtk = LegacyVTKReader(registrationName='magnetic_field.vtk', FileNames=['/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magnetic_field.vtk'])

# create a new 'Plane'
plane1 = Plane(registrationName='Plane1')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 0

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# find source
neuron_mesh_0vtm = FindSource('neuron_mesh_0.vtm*')

# Properties modified on neuron_mesh_0vtm
neuron_mesh_0vtm.TimeArray = 'None'

# show data in view
neuron_mesh_0vtmDisplay = Show(neuron_mesh_0vtm, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
neuron_mesh_0vtmDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# show color bar/color legend
neuron_mesh_0vtmDisplay.SetScalarBarVisibility(renderView1, True)

# show data in view
magnetic_fieldvtkDisplay = Show(magnetic_fieldvtk, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
magnetic_fieldvtkDisplay.Representation = 'Outline'

# Properties modified on plane1
plane1.Origin = [-120.0, -200.0, 60.0]
plane1.Point1 = [-120.0, 560.0, 60.0]
plane1.Point2 = [160.0, -200.0, 60.0]
plane1.XResolution = 20
plane1.YResolution = 20

# show data in view
plane1Display = Show(plane1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
plane1Display.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

# find view
renderView2 = FindViewOrCreate('RenderView2', viewtype='RenderView')

# update the view to ensure updated data information
renderView2.Update()

# hide data in view
Hide(plane1, renderView1)

# change representation type
plane1Display.SetRepresentationType('Points')

# set active source
SetActiveSource(plane1)

# show data in view
plane1Display = Show(plane1, renderView1, 'GeometryRepresentation')

# Properties modified on plane1
plane1.XResolution = 30

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on plane1
plane1.XResolution = 10
plane1.YResolution = 10

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on plane1
plane1.YResolution = 20

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on plane1
plane1.XResolution = 20
plane1.YResolution = 10

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(plane1)

# set active source
SetActiveSource(magnetic_fieldvtk)

# set active source
SetActiveSource(plane1)

# set active source
SetActiveSource(magnetic_fieldvtk)

# set scalar coloring
ColorBy(magnetic_fieldvtkDisplay, ('POINTS', 'B', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
magnetic_fieldvtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
magnetic_fieldvtkDisplay.SetScalarBarVisibility(renderView1, True)

# get 2D transfer function for 'B'
bTF2D = GetTransferFunction2D('B')

# get color transfer function/color map for 'B'
bLUT = GetColorTransferFunction('B')
bLUT.TransferFunction2D = bTF2D
bLUT.RGBPoints = [1.4857020609989125e-07, 0.231373, 0.298039, 0.752941, 5.932383895345202e-05, 0.865003, 0.865003, 0.865003, 0.00011849910770080414, 0.705882, 0.0156863, 0.14902]
bLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'B'
bPWF = GetOpacityTransferFunction('B')
bPWF.Points = [1.4857020609989125e-07, 0.0, 0.5, 0.0, 0.00011849910770080414, 1.0, 0.5, 0.0]
bPWF.ScalarRangeInitialized = 1

# turn off scalar coloring
ColorBy(magnetic_fieldvtkDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(bLUT, renderView1)

# set active source
SetActiveSource(plane1)

# set active source
SetActiveSource(magnetic_fieldvtk)

# destroy magnetic_fieldvtk
Delete(magnetic_fieldvtk)
del magnetic_fieldvtk

# create a new 'Legacy VTK Reader'
magnetic_field_0vtk = LegacyVTKReader(registrationName='magnetic_field_0.vtk*', FileNames=['/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_0.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_1.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_2.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_3.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_4.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_5.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_6.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_7.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_8.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_9.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_10.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_11.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_12.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_13.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_14.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_15.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_16.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_17.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_18.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_19.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_20.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_21.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_22.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_23.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_24.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_25.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_26.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_27.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_28.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_29.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_30.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_31.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_32.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_33.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_34.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_35.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_36.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_37.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_38.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_39.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_40.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_41.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_42.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_43.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_44.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_45.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_46.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_47.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_48.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_49.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_50.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_51.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_52.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_53.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_54.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_55.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_56.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_57.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_58.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_59.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_60.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_61.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_62.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_63.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_64.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_65.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_66.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_67.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_68.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_69.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_70.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_71.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_72.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_73.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_74.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_75.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_76.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_77.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_78.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_79.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_80.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_81.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_82.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_83.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_84.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_85.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_86.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_87.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_88.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_89.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_90.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_91.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_92.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_93.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_94.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_95.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_96.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_97.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_98.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_99.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_100.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_101.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_102.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_103.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_104.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_105.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_106.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_107.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_108.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_109.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_110.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_111.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_112.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_113.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_114.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_115.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_116.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_117.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_118.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_119.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_120.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_121.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_122.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_123.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_124.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_125.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_126.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_127.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_128.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_129.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_130.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_131.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_132.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_133.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_134.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_135.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_136.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_137.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_138.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_139.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_140.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_141.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_142.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_143.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_144.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_145.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_146.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_147.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_148.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_149.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_150.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_151.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_152.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_153.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_154.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_155.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_156.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_157.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_158.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_159.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_160.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_161.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_162.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_163.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_164.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_165.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_166.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_167.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_168.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_169.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_170.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_171.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_172.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_173.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_174.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_175.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_176.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_177.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_178.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_179.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_180.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_181.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_182.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_183.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_184.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_185.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_186.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_187.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_188.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_189.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_190.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_191.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_192.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_193.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_194.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_195.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_196.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_197.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_198.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_199.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_200.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_201.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_202.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_203.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_204.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_205.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_206.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_207.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_208.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_209.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_210.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_211.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_212.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_213.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_214.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_215.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_216.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_217.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_218.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_219.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_220.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_221.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_222.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_223.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_224.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_225.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_226.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_227.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_228.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_229.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_230.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_231.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_232.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_233.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_234.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_235.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_236.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_237.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_238.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_239.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_240.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_241.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_242.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_243.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_244.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_245.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_246.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_247.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_248.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_249.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_250.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_251.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_252.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_253.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_254.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_255.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_256.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_257.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_258.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_259.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_260.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_261.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_262.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_263.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_264.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_265.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_266.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_267.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_268.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_269.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_270.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_271.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_272.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_273.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_274.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_275.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_276.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_277.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_278.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_279.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_280.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_281.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_282.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_283.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_284.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_285.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_286.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_287.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_288.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_289.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_290.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_291.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_292.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_293.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_294.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_295.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_296.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_297.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_298.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_299.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_300.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_301.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_302.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_303.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_304.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_305.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_306.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_307.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_308.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_309.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_310.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_311.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_312.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_313.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_314.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_315.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_316.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_317.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_318.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_319.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_320.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_321.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_322.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_323.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_324.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_325.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_326.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_327.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_328.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_329.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_330.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_331.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_332.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_333.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_334.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_335.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_336.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_337.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_338.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_339.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_340.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_341.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_342.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_343.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_344.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_345.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_346.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_347.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_348.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_349.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_350.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_351.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_352.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_353.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_354.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_355.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_356.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_357.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_358.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_359.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_360.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_361.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_362.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_363.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_364.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_365.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_366.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_367.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_368.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_369.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_370.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_371.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_372.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_373.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_374.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_375.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_376.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_377.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_378.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_379.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_380.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_381.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_382.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_383.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_384.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_385.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_386.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_387.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_388.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_389.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_390.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_391.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_392.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_393.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_394.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_395.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_396.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_397.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_398.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_399.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_400.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_401.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_402.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_403.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_404.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_405.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_406.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_407.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_408.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_409.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_410.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_411.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_412.vtk', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield/magnetic_field_413.vtk'])

# set active source
SetActiveSource(magnetic_field_0vtk)

# show data in view
magnetic_field_0vtkDisplay = Show(magnetic_field_0vtk, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
magnetic_field_0vtkDisplay.Representation = 'Outline'

# set active source
SetActiveSource(magnetic_field_0vtk)

# show data in view
magnetic_field_0vtkDisplay = Show(magnetic_field_0vtk, renderView1, 'StructuredGridRepresentation')

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSource1 = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource1', Input=magnetic_field_0vtk,
    SeedSource=plane1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracerWithCustomSource1Display.Representation = 'Surface'

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(streamTracerWithCustomSource1, renderView1)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(streamTracerWithCustomSource1, renderView1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# hide data in view
Hide(streamTracerWithCustomSource1, renderView1)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# set active source
SetActiveSource(magnetic_field_0vtk)

# set active source
SetActiveSource(plane1)

# set active source
SetActiveSource(magnetic_field_0vtk)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# change representation type
streamTracerWithCustomSource1Display.SetRepresentationType('Points')

# change representation type
streamTracerWithCustomSource1Display.SetRepresentationType('Surface')

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=streamTracerWithCustomSource1,
    SeedType='Line')

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=streamTracer1.SeedType)

# destroy streamTracer1
Delete(streamTracer1)
del streamTracer1

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# set active source
SetActiveSource(magnetic_field_0vtk)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# hide data in view
Hide(streamTracerWithCustomSource1, renderView1)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(streamTracerWithCustomSource1, renderView1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# set active source
SetActiveSource(magnetic_field_0vtk)

# hide data in view
Hide(streamTracerWithCustomSource1, renderView1)

# show data in view
magnetic_field_0vtkDisplay = Show(magnetic_field_0vtk, renderView1, 'StructuredGridRepresentation')

# destroy streamTracerWithCustomSource1
Delete(streamTracerWithCustomSource1)
del streamTracerWithCustomSource1

# set active source
SetActiveSource(magnetic_field_0vtk)

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSource1 = StreamTracerWithCustomSource(registrationName='StreamTracerWithCustomSource1', Input=magnetic_field_0vtk,
    SeedSource=plane1)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
streamTracerWithCustomSource1Display.Representation = 'Surface'

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# set active source
SetActiveSource(magnetic_field_0vtk)

# set active source
SetActiveSource(None)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracerWithCustomSource1)

# set active source
SetActiveSource(tube1)

# show data in view
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'

# hide data in view
Hide(tube1, renderView1)

# show data in view
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# show data in view
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(streamTracerWithCustomSource1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(tube1, renderView1)

# show data in view
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# Properties modified on tube1
tube1.Capping = 0

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on tube1
tube1.Vectors = ['POINTS', 'B']

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on tube1
tube1.Vectors = ['POINTS', 'Normals']
tube1.Capping = 1
tube1.VaryRadius = 'By Scalar'

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on renderView1
renderView1.Visible = 1

# Properties modified on renderView1
renderView1.Visible = 0

# set active source
SetActiveSource(tube1)

# set active view
SetActiveView(renderView2)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(tube1)

# show data in view
tube1Display_1 = Show(tube1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display_1.Representation = 'Surface'

# hide data in view
Hide(tube1, renderView2)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(tube1)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# hide data in view
Hide(tube1, renderView1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# destroy tube1
Delete(tube1)
del tube1

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracerWithCustomSource1)

# Properties modified on tube1
tube1.Vectors = ['POINTS', 'B']

# show data in view
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'

# hide data in view
Hide(streamTracerWithCustomSource1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(tube1, renderView1)

# set active source
SetActiveSource(tube1)

# show data in view
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(tube1, renderView1)

# show data in view
tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

# Properties modified on tube1
tube1.Radius = 15.200000000000001

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(tube1, renderView1)

# hide data in view
Hide(plane1, renderView1)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(streamTracerWithCustomSource1, renderView1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(streamTracerWithCustomSource1, renderView1)

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(streamTracerWithCustomSource1, renderView1)

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=streamTracerWithCustomSource1)

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1.SliceType)

# destroy slice1
Delete(slice1)
del slice1

# set active source
SetActiveSource(magnetic_field_0vtk)

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=magnetic_field_0vtk)

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color legend/bar for bLUT in view renderView1
bLUTColorBar = GetScalarBar(bLUT, renderView1)
bLUTColorBar.WindowLocation = 'Upper Right Corner'
bLUTColorBar.Title = 'B'
bLUTColorBar.ComponentTitle = 'Magnitude'

# change scalar bar placement
bLUTColorBar.Position = [0.8874744114636642, 0.6584668192219679]

# Rescale transfer function
bLUT.RescaleTransferFunction(0.0, 1e-08)

# Rescale transfer function
bPWF.RescaleTransferFunction(0.0, 1e-08)

# Rescale 2D transfer function
bTF2D.RescaleTransferFunction(0.0, 1e-08, 0.0, 1.0)

# Rescale transfer function
bLUT.RescaleTransferFunction(0.0, 1e-06)

# Rescale transfer function
bPWF.RescaleTransferFunction(0.0, 1e-06)

# Rescale 2D transfer function
bTF2D.RescaleTransferFunction(0.0, 1e-06, 0.0, 1.0)

# Rescale transfer function
bLUT.RescaleTransferFunction(0.0, 1e-07)

# Rescale transfer function
bPWF.RescaleTransferFunction(0.0, 1e-07)

# Rescale 2D transfer function
bTF2D.RescaleTransferFunction(0.0, 1e-07, 0.0, 1.0)

# Rescale transfer function
bLUT.RescaleTransferFunction(1e-11, 1e-07)

# Rescale transfer function
bPWF.RescaleTransferFunction(1e-11, 1e-07)

# convert to log space
bLUT.MapControlPointsToLogSpace()

# Properties modified on bLUT
bLUT.UseLogScale = 1

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
bLUT.ApplyPreset('Inferno (matplotlib)', True)

# hide color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# Rescale transfer function
bLUT.RescaleTransferFunction(1e-11, 1e-08)

# Rescale transfer function
bPWF.RescaleTransferFunction(1e-11, 1e-08)

# Rescale 2D transfer function
bTF2D.RescaleTransferFunction(1e-11, 1e-08, 0.0, 1.0)

# Rescale transfer function
bLUT.RescaleTransferFunction(0.0, 1e-05)

# Rescale transfer function
bPWF.RescaleTransferFunction(0.0, 1e-05)

# Rescale 2D transfer function
bTF2D.RescaleTransferFunction(0.0, 1e-05, 0.0, 1.0)

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.Play()

# Properties modified on slice1
slice1.Crinkleslice = 1

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
bLUT.RescaleTransferFunction(8.134167396283395e-11, 1e-05)

# Properties modified on slice1
slice1.Crinkleslice = 0

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
bLUT.RescaleTransferFunction(6.593901732582252e-11, 1e-05)

# change representation type
slice1Display.SetRepresentationType('Surface With Edges')

# change representation type
slice1Display.SetRepresentationType('Point Gaussian')

# change representation type
slice1Display.SetRepresentationType('3D Glyphs')

# change representation type
slice1Display.SetRepresentationType('Surface With Edges')

# Properties modified on slice1Display
slice1Display.Opacity = 0.98

# Properties modified on slice1Display
slice1Display.Opacity = 0.6

# change representation type
slice1Display.SetRepresentationType('Surface')

# Properties modified on slice1Display
slice1Display.Opacity = 0.58

# Properties modified on slice1Display
slice1Display.Opacity = 1.0

# Properties modified on slice1Display
slice1Display.Specular = 0.44

# Properties modified on slice1Display
slice1Display.Specular = 0.54

# Properties modified on slice1Display
slice1Display.Specular = 0.0

# Properties modified on slice1Display
slice1Display.OSPRayUseScaleArray = 'All Exact'

# Properties modified on slice1Display.DataAxesGrid
slice1Display.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on slice1Display.DataAxesGrid
slice1Display.DataAxesGrid.GridAxesVisibility = 0

# Properties modified on slice1Display.DataAxesGrid
slice1Display.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on slice1Display.DataAxesGrid
slice1Display.DataAxesGrid.GridAxesVisibility = 0

# Properties modified on slice1Display.DataAxesGrid
slice1Display.DataAxesGrid.GridAxesVisibility = 1

# set active source
SetActiveSource(plane1)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1.SliceType)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 0

animationScene1.Play()

# set active source
SetActiveSource(slice1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice1.SliceType)

# Properties modified on slice1Display.DataAxesGrid
slice1Display.DataAxesGrid.GridAxesVisibility = 0

# convert from log to linear
bLUT.MapControlPointsToLinearSpace()

# Properties modified on bLUT
bLUT.UseLogScale = 0

# Rescale transfer function
bLUT.RescaleTransferFunction(6.59390173258224e-11, 1e-06)

# Rescale transfer function
bPWF.RescaleTransferFunction(6.59390173258224e-11, 1e-06)

# Rescale 2D transfer function
bTF2D.RescaleTransferFunction(6.59390173258224e-11, 1e-06, 0.0, 1.0)

# Rescale transfer function
bLUT.RescaleTransferFunction(6.59390173258224e-11, 1e-07)

# Rescale transfer function
bPWF.RescaleTransferFunction(6.59390173258224e-11, 1e-07)

# Rescale 2D transfer function
bTF2D.RescaleTransferFunction(6.59390173258224e-11, 1e-07, 0.0, 1.0)

# Rescale transfer function
bLUT.RescaleTransferFunction(6.59390173258224e-11, 1e-06)

# Rescale transfer function
bPWF.RescaleTransferFunction(6.59390173258224e-11, 1e-06)

# Rescale 2D transfer function
bTF2D.RescaleTransferFunction(6.59390173258224e-11, 1e-06, 0.0, 1.0)

# Rescale transfer function
bLUT.RescaleTransferFunction(6.59390173258224e-11, 1e-07)

# Rescale transfer function
bPWF.RescaleTransferFunction(6.59390173258224e-11, 1e-07)

# Rescale 2D transfer function
bTF2D.RescaleTransferFunction(6.59390173258224e-11, 1e-07, 0.0, 1.0)

# Rescale transfer function
bLUT.RescaleTransferFunction(6.59390173258224e-11, 5e-07)

# Rescale transfer function
bPWF.RescaleTransferFunction(6.59390173258224e-11, 5e-07)

# Rescale 2D transfer function
bTF2D.RescaleTransferFunction(6.59390173258224e-11, 5e-07, 0.0, 1.0)

# set active source
SetActiveSource(neuron_mesh_0vtm)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1.SliceType)

# get 2D transfer function for 'voltages'
voltagesTF2D = GetTransferFunction2D('voltages')
voltagesTF2D.ScalarRangeInitialized = 1
voltagesTF2D.Range = [-70.0, 20.0, 0.0, 1.0]

# get color transfer function/color map for 'voltages'
voltagesLUT = GetColorTransferFunction('voltages')
voltagesLUT.AutomaticRescaleRangeMode = 'Never'
voltagesLUT.TransferFunction2D = voltagesTF2D
voltagesLUT.RGBPoints = [-70.0, 0.231373, 0.298039, 0.752941, -24.999999999959073, 0.865003, 0.865003, 0.865003, 20.0, 0.705882, 0.0156863, 0.14902]
voltagesLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'voltages'
voltagesPWF = GetOpacityTransferFunction('voltages')
voltagesPWF.Points = [-70.0, 0.0, 0.5, 0.0, 20.0, 1.0, 0.5, 0.0]
voltagesPWF.ScalarRangeInitialized = 1

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# set active source
SetActiveSource(plane1)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 0

# set active source
SetActiveSource(neuron_mesh_0vtm)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# set active source
SetActiveSource(magnetic_field_0vtk)

# set active source
SetActiveSource(plane1)

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.XTitle = 'X, μm '

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.YTitle = 'Y, μm '
renderView1.AxesGrid.ZTitle = 'Z, μm '
renderView1.AxesGrid.ShowGrid = 1

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.ShowGrid = 0

# get layout
layout1 = GetLayout()

# resize frame
layout1.SetSplitFraction(0, 0.5180493983533883)

# resize frame
layout1.SetSplitFraction(0, 0.5541481950601647)

# set active view
SetActiveView(renderView2)

# set active view
SetActiveView(renderView1)

renderView1.ResetActiveCameraToPositiveX()

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# Properties modified on plane1
plane1.Origin = [-120.0, -200.0, 100.0]
plane1.Point1 = [-120.0, 560.0, 100.0]
plane1.Point2 = [160.0, -200.0, 100.0]

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
bLUT.RescaleTransferFunction(6.59390173258224e-11, 9.807486590305607e-07)

# Rescale transfer function
bPWF.RescaleTransferFunction(6.59390173258224e-11, 9.807486590305607e-07)

# set active source
SetActiveSource(plane1)

# show data in view
plane1Display = Show(plane1, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(plane1, renderView1)

# Properties modified on plane1
plane1.Origin = [-120.0, -200.0, 60.0]
plane1.Point1 = [-120.0, 560.0, 60.0]
plane1.Point2 = [160.0, -200.0, 60.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice1.SliceType)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 150.0, 150.0]

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0, 150.0, 100.0]

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
bLUT.RescaleTransferFunction(6.59390173258224e-11, 1.167690906161123e-06)

# Rescale transfer function
bPWF.RescaleTransferFunction(6.59390173258224e-11, 1.167690906161123e-06)

# Properties modified on slice1.SliceType
slice1.SliceType.Offset = 100.0

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice1.SliceType
slice1.SliceType.Offset = 1.0

# update the view to ensure updated data information
renderView1.Update()

# Rescale transfer function
bLUT.RescaleTransferFunction(6.59390173258224e-11, 1.3858614060630069e-06)

# Rescale transfer function
bPWF.RescaleTransferFunction(6.59390173258224e-11, 1.3858614060630069e-06)

# Properties modified on slice1.SliceType
slice1.SliceType.Offset = 20.0

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on slice1Display
slice1Display.InterpolateScalarsBeforeMapping = 0

# Properties modified on slice1Display
slice1Display.InterpolateScalarsBeforeMapping = 1

# Properties modified on slice1Display
slice1Display.InterpolateScalarsBeforeMapping = 0

# Properties modified on slice1Display
slice1Display.MapScalars = 0

# Properties modified on bLUT
bLUT.RGBPoints = [3.809492900388619e-09, 0.001462, 0.000466, 0.013866, 7.506884622253576e-09, 0.002267, 0.00127, 0.01857, 1.1203333612928537e-08, 0.003299, 0.002249, 0.024239, 1.4900725334793816e-08, 0.004547, 0.003392, 0.030909, 1.8597174325469426e-08, 0.006006, 0.004692, 0.038558, 2.229456604733374e-08, 0.007676, 0.006136, 0.046836, 2.599101503800967e-08, 0.009561, 0.007713, 0.055143, 2.968840675987495e-08, 0.011663, 0.009417, 0.06346, 3.338579848173894e-08, 0.013995, 0.011225, 0.071862, 3.7082247472414544e-08, 0.016561, 0.013136, 0.080282, 4.0779639194279175e-08, 0.019373, 0.015133, 0.088767, 4.4476088184955437e-08, 0.022447, 0.017199, 0.097327, 4.817347990681942e-08, 0.025793, 0.019331, 0.10593, 5.1869928897496e-08, 0.029432, 0.021503, 0.114621, 5.556732061935966e-08, 0.033385, 0.023702, 0.123397, 5.926471234122429e-08, 0.037668, 0.025921, 0.132232, 6.296116133190055e-08, 0.042253, 0.028139, 0.141141, 6.665855305376519e-08, 0.046915, 0.030324, 0.150164, 7.035500204444013e-08, 0.051644, 0.032474, 0.159254, 7.405239376630542e-08, 0.056449, 0.034569, 0.168414, 7.774884275698134e-08, 0.06134, 0.03659, 0.177642, 8.144623447884566e-08, 0.066331, 0.038504, 0.186962, 8.51436262007103e-08, 0.071429, 0.040294, 0.196354, 8.884007519138625e-08, 0.076637, 0.041905, 0.205799, 9.253746691325053e-08, 0.081962, 0.043328, 0.215289, 9.623391590392647e-08, 0.087411, 0.044556, 0.224813, 9.993130762579175e-08, 0.09299, 0.045583, 0.234358, 1.0362775661646671e-07, 0.098702, 0.046402, 0.243904, 1.0732514833833133e-07, 0.104551, 0.047008, 0.25343, 1.1102159732900759e-07, 0.110536, 0.047399, 0.262912, 1.1471898905087156e-07, 0.116656, 0.047574, 0.272321, 1.184163807727359e-07, 0.122908, 0.047536, 0.281624, 1.221128297634125e-07, 0.129285, 0.047293, 0.290788, 1.2581022148527647e-07, 0.135778, 0.046856, 0.299776, 1.2950667047595273e-07, 0.142378, 0.046242, 0.308553, 1.3320406219781736e-07, 0.149073, 0.045468, 0.317085, 1.3690051118849298e-07, 0.15585, 0.044559, 0.325338, 1.4059790291035696e-07, 0.162689, 0.043554, 0.333277, 1.442952946322222e-07, 0.169575, 0.042489, 0.340874, 1.4799174362289817e-07, 0.176493, 0.041402, 0.348111, 1.516891353447625e-07, 0.183429, 0.040329, 0.354971, 1.553855843354384e-07, 0.190367, 0.039309, 0.361447, 1.5908297605730336e-07, 0.197297, 0.0384, 0.367535, 1.627794250479783e-07, 0.204209, 0.037632, 0.373238, 1.664768167698433e-07, 0.211095, 0.03703, 0.378563, 1.701742084917076e-07, 0.217949, 0.036615, 0.383522, 1.738706574823839e-07, 0.224763, 0.036405, 0.388129, 1.7756804920424848e-07, 0.231538, 0.036405, 0.3924, 1.8126449819492407e-07, 0.238273, 0.036621, 0.396353, 1.8496188991678845e-07, 0.244967, 0.037055, 0.400007, 1.8865833890746433e-07, 0.25162, 0.037705, 0.403378, 1.923557306293296e-07, 0.258234, 0.038571, 0.406485, 1.960531223511936e-07, 0.26481, 0.039647, 0.409345, 1.9974957134186922e-07, 0.271347, 0.040922, 0.411976, 2.034469630637338e-07, 0.27785, 0.042353, 0.414392, 2.0714341205440977e-07, 0.284321, 0.043933, 0.416608, 2.1084080377627407e-07, 0.290763, 0.045644, 0.418637, 2.1453725276695056e-07, 0.297178, 0.04747, 0.420491, 2.1823464448881467e-07, 0.303568, 0.049396, 0.422182, 2.2193203621067925e-07, 0.309935, 0.051407, 0.423721, 2.2562848520135524e-07, 0.316282, 0.05349, 0.425116, 2.293258769232198e-07, 0.32261, 0.055634, 0.426377, 2.3302232591389486e-07, 0.328921, 0.057827, 0.427511, 2.367197176357601e-07, 0.335217, 0.06006, 0.428524, 2.4041616662643597e-07, 0.3415, 0.062325, 0.429425, 2.4411355834830066e-07, 0.347771, 0.064616, 0.430217, 2.478109500701649e-07, 0.354032, 0.066925, 0.430906, 2.5150739906084057e-07, 0.360284, 0.069247, 0.431497, 2.552047907827052e-07, 0.366529, 0.071579, 0.431994, 2.5890123977338144e-07, 0.372768, 0.073915, 0.4324, 2.6259863149524576e-07, 0.379001, 0.076253, 0.432719, 2.6629508048592167e-07, 0.385228, 0.078591, 0.432955, 2.6999247220778567e-07, 0.391453, 0.080927, 0.433109, 2.736898639296503e-07, 0.397674, 0.083257, 0.433183, 2.773863129203266e-07, 0.403894, 0.08558, 0.433179, 2.8108370464219086e-07, 0.410113, 0.087896, 0.433098, 2.8478015363286714e-07, 0.416331, 0.090203, 0.432943, 2.8847754535473077e-07, 0.422549, 0.092501, 0.432714, 2.9217399434540705e-07, 0.428768, 0.09479, 0.432412, 2.958713860672723e-07, 0.434987, 0.097069, 0.432039, 2.9956783505794723e-07, 0.441207, 0.099338, 0.431594, 3.032652267798119e-07, 0.447428, 0.101597, 0.43108, 3.0696261850167687e-07, 0.453651, 0.103848, 0.430498, 3.1065906749235215e-07, 0.459875, 0.106089, 0.429846, 3.143564592142174e-07, 0.4661, 0.108322, 0.429125, 3.1805290820489307e-07, 0.472328, 0.110547, 0.428334, 3.2175029992675765e-07, 0.478558, 0.112764, 0.427475, 3.2544674891743303e-07, 0.484789, 0.114974, 0.426548, 3.2914414063929794e-07, 0.491022, 0.117179, 0.425552, 3.328415323611625e-07, 0.497257, 0.119379, 0.424488, 3.365379813518382e-07, 0.503493, 0.121575, 0.423356, 3.4023537307370275e-07, 0.50973, 0.123769, 0.422156, 3.4393182206437877e-07, 0.515967, 0.12596, 0.420887, 3.4762921378624303e-07, 0.522206, 0.12815, 0.419549, 3.5132566277691937e-07, 0.528444, 0.130341, 0.418142, 3.550230544987842e-07, 0.534683, 0.132534, 0.416667, 3.587204462206479e-07, 0.54092, 0.134729, 0.415123, 3.624168952113238e-07, 0.547157, 0.136929, 0.413511, 3.6611428693318824e-07, 0.553392, 0.139134, 0.411829, 3.6981073592386447e-07, 0.559624, 0.141346, 0.410078, 3.735081276457288e-07, 0.565854, 0.143567, 0.408258, 3.77204576636405e-07, 0.572081, 0.145797, 0.406369, 3.809019683582689e-07, 0.578304, 0.148039, 0.404411, 3.8459936008013387e-07, 0.584521, 0.150294, 0.402385, 3.882958090708102e-07, 0.590734, 0.152563, 0.40029, 3.9199320079267447e-07, 0.59694, 0.154848, 0.398125, 3.956896497833498e-07, 0.603139, 0.157151, 0.395891, 3.993870415052148e-07, 0.60933, 0.159474, 0.393589, 4.0308349049589e-07, 0.615513, 0.161817, 0.391219, 4.0678088221775525e-07, 0.621685, 0.164184, 0.388781, 4.1047827393961904e-07, 0.627847, 0.166575, 0.386276, 4.141747229302956e-07, 0.633998, 0.168992, 0.383704, 4.1787211465215985e-07, 0.640135, 0.171438, 0.381065, 4.215685636428357e-07, 0.64626, 0.173914, 0.378359, 4.252659553647004e-07, 0.652369, 0.176421, 0.375586, 4.289624043553763e-07, 0.658463, 0.178962, 0.372748, 4.326597960772407e-07, 0.66454, 0.181539, 0.369846, 4.363571877991051e-07, 0.670599, 0.184153, 0.366879, 4.400536367897812e-07, 0.676638, 0.186807, 0.363849, 4.437510285116455e-07, 0.682656, 0.189501, 0.360757, 4.47447477502322e-07, 0.688653, 0.192239, 0.357603, 4.5114486922418583e-07, 0.694627, 0.195021, 0.354388, 4.5484131821486164e-07, 0.700576, 0.197851, 0.351113, 4.5853870993672617e-07, 0.7065, 0.200728, 0.347777, 4.622361016585912e-07, 0.712396, 0.203656, 0.344383, 4.659325506492666e-07, 0.718264, 0.206636, 0.340931, 4.696299423711311e-07, 0.724103, 0.20967, 0.337424, 4.733263913618068e-07, 0.729909, 0.212759, 0.333861, 4.770237830836719e-07, 0.735683, 0.215906, 0.330245, 4.807202320743478e-07, 0.741423, 0.219112, 0.326576, 4.844176237962127e-07, 0.747127, 0.222378, 0.322856, 4.881140727868876e-07, 0.752794, 0.225706, 0.319085, 4.918114645087526e-07, 0.758422, 0.229097, 0.315266, 4.955088562306169e-07, 0.76401, 0.232554, 0.311399, 4.99205305221293e-07, 0.769556, 0.236077, 0.307485, 5.029026969431567e-07, 0.775059, 0.239667, 0.303526, 5.065991459338335e-07, 0.780517, 0.243327, 0.299523, 5.102965376556977e-07, 0.785929, 0.247056, 0.295477, 5.139929866463737e-07, 0.791293, 0.250856, 0.29139, 5.176903783682383e-07, 0.796607, 0.254728, 0.287264, 5.213877700901029e-07, 0.801871, 0.258674, 0.283099, 5.250842190807789e-07, 0.807082, 0.262692, 0.278898, 5.287816108026431e-07, 0.812239, 0.266786, 0.274661, 5.324780597933191e-07, 0.817341, 0.270954, 0.27039, 5.361754515151833e-07, 0.822386, 0.275197, 0.266085, 5.398719005058599e-07, 0.827372, 0.279517, 0.26175, 5.435692922277239e-07, 0.832299, 0.283913, 0.257383, 5.472666839495883e-07, 0.837165, 0.288385, 0.252988, 5.509631329402643e-07, 0.841969, 0.292933, 0.248564, 5.546605246621292e-07, 0.846709, 0.297559, 0.244113, 5.583569736528045e-07, 0.851384, 0.30226, 0.239636, 5.620543653746694e-07, 0.855992, 0.307038, 0.235133, 5.65750814365345e-07, 0.860533, 0.311892, 0.230606, 5.694482060872096e-07, 0.865006, 0.316822, 0.226055, 5.731455978090736e-07, 0.869409, 0.321827, 0.221482, 5.768420467997502e-07, 0.873741, 0.326906, 0.216886, 5.805394385216147e-07, 0.878001, 0.33206, 0.212268, 5.842358875122908e-07, 0.882188, 0.337287, 0.207628, 5.879332792341549e-07, 0.886302, 0.342586, 0.202968, 5.916297282248308e-07, 0.890341, 0.347957, 0.198286, 5.953271199466948e-07, 0.894305, 0.353399, 0.193584, 5.990245116685598e-07, 0.898192, 0.358911, 0.18886, 6.027209606592359e-07, 0.902003, 0.364492, 0.184116, 6.064183523811e-07, 0.905735, 0.37014, 0.17935, 6.101148013717758e-07, 0.90939, 0.375856, 0.174563, 6.138121930936406e-07, 0.912966, 0.381636, 0.169755, 6.175086420843168e-07, 0.916462, 0.387481, 0.164924, 6.21206033806181e-07, 0.919879, 0.393389, 0.16007, 6.249034255280459e-07, 0.923215, 0.399359, 0.155193, 6.28599874518721e-07, 0.92647, 0.405389, 0.150292, 6.322972662405858e-07, 0.929644, 0.411479, 0.145367, 6.359937152312618e-07, 0.932737, 0.417627, 0.140417, 6.396911069531264e-07, 0.935747, 0.423831, 0.13544, 6.43387555943802e-07, 0.938675, 0.430091, 0.130438, 6.470849476656671e-07, 0.941521, 0.436405, 0.125409, 6.507823393875316e-07, 0.944285, 0.442772, 0.120354, 6.544787883782074e-07, 0.946965, 0.449191, 0.115272, 6.581761801000714e-07, 0.949562, 0.45566, 0.110164, 6.618726290907476e-07, 0.952075, 0.462178, 0.105031, 6.655700208126116e-07, 0.954506, 0.468744, 0.099874, 6.692664698032884e-07, 0.956852, 0.475356, 0.094695, 6.729638615251525e-07, 0.959114, 0.482014, 0.089499, 6.766603105158284e-07, 0.961293, 0.488716, 0.084289, 6.803577022376928e-07, 0.963387, 0.495462, 0.079073, 6.840550939595576e-07, 0.965397, 0.502249, 0.073859, 6.877515429502324e-07, 0.967322, 0.509078, 0.068659, 6.914489346720979e-07, 0.969163, 0.515946, 0.063488, 6.951453836627737e-07, 0.970919, 0.522853, 0.058367, 6.98842775384638e-07, 0.97259, 0.529798, 0.053324, 7.025392243753141e-07, 0.974176, 0.53678, 0.048392, 7.062366160971786e-07, 0.975677, 0.543798, 0.043618, 7.099340078190428e-07, 0.977092, 0.55085, 0.03905, 7.136304568097187e-07, 0.978422, 0.557937, 0.034931, 7.173278485315839e-07, 0.979666, 0.565057, 0.031409, 7.21024297522259e-07, 0.980824, 0.572209, 0.028508, 7.247216892441238e-07, 0.981895, 0.579392, 0.02625, 7.284181382347997e-07, 0.982881, 0.586606, 0.024661, 7.321155299566643e-07, 0.983779, 0.593849, 0.02377, 7.358129216785281e-07, 0.984591, 0.601122, 0.023606, 7.39509370669205e-07, 0.985315, 0.608422, 0.024202, 7.432067623910691e-07, 0.985952, 0.61575, 0.025592, 7.469032113817454e-07, 0.986502, 0.623105, 0.027814, 7.506006031036096e-07, 0.986964, 0.630485, 0.030908, 7.542970520942853e-07, 0.987337, 0.63789, 0.034916, 7.579944438161502e-07, 0.987622, 0.64532, 0.039886, 7.616918355380145e-07, 0.987819, 0.652773, 0.045581, 7.653882845286907e-07, 0.987926, 0.66025, 0.05175, 7.690856762505547e-07, 0.987945, 0.667748, 0.058329, 7.727821252412307e-07, 0.987874, 0.675267, 0.065257, 7.764795169630953e-07, 0.987714, 0.682807, 0.072489, 7.801759659537711e-07, 0.987464, 0.690366, 0.07999, 7.838733576756356e-07, 0.987124, 0.697944, 0.087731, 7.875707493975009e-07, 0.986694, 0.70554, 0.095694, 7.912671983881759e-07, 0.986175, 0.713153, 0.103863, 7.949645901100406e-07, 0.985566, 0.720782, 0.112229, 7.986610391007162e-07, 0.984865, 0.728427, 0.120785, 8.023584308225811e-07, 0.984075, 0.736087, 0.129527, 8.060548798132567e-07, 0.983196, 0.743758, 0.138453, 8.097522715351219e-07, 0.982228, 0.751442, 0.147565, 8.134496632569854e-07, 0.981173, 0.759135, 0.156863, 8.171461122476616e-07, 0.980032, 0.766837, 0.166353, 8.208435039695264e-07, 0.978806, 0.774545, 0.176037, 8.245399529602022e-07, 0.977497, 0.782258, 0.185923, 8.282373446820663e-07, 0.976108, 0.789974, 0.196018, 8.31933793672743e-07, 0.974638, 0.797692, 0.206332, 8.356311853946072e-07, 0.973088, 0.805409, 0.216877, 8.393285771164715e-07, 0.971468, 0.813122, 0.227658, 8.430250261071472e-07, 0.969783, 0.820825, 0.238686, 8.467224178290122e-07, 0.968041, 0.828515, 0.249972, 8.504188668196882e-07, 0.966243, 0.836191, 0.261534, 8.541162585415523e-07, 0.964394, 0.843848, 0.273391, 8.578127075322283e-07, 0.962517, 0.851476, 0.285546, 8.615100992540928e-07, 0.960626, 0.859069, 0.29801, 8.652065482447686e-07, 0.95872, 0.866624, 0.31082, 8.689039399666336e-07, 0.956834, 0.874129, 0.323974, 8.726013316884974e-07, 0.954997, 0.881569, 0.337475, 8.762977806791736e-07, 0.953215, 0.888942, 0.351369, 8.799951724010385e-07, 0.951546, 0.896226, 0.365627, 8.83691621391714e-07, 0.950018, 0.903409, 0.380271, 8.873890131135783e-07, 0.948683, 0.910473, 0.395289, 8.910854621042544e-07, 0.947594, 0.917399, 0.410665, 8.94782853826119e-07, 0.946809, 0.924168, 0.426373, 8.984802455479831e-07, 0.946392, 0.930761, 0.442367, 9.021766945386596e-07, 0.946403, 0.937159, 0.458592, 9.058740862605238e-07, 0.946903, 0.943348, 0.47497, 9.095705352511997e-07, 0.947937, 0.949318, 0.491426, 9.132679269730642e-07, 0.949545, 0.955063, 0.50786, 9.169643759637402e-07, 0.95174, 0.960587, 0.524203, 9.206617676856043e-07, 0.954529, 0.965896, 0.540361, 9.243591594074693e-07, 0.957896, 0.971003, 0.556275, 9.28055608398145e-07, 0.961812, 0.975924, 0.571925, 9.317530001200097e-07, 0.966249, 0.980678, 0.587206, 9.354494491106856e-07, 0.971162, 0.985282, 0.602154, 9.391468408325504e-07, 0.976511, 0.989753, 0.61676, 9.428432898232261e-07, 0.982257, 0.994109, 0.631017, 9.465406815450903e-07, 0.988362, 0.998364, 0.644924]

# Properties modified on slice1Display
slice1Display.MapScalars = 1

# Properties modified on slice1Display
slice1Display.Translation = [-200.0, 0.0, 0.0]

# Properties modified on slice1Display.PolarAxes
slice1Display.PolarAxes.Translation = [-200.0, 0.0, 0.0]

# Properties modified on slice1Display
slice1Display.Translation = [-300.0, 0.0, 0.0]

# Properties modified on slice1Display.PolarAxes
slice1Display.PolarAxes.Translation = [-300.0, 0.0, 0.0]

# Properties modified on slice1Display
slice1Display.MatchBoundariesIgnoringCellOrder = 1

# Properties modified on slice1Display
slice1Display.MatchBoundariesIgnoringCellOrder = 0

# Properties modified on slice1Display.DataAxesGrid
slice1Display.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on slice1Display.DataAxesGrid
slice1Display.DataAxesGrid.GridAxesVisibility = 0

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 0

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1.SliceType)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=slice1.SliceType)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=slice1.SliceType)

# set active source
SetActiveSource(plane1)

# hide data in view
Hide(plane1, renderView1)

# set active source
SetActiveSource(plane1)

# show data in view
plane1Display = Show(plane1, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(plane1, renderView1)

# set active source
SetActiveSource(neuron_mesh_0vtm)

# hide data in view
Hide(magnetic_field_0vtk, renderView1)

# set active source
SetActiveSource(magnetic_field_0vtk)

# show data in view
magnetic_field_0vtkDisplay = Show(magnetic_field_0vtk, renderView1, 'StructuredGridRepresentation')

# hide data in view
Hide(magnetic_field_0vtk, renderView1)

# set active source
SetActiveSource(neuron_mesh_0vtm)

# Properties modified on neuron_mesh_0vtmDisplay.DataAxesGrid
neuron_mesh_0vtmDisplay.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on neuron_mesh_0vtmDisplay.DataAxesGrid
neuron_mesh_0vtmDisplay.DataAxesGrid.GridAxesVisibility = 0

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 1

# Properties modified on renderView1.AxesGrid
renderView1.AxesGrid.Visibility = 0

# Properties modified on neuron_mesh_0vtmDisplay.DataAxesGrid
neuron_mesh_0vtmDisplay.DataAxesGrid.GridAxesVisibility = 1

# Properties modified on neuron_mesh_0vtmDisplay.DataAxesGrid
neuron_mesh_0vtmDisplay.DataAxesGrid.XTitle = 'X, μm '
neuron_mesh_0vtmDisplay.DataAxesGrid.YTitle = 'Y, μm '
neuron_mesh_0vtmDisplay.DataAxesGrid.ZTitle = 'Z, μm '

# set active source
SetActiveSource(plane1)

# set active source
SetActiveSource(slice1)

# Properties modified on slice1Display
slice1Display.Translation = [-400.0, 0.0, 0.0]

# Properties modified on slice1Display.PolarAxes
slice1Display.PolarAxes.Translation = [-400.0, 0.0, 0.0]

# save data
SaveData('/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/magfield sim.pvd', proxy=slice1, PointDataArrays=['B'])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(3127, 1748)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [1850.1795158423465, 289.47875275519687, 1533.743637184458]
renderView1.CameraFocalPoint = [1.5962569601849468e-13, 149.99999999999986, 28.29049986600873]
renderView1.CameraViewUp = [-0.6286015263734704, -0.043081527907695635, 0.7765333882030326]
renderView1.CameraParallelScale = 511.3560164767177

# current camera placement for renderView2
renderView2.CameraPosition = [1850.1795158423465, 289.47875275519687, 1533.743637184458]
renderView2.CameraFocalPoint = [1.5962569601849468e-13, 149.99999999999986, 28.29049986600873]
renderView2.CameraViewUp = [-0.6286015263734704, -0.043081527907695635, 0.7765333882030326]
renderView2.CameraParallelScale = 511.3560164767177


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------