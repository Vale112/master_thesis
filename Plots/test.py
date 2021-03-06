# from scipy.constants import physical_constants as pcon
# import scipy.constants as const
import numpy as np

def Pol(kx, ky, E, off=0):
    me = 9.1093837015e-31
    e = 1.602176634e-19
    E *= e
    A = np.sqrt(8*me*E*np.pi**2/(6.62607015e-34**2))
    k = np.sqrt(kx**2 + ky**2)*1e10
    print('Polarisation ', np.cos(np.arcsin(k/A) - 11*np.pi/30 + off*np.pi/180)**2)
    return

def Oxid(Roh1, Roh2, M1, M2, SD):
    SD *= 1e-8
    SD2 = (Roh1 * SD * (M1 + M2))/(M1*Roh2)
    SD2 *= 1e8
    # print('Die Schichtdicke ist (A)', SD2)
    return SD2

def Mono(Roh1, Roh2, M1, M2, SD, Lage):
    SD2 = Oxid(Roh1, Roh2, M1, M2, SD)
    ML = SD2/Lage
    print('Die Schichtdicke ist (A)', SD2)
    print('und entspricht Anzahl ML', ML)

# Pol(0.068565, 1.7827, 33.75, 0)
# Pol(0.03918, 1.7925, 33.75)
# Pol(0, 1.8219, 33.75)
# Pol(0.029385, 1.8121, 33.75, 90)
# Pol(0.07334, 1.4478, 27.55, 0)
# Pol(0.02447, 1.814, 27.55, 90)

Mono(8.908, 6.72, 58.6, 74.69, 0.3*35, 4.17/np.sqrt(3))

