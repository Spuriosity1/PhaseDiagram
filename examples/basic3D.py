import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import numpy as np
import matplotlib.pyplot as plt

from PhaseDiagram import PhaseSphere


def phase(j,k,g):
    return np.argmin([(j- k)**2, g*k*j - k**2*g - j**2*k, k, g**2 + j*k], axis=0)
    

ps = PhaseSphere(phase, ['A', 'B', 'C','D'], param_names = ['X1','X2','X3'],projection="azimuthal")
ps.set_initpts(ntheta=20,nphi=50)
ps.refine(8)
ps.plot(show_triangulation=True)


ps = PhaseSphere(phase, ['A', 'B', 'C','D'], param_names = ['X1','X2','X3'],projection="mercator")
ps.refine(8)
ps.plot(show_triangulation=True)

plt.show()
