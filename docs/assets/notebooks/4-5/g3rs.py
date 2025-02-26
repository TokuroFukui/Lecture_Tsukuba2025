#--------
# Modules
#--------
## Public modules
import numpy as np
import matplotlib.pyplot as plt

## Private modules
from physconst import pi
import gem_nt


#-----------------------------
# Parameters of G3RS potential
#-----------------------------
vc = np.array([-5.0, -230.0, 2000.0])
rc = np.array([2.5, 0.942, 0.447])
vt = np.array([-7.5, -67.5, 67.5])
rt = np.array([2.5, 1.2, 0.447])
    

#-----------------------------------
# Radial function of G3RS potential
#-----------------------------------
def g3rs_rad(r, v0, r0):
    vg3rs = 0.0
    for i in range(3):
        vg3rs += v0[i] * np.exp(-(r / r0[i])**2)
    return vg3rs
    

#----------------
# Plot G3RS 3E-1
#----------------
def plt_g3rs(irmx, rmx, dr):
    vpot = np.zeros((irmx, 2))
    for ir in range(irmx):
        r = ir * dr
        c =  g3rs_rad(r, vc, rc) # Central
        t =  g3rs_rad(r, vt, rt) # Tensor
        vpot[ir, 0] = c
        vpot[ir, 1] = t    
    
    r_set = np.linspace(0, rmx, irmx)
    plt.figure(figsize=(16, 4.5))
    plt.subplot(1, 2, 1)
    plt.xlim([0.0, 3.0])
    plt.ylim([-100, 2000])
    plt.axhline(y=0, color="black", linestyle="--", linewidth=1)
    plt.plot(r_set, vpot[:, 0], linewidth=3, label="Central")
    plt.plot(r_set, vpot[:, 1], linewidth=3, label="Tensor")
    plt.title("G3RS 3E-1 potentials")
    plt.xlabel("r (fm)")
    plt.ylabel("$v(r)$ (MeV)")
    plt.tick_params(axis='both', direction='in')
    plt.legend()
    plt.subplots_adjust(wspace=0.3)

    plt.subplot(1, 2, 2)
    plt.xlim([0.0, 3.0])
    plt.ylim([-100, 100])
    plt.axhline(y=0, color="black", linestyle="--", linewidth=1)
    plt.plot(r_set, vpot[:, 0], linewidth=3, label="Central")
    plt.plot(r_set, vpot[:, 1], linewidth=3, label="Tensor")
    plt.title("G3RS 3E-1 potentials")
    plt.xlabel("r (fm)")
    plt.ylabel("$v(r)$ (MeV)")
    plt.tick_params(axis='both', direction='in')
    plt.legend()

    plt.show()


#------------------------
# Matrix elements of G3RS
#------------------------
def me_g3rs(idxmx, nbmx, bmn, rho):
    """
    idxmx: int, size of matrices （nbmx x 2）
    nbmx: int, number of Gaussian basis functions
    bmn, rho: Gaussian range parameters
    
    Return values:
        nu: Gaussian range parameter (1.0 / b**2)
        Nfac: Gaussian normalization factor
        Nij: Norm matrix of size idxmx x idxmx
        Hij: Hamiltonian matrix of size idxmx x idxmx
        V00, V22, V02: Interaction matrices of size nbmx x nbmx for visualization
    """

    ## Arrays
    Hij = np.zeros((idxmx, idxmx)) # Hamiltonian-matrix elements
    V00 = np.zeros((nbmx, nbmx))   # For visualization
    V02 = np.zeros((nbmx, nbmx))   # For visualization
    V22 = np.zeros((nbmx, nbmx))   # For visualization
            
    ## Common GEM calculations
    nu, Nfac, Nij, Tij = gem_nt.get_nt(idxmx, nbmx, bmn, rho)

    ## Calculation of matrix elements
    for idx in range(idxmx):
        li = int(idx / nbmx) * 2
        i = int(idx - nbmx * li / 2)

        for jdx in range(idx + 1):
            lj = int(jdx / nbmx) * 2
            j = int(jdx - nbmx * lj / 2)

            wc1 = 0.0
            wc2 = 0.0
            wt1 = 0.0
            wt2 = 0.0
            for k in range(3):
                nuc = 1.0 / rc[k]**2
                nut = 1.0 / rt[k]**2
                wc1 += vc[k] * (nu[idx] + nu[jdx] + nuc)**(-1.5)
                wc2 += vc[k] * (nu[idx] + nu[jdx] + nuc)**(-3.5)
                wt1 += vt[k] * (nu[idx] + nu[jdx] + nut)**(-2.5)
                wt2 += vt[k] * (nu[idx] + nu[jdx] + nut)**(-3.5)

            wc1 *= np.sqrt(pi) * 0.25   # 1/4
            wc2 *= np.sqrt(pi) * 0.9375 # 15/16
            wt1 *= np.sqrt(pi) * 0.375  # 3/8
            wt2 *= np.sqrt(pi) * 0.9375 # 15/16

            if li == lj and li == 0:
                Vij = Nfac[idx] * Nfac[jdx] * wc1
                V00[i, j] = Vij
            elif li == lj and li == 2:
                Vij = Nfac[idx] * Nfac[jdx] * (wc2 - 2.0 * wt2)
                V22[i, j] = Vij
            else:
                Vij = 2.0 * np.sqrt(2.0) * Nfac[idx] * Nfac[jdx] * wt1
                V02[i, j] = Vij

            Hij[idx, jdx] = Tij[idx, jdx] + Vij
            Hij[jdx, idx] = Hij[idx, jdx]
            V00[j, i] = V00[i, j]
            V22[j, i] = V22[i, j]
            V02[j, i] = V02[i, j]

    return nu, Nfac, Nij, Hij, V00, V22, V02