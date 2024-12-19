from neuron import h, gui
from neuron.units import ms, mV, μM
import matplotlib.pyplot as plt
# note that in terminal all other files are loaded relative to the 
# path from which python was invoked. it seems that additional functions
# from files other than mosinit.hoc are not loaded if python is not invoked
# in the folder with mosinit.hoc
h.load_file('obliques/mosinit.hoc')

t = h.Vector().record(h._ref_t)
v = h.Vector().record(h.soma[0](0.5)._ref_v)

h.finitialize(-65 * mV)
h.continuerun(100 * ms)

plt.plot(t, v)
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
plt.show()

ps = h.PlotShape(True)
