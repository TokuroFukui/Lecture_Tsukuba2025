#--------
# Modules
#--------
## Public modules
import numpy as np
import mpmath as mp

## Private modules
from physconst import pi, hc, muac


#--------------------------------------------------
# Common GEM calculations, norm, and kinetic energy
#--------------------------------------------------
def get_nt(idxmx, nbmx, bmn, rho):
    """
    idxmx: int, size of matrices （nbmx x 2）
    nbmx: int, number of Gaussian basis functions
    bmn, rho: Gaussian range parameters
    
    Return values:
        nu: Gaussian range parameter (1.0 / b**2)
        Nfac: Gaussian normalization factor
        Nij: Norm matrix of size idxmx x idxmx
        Tij: Kinetic-energy matrix of size idxmx x idxmx
    """
    
    ## Arrays
    nu = np.zeros(idxmx)           # Range parameter
    Nfac = np.zeros(idxmx)         # Normalization factor
    Nij = np.zeros((idxmx, idxmx)) # Norm-matrix elements
    Tij = np.zeros((idxmx, idxmx)) # Matrix elements of Kinetic energy 

    ## Range parameter and normalization factor
    for idx in range(idxmx):
        l = int(idx / nbmx) * 2
        i = int(idx - nbmx * l / 2)

        b = bmn * rho**i
        nu[idx] = 1.0 / b**2
        Nfac[idx] = np.sqrt(2.0**(l + 2) / mp.fac2(2 * l + 1)) * ((2.0 * nu[idx])**(2 * l + 3) / pi)**(0.25)
        
    ## Matrix elements of norm and kinetic energy
    for idx in range(idxmx):
        li = int(idx / nbmx) * 2

        for jdx in range(idx + 1):
            lj = int(jdx / nbmx) * 2

            beta = 2.0 * np.sqrt(nu[idx] * nu[jdx]) / (nu[idx] + nu[jdx])
            Nij[idx, jdx] = beta**(li + 1.5) if li == lj else 0.0
            Nij[jdx, idx] = Nij[idx, jdx]

            coeff_T = hc**2 / muac * (2.0 * li + 3.0) * nu[idx] * nu[jdx] / (nu[idx] + nu[jdx])
            Tij[idx, jdx] = coeff_T * Nij[idx, jdx]
            
    return nu, Nfac, Nij, Tij