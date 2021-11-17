# Dieses Skript ist zum Kalkulieren von Schichtdicken der QCM
import numpy as np

def Oxid(Roh1, Roh2, M1, M2, SD, n=1):   # Berechnet die Schcihtdicke für Oxide, wenn die Aufdampfrate des Materials 1 bekannt ist, kann die Komposition mit Material 2 bestimmt werden.
    # Roh sind die Dichten und M die Molaren Massen, SD die Schichtdicke des Materials, wenn die Stochimetrie 1:n für Material 1 zum 2. ist.
    SD *= 1e-8
    SD2 = (Roh1 * SD * (M1 + M2*n))/(M1*Roh2)
    SD2 *= 1e8
    # print('Die Schichtdicke ist (A)', SD2)
    return SD2

def Mono(Roh1, Roh2, M1, M2, SD, Lage): # Berechnet die Anzahl Monolagen in abhängigkeit des Lagenabstandes (fcc(111) = a/sqrt(3); fcc(100) = a/2)
    SD2 = Oxid(Roh1, Roh2, M1, M2, SD)
    ML = SD2/Lage
    print('Die Schichtdicke ist (A)', SD2)
    print('und entspricht Anzahl ML', ML)

Mono(8.908, 6.72, 58.6, 74.69, 0.7*15, 4.17/np.sqrt(3))
Mono(8.908, 6.72, 58.6, 74.69, 0.7*35, 4.17/np.sqrt(3))

