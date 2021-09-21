import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import numpy as np
import matplotlib.pyplot as plt

from PhaseDiagram import PhaseSphere


P = np.array([  
            [0,0,1],
            [1,0,0],
            [0,1,0]
             ])

Gz = np.array([  
            [0,1,0],
            [1,0,0],
            [0,0,0]
             ])
Gx = P.T@Gz@P
Gy = P.T@Gx@P


Gpz = np.array([  
            [0,0,1],
            [0,0,1],
            [1,1,0]
             ])
Gpx = P.T@Gpz@P
Gpy = P.T@Gpx@P


Kz = np.diag([0,0,1])
Kx = P.T@Kz@P
Ky = P.T@Kx@P


# Calculates the classical ground state of a Heisenverg-Kitaev-Gamma-Gamma'-J2-J3 model.
# See Songvilay et al., “Kitaev Interactions in the Co Honeycomb Antiferromagnets
# Na$_3$Co$_2$SbO$_6$ and Na$_2$Co$_2$TeO$_6$.”, Phys. Rev. B 2020 for details
def get_energy(model, free_params, X, Y, Z):
    
    model[free_params[0]] = X
    model[free_params[1]] = Y
    model[free_params[2]] = Z
    
    J = np.eye(3)
 
    J1 = np.multiply.outer(model['J'], J)
    J2 = np.multiply.outer(model['J2'],J)
    J3 = np.multiply.outer(model['J3'],J)
    
    Kppp = np.multiply.outer(model['K'],Kx+Ky+Kz)
    Kppm = np.multiply.outer(model['K'],Kx+Ky-Kz)

    Gppp = np.multiply.outer(model['G'],Gx+Gy+Gz)
    Gppm = np.multiply.outer(model['G'],Gx+Gy-Gz)
    
    GPppp = np.multiply.outer(model['Gp'],Gpx+Gpy+Gpz)
    GPppm = np.multiply.outer(model['Gp'],Gpx+Gpy-Gpz)
    

    
    fmTens =  3*J1 + Kppp + Gppp + GPppp + 6*J2 + 3*J3
    afTens = -3*J1 - Kppp - Gppp - GPppp + 6*J2 - 3*J3
    zzTens =  J1   + Kppm + Gppm + GPppm - 2*J2 - 3*J3
    stTens = -J1   - Kppm - Gppm - GPppm - 2*J2 + 3*J3
    
    
    E = np.vstack((
        np.min(np.linalg.eigh(fmTens)[0],axis=1),
        np.min(np.linalg.eigh(afTens)[0],axis=1),
        np.min(np.linalg.eigh(zzTens)[0],axis=1),
        np.min(np.linalg.eigh(stTens)[0],axis=1)
    ))
    
    return E


fixed_parameters = {
        'J3': 0.1,
        'J2': 0,
        'Gp': 0
        }

def phase(j,k,g):
    return np.argmin(get_energy(fixed_parameters,['J','K','G'], j, k, g),axis=0)
    

ps = PhaseSphere(phase, ['FM', 'AFM', 'ZZ', 'S'], param_names = ['J','K','Γ'],projection="azimuthal")

ps.refine(8)

ps.plot()

plt.show()
