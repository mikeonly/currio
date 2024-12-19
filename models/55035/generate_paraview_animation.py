# trace generated using paraview version 5.13.0-RC1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML MultiBlock Data Reader'
neuron_mesh_0vtm = XMLMultiBlockDataReader(registrationName='neuron_mesh_0.vtm*', FileName=['/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_0.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_1.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_2.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_3.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_4.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_5.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_6.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_7.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_8.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_9.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_10.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_11.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_12.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_13.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_14.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_15.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_16.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_17.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_18.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_19.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_20.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_21.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_22.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_23.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_24.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_25.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_26.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_27.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_28.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_29.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_30.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_31.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_32.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_33.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_34.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_35.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_36.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_37.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_38.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_39.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_40.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_41.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_42.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_43.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_44.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_45.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_46.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_47.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_48.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_49.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_50.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_51.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_52.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_53.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_54.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_55.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_56.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_57.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_58.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_59.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_60.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_61.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_62.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_63.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_64.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_65.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_66.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_67.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_68.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_69.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_70.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_71.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_72.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_73.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_74.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_75.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_76.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_77.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_78.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_79.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_80.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_81.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_82.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_83.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_84.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_85.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_86.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_87.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_88.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_89.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_90.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_91.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_92.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_93.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_94.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_95.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_96.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_97.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_98.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_99.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_100.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_101.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_102.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_103.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_104.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_105.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_106.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_107.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_108.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_109.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_110.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_111.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_112.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_113.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_114.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_115.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_116.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_117.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_118.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_119.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_120.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_121.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_122.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_123.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_124.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_125.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_126.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_127.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_128.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_129.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_130.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_131.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_132.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_133.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_134.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_135.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_136.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_137.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_138.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_139.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_140.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_141.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_142.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_143.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_144.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_145.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_146.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_147.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_148.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_149.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_150.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_151.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_152.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_153.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_154.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_155.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_156.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_157.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_158.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_159.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_160.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_161.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_162.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_163.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_164.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_165.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_166.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_167.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_168.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_169.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_170.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_171.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_172.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_173.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_174.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_175.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_176.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_177.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_178.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_179.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_180.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_181.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_182.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_183.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_184.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_185.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_186.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_187.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_188.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_189.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_190.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_191.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_192.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_193.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_194.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_195.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_196.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_197.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_198.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_199.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_200.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_201.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_202.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_203.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_204.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_205.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_206.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_207.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_208.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_209.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_210.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_211.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_212.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_213.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_214.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_215.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_216.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_217.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_218.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_219.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_220.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_221.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_222.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_223.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_224.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_225.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_226.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_227.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_228.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_229.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_230.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_231.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_232.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_233.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_234.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_235.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_236.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_237.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_238.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_239.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_240.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_241.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_242.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_243.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_244.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_245.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_246.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_247.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_248.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_249.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_250.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_251.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_252.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_253.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_254.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_255.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_256.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_257.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_258.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_259.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_260.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_261.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_262.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_263.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_264.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_265.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_266.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_267.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_268.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_269.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_270.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_271.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_272.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_273.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_274.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_275.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_276.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_277.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_278.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_279.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_280.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_281.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_282.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_283.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_284.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_285.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_286.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_287.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_288.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_289.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_290.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_291.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_292.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_293.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_294.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_295.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_296.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_297.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_298.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_299.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_300.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_301.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_302.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_303.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_304.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_305.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_306.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_307.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_308.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_309.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_310.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_311.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_312.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_313.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_314.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_315.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_316.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_317.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_318.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_319.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_320.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_321.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_322.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_323.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_324.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_325.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_326.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_327.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_328.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_329.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_330.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_331.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_332.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_333.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_334.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_335.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_336.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_337.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_338.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_339.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_340.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_341.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_342.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_343.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_344.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_345.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_346.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_347.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_348.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_349.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_350.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_351.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_352.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_353.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_354.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_355.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_356.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_357.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_358.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_359.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_360.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_361.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_362.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_363.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_364.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_365.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_366.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_367.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_368.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_369.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_370.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_371.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_372.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_373.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_374.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_375.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_376.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_377.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_378.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_379.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_380.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_381.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_382.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_383.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_384.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_385.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_386.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_387.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_388.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_389.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_390.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_391.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_392.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_393.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_394.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_395.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_396.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_397.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_398.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_399.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_400.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_401.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_402.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_403.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_404.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_405.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_406.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_407.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_408.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_409.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_410.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_411.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_412.vtm', '/Users/mf/Documents/Helmholtz Institue Mainz/Neuron/obliques/vtk_time_series/neuron_mesh_413.vtm'])

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.AxesGrid = 'Grid Axes 3D Actor'
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraFocalDisk = 1.0
renderView2.LegendGrid = 'Legend Grid Actor'
renderView2.PolarGrid = 'Polar Grid Actor'
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView2, layout=layout1, hint=2)

