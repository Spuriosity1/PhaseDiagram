import sys
import numpy as np
import matplotlib.pyplot as plt

from PhaseDiagram import PhasePlane


def phase(X, Y):
    return np.where(X**2 + 4*Y**2 > 1, 1, 0) + np.where(X + Y > 0, 1, 0)

p = PhasePlane(phase, ['A','B','C'], ['x1','x2'])
p.set_initpts(np.linspace(-1.5,1.5,10),np.linspace(-1.5,1.5,10))

if len(sys.argv) == 1:
    p.refine(6)
else:
    p.refine(int(sys.argv[1]))

p.plot()

plt.show()
