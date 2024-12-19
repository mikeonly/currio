from neuron import h            # , gui (to run GUI as well)

soma = h.Section(name="soma")
dend = h.Section(name="dendrite")

dend.connect(soma(1))

soma.L = 50                     # [um] length
soma.diam = 50                  # [um]
soma.nseg = 1
soma.insert('hh')               # hodgkin-huxley mechanism

dend.L = 200                    # [um]
dend.diam = 2                   # [..] all lengths are in um
dend.nseg = 3                   # because transmembrane voltage varies across the length, add more compartments
dend.insert('pas')
dend.e_pas = -65