# link cameras in two views
AddCameraLink(renderView2, renderView1, 'CameraLink0')

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(neuron_mesh_0vtm)

# show data in view
neuron_mesh_0vtmDisplay = Show(neuron_mesh_0vtm, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
neuron_mesh_0vtmDisplay.Representation = 'Surface'

# show color bar/color legend
neuron_mesh_0vtmDisplay.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# get 2D transfer function for 'diameters'
diametersTF2D = GetTransferFunction2D('diameters')

# get color transfer function/color map for 'diameters'
diametersLUT = GetColorTransferFunction('diameters')
diametersLUT.TransferFunction2D = diametersTF2D
diametersLUT.RGBPoints = [0.8999999761581421, 0.231373, 0.298039, 0.752941, 4.195500075817108, 0.865003, 0.865003, 0.865003, 7.491000175476074, 0.705882, 0.0156863, 0.14902]
diametersLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'diameters'
diametersPWF = GetOpacityTransferFunction('diameters')
diametersPWF.Points = [0.8999999761581421, 0.0, 0.5, 0.0, 7.491000175476074, 1.0, 0.5, 0.0]
diametersPWF.ScalarRangeInitialized = 1

# set active view
SetActiveView(renderView2)

# show data in view
neuron_mesh_0vtmDisplay_1 = Show(neuron_mesh_0vtm, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
neuron_mesh_0vtmDisplay_1.Representation = 'Surface'

# show color bar/color legend
neuron_mesh_0vtmDisplay_1.SetScalarBarVisibility(renderView2, True)

# reset view to fit data
renderView2.ResetCamera(False, 0.9)

# set active view
SetActiveView(renderView1)

# set scalar coloring
ColorBy(neuron_mesh_0vtmDisplay, ('POINTS', 'voltages'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(diametersLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
neuron_mesh_0vtmDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
neuron_mesh_0vtmDisplay.SetScalarBarVisibility(renderView1, True)

# get 2D transfer function for 'voltages'
voltagesTF2D = GetTransferFunction2D('voltages')

# get color transfer function/color map for 'voltages'
voltagesLUT = GetColorTransferFunction('voltages')
voltagesLUT.TransferFunction2D = voltagesTF2D
voltagesLUT.RGBPoints = [-65.00000000000001, 0.231373, 0.298039, 0.752941, -64.9921875, 0.865003, 0.865003, 0.865003, -64.984375, 0.705882, 0.0156863, 0.14902]
voltagesLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'voltages'
voltagesPWF = GetOpacityTransferFunction('voltages')
voltagesPWF.Points = [-65.00000000000001, 0.0, 0.5, 0.0, -64.984375, 1.0, 0.5, 0.0]
voltagesPWF.ScalarRangeInitialized = 1

# set active view
SetActiveView(renderView2)

# set scalar coloring
ColorBy(neuron_mesh_0vtmDisplay_1, ('POINTS', 'voltages'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(diametersLUT, renderView2)

# rescale color and/or opacity maps used to include current data range
neuron_mesh_0vtmDisplay_1.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
neuron_mesh_0vtmDisplay_1.SetScalarBarVisibility(renderView2, True)

# set scalar coloring
ColorBy(neuron_mesh_0vtmDisplay_1, ('CELLS', 'currents'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(voltagesLUT, renderView2)

# rescale color and/or opacity maps used to include current data range
neuron_mesh_0vtmDisplay_1.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
neuron_mesh_0vtmDisplay_1.SetScalarBarVisibility(renderView2, True)

# get 2D transfer function for 'currents'
currentsTF2D = GetTransferFunction2D('currents')

# get color transfer function/color map for 'currents'
currentsLUT = GetColorTransferFunction('currents')
currentsLUT.TransferFunction2D = currentsTF2D
currentsLUT.RGBPoints = [-5.573893204197572e-20, 0.231373, 0.298039, 0.752941, 7.596658518133421e-21, 0.865003, 0.865003, 0.865003, 7.093224907824256e-20, 0.705882, 0.0156863, 0.14902]
currentsLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'currents'
currentsPWF = GetOpacityTransferFunction('currents')
currentsPWF.Points = [-5.573893204197572e-20, 0.0, 0.5, 0.0, 7.093224907824256e-20, 1.0, 0.5, 0.0]
currentsPWF.ScalarRangeInitialized = 1

# set active view
SetActiveView(renderView1)

# Rescale transfer function
voltagesLUT.RescaleTransferFunction(-70.0, 20.0)

# Rescale transfer function
voltagesPWF.RescaleTransferFunction(-70.0, 20.0)

# Rescale 2D transfer function
voltagesTF2D.RescaleTransferFunction(-70.0, 20.0, 0.0, 1.0)

# get color legend/bar for voltagesLUT in view renderView1
voltagesLUTColorBar = GetScalarBar(voltagesLUT, renderView1)
voltagesLUTColorBar.Title = 'voltages'
voltagesLUTColorBar.ComponentTitle = ''

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6.1g'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6.1e'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6.3g'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6.3f'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6.3a'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6.3b'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6.3c'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6.3d'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6.3e'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6.3g'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6.2g'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6.0g'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#6g'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-#g'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.RangeLabelFormat = '%-g'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.Title = 'Voltage, mV'

# Properties modified on voltagesLUTColorBar
voltagesLUTColorBar.HorizontalTitle = 1

# set active view
SetActiveView(renderView2)

# Rescale transfer function
currentsLUT.RescaleTransferFunction(-1e-06, 1000000.0)

# Rescale transfer function
currentsPWF.RescaleTransferFunction(-1e-06, 1000000.0)

# Rescale 2D transfer function
currentsTF2D.RescaleTransferFunction(-1e-06, 1000000.0, 0.0, 1.0)

# Rescale transfer function
currentsLUT.RescaleTransferFunction(-1e-06, 1e-06)

# Rescale transfer function
currentsPWF.RescaleTransferFunction(-1e-06, 1e-06)

# Rescale 2D transfer function
currentsTF2D.RescaleTransferFunction(-1e-06, 1e-06, 0.0, 1.0)

# get color legend/bar for currentsLUT in view renderView2
currentsLUTColorBar = GetScalarBar(currentsLUT, renderView2)
currentsLUTColorBar.Title = 'currents'
currentsLUTColorBar.ComponentTitle = ''

# Properties modified on currentsLUTColorBar
currentsLUTColorBar.Title = 'Current, mA'

# Properties modified on currentsLUTColorBar
currentsLUTColorBar.HorizontalTitle = 1

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(4371, 2324)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [16.055433063298977, 177.24307925123748, 1727.8603074959524]
renderView1.CameraFocalPoint = [16.055433063298977, 177.24307925123748, -0.6406358437920403]
renderView1.CameraParallelScale = 449.1302372689965

# current camera placement for renderView2
renderView2.CameraPosition = [16.055433063298977, 177.24307925123748, 1727.8603074959524]
renderView2.CameraFocalPoint = [16.055433063298977, 177.24307925123748, -0.6406358437920403]
renderView2.CameraParallelScale = 449.1302372689965


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