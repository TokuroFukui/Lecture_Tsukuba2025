#--------
# Modules
#--------
## Public modules
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import gamma, hyp1f1

## Private modules
from physconst import pi, hc, m_av
import gem_nt


#---------------------
# Get meson parameters
#---------------------
def get_mesoninfo(meson, meson_bundle):
    """
    Args:
        meson: string, a character from "pesrod"
    
    Returns:
        mass: float, meson mass
        gsq: float, coupling constant
        Lam: float, cutoff momentum
    """
    
    meson_param = meson_bundle["meson_param"]
    mass = meson_param[meson][0]
    gsq  = meson_param[meson][1]
    Lam  = meson_param[meson][2]
    
    return mass, gsq, Lam


#-----------------------------
# Radial initegration G_ij^(n)
# using numerical integration
#-----------------------------
def g_ninteg(m, nu, n):
    """

    .. math::

        \\int_0^\\infty dr\\, r^n e^{-nu\\, r - m\\, r}

    Args:
        m: float, meson mass or cutoff momentum
        nu: float, Gaussian range parameter
        n: int, power of r   
    """
    
    gijn = 0.0
    if n > 0:
        gijn, err = quad(lambda r: r**n * np.exp(-nu * r**2 - m * r), 0.0, np.inf)
        
    return gijn


#----------------------------------------
# Common structure of matrix elements (1)
#----------------------------------------
def gg1(mass, Lam, n, nu):
    """
    Args:
        mass: float, meson mass
        Lam: float, cutoff momentum
        n: int, power of r
        nu: float, Gaussian range parameters
    
    Returns:
        float, Gij^{(n)}(mass) - Gij^{(n)}(Lam)
    """

    return g_ninteg(mass, nu, n) - g_ninteg(Lam, nu, n)


#----------------------------------------
# Common structure of matrix elements (2)
#----------------------------------------
def gg2(mass, Lam, n, nu):
    """
    Args:
        mass: float, meson mass
        Lam: float, cutoff momentum
        n: int, power of r
        nu: float, Gaussian range parameters
    
    Returns:
        float, mass * Gij^{(n)}(mass) - Lam * Gij^{(n)}(Lam)
    """

    return mass * g_ninteg(mass, nu, n) - Lam * g_ninteg(Lam, nu, n)


#---------------------------------------
# Matrix elements for pseudoscalar meson
#---------------------------------------
def me_ps(mass, Lam, li, lj, nuij):
    """
    Args:
        mass: float, meson mass
        Lam: float, cutoff momentum
        li, lj: int, orbital angular momenta
        nuij: float, Gaussian range parameter
    
    Returns:
        meC: float, central matrix element
        meT: float, tensor matrix element
    """

    Lam2m2 = Lam**2 - mass**2
    ## Central force
    if li == lj:
        meC = g_ninteg(mass, nuij, 2 * li + 1) \
            - g_ninteg(Lam, nuij, 2 * li + 1) \
            - 0.5 * Lam2m2 / Lam * g_ninteg(Lam, nuij, 2 * li + 2)
        meC *= (mass / m_av)**2 / 12.0
    else:
        meC = 0.0
        
    ## Tensor force
    lij = li + lj
    if lij == 0:
        cg6j = 0.0
    elif lij == 2:
        cg6j = 2.0 * np.sqrt(2.0)
    elif lij == 4:
        cg6j = -2.0
              
    g3 = lambda m: 3.0 / m_av**2 * g_ninteg(m, nuij, lij - 1) \
                 + 3.0 * m / m_av**2 * g_ninteg(m, nuij, lij) \
                 + (m / m_av)**2 * g_ninteg(m, nuij, lij + 1)
             
    meT = g3(mass) - g3(Lam) \
        -0.5 * Lam2m2 / m_av**2 \
        * (g_ninteg(Lam, nuij, lij + 1) + Lam * g_ninteg(Lam, nuij, lij + 2))
    meT *= cg6j / 12.0
    
    return meC, meT


#---------------------------------
# Matrix elements for scalar meson
#---------------------------------
def me_s(mass, Lam, l, nuij, nuj):
    """
    Args:
        mass: float, meson mass
        Lam: float, cutoff momentum
        l: int, orbital angular momentum (call this function under li == lj)
        nuij, nuj: float, Gaussian range parameters
    
    Returns:
        meC: float, central matrix element
        meSO: float, spin-orbit matrix element
    """
    
    Lam2m2 = Lam**2 - mass**2
    gij_2lp1 = g_ninteg(Lam, nuij, 2 * l + 1)
    gg1_2lm1 = gg1(mass, Lam, 3, nuij)
    gg2_2l   = gg2(mass, Lam, 4, nuij)
    gg1_2lp1 = gg1(mass, Lam, 2 * l + 1, nuij)
    gg2_2lp2 = gg2(mass, Lam, 2 * l + 2, nuij)
    gg1_2lp3 = gg1(mass, Lam, 2 * l + 3, nuij)

    ## Central force
    meC = gg1_2lp1 - 0.5 * Lam2m2 / Lam * g_ninteg(Lam, nuij, 2 * l + 2)
    meC *= -(1.0 - 0.25 * (mass / m_av)**2)

    ## Velocity-dependent term
    meC_vel = (mass**2 - 8.0 * (l + 1.0) * nuj) * gg1_2lp1 \
            + 4.0 * nuj * gg2_2lp2 \
            - 0.5 * Lam2m2 / Lam * (Lam**2 - 4.0 * (2.0 * l + 3.0) * nuj) * g_ninteg(Lam, nuij, 2 * l + 2) \
            + 8.0 * nuj**2 * gg1_2lp3 - 2.0 * Lam2m2 * nuj * g_ninteg(Lam, nuij, 2 * l + 3) \
            - 4.0 * Lam2m2 / Lam * nuj**2 * g_ninteg(Lam, nuij, 2 * l + 4)
    if l == 2:
        meC_vel += 2.0 * l / m_av**2 * (gg1_2lm1 + gg2_2l) \
            + l / m_av**2 * Lam2m2 * gij_2lp1
    meC += -0.25 / m_av**2 * meC_vel
        
    ## Spin-orbit force
    if l == 2:
        meSO = 1.5 / m_av**2 * (gg1_2lm1 + gg2_2l - 0.5 * Lam2m2 * gij_2lp1) # 1.5 = l(l+1)/4
    else:
        meSO = 0.0
    
    return meC, meSO


#---------------------------------
# Matrix elements for vector meson
#---------------------------------
def me_v(meson, mass, Lam, li, lj, nuij, nuj, meson_bundle):
    """
    Args:
        meson: string, a character from "pesrod"
        mass: float, meson mass
        Lam: float, cutoff momentum
        li, lj: int, orbital angular momenta
        nuij, nuj: float, Gaussian range parameters
    
    Returns:
        meC: float, central matrix element
        meSO: float, spin-orbit matrix element
        meT: float, tensor matrix element
    """
       
    ## Common values
    mm = (mass / m_av)**2
    Lam2m2 = Lam**2 - mass**2
    meson_param2 = meson_bundle["meson_param2"]
    fong = meson_param2[meson][0] # f_v / g_v
    gij_2lp1 = g_ninteg(Lam, nuij, 2 * li + 1)
    gg1_2lm1 = gg1(mass, Lam, 3, nuij)
    gg2_2l   = gg2(mass, Lam, 4, nuij)
        
    ## Central force
    if li == lj:
        gg1_2lp1 = gg1(mass, Lam, 2 * li + 1, nuij)
        gg2_2lp2 = gg2(mass, Lam, 2 * li + 2, nuij)
        gg1_2lp3 = gg1(mass, Lam, 2 * li + 3, nuij)
        
        meC = gg1_2lp1 - 0.5 * Lam2m2 / Lam * g_ninteg(Lam, nuij, 2 * li + 2)
        meC *= 1.0 + 2.0 / 3.0 * mm + 5.0 / 6.0 * fong * mm + 1.0 / 6.0 * fong**2 * mm

        ## Velocity-dependent term
        meC_vel = (mass**2 - 8.0 * (li + 1.0) * nuj) * gg1_2lp1 \
                + 4.0 * nuj * gg2_2lp2 \
                - 0.5 * Lam2m2 / Lam * (Lam**2 - 4.0 * (2.0 * li + 3.0) * nuj) * g_ninteg(Lam, nuij, 2 * li + 2) \
                + 8.0 * nuj**2 * gg1_2lp3 - 2.0 * Lam2m2 * nuj * g_ninteg(Lam, nuij, 2 * li + 3) \
                - 4.0 * Lam2m2 / Lam * nuj**2 * g_ninteg(Lam, nuij, 2 * li + 4)
        if li == 2:
            meC_vel += 2.0 * li / m_av**2 * (gg1_2lm1 + gg2_2l) \
                + li / m_av**2 * Lam2m2 * gij_2lp1
        meC += -0.75 / m_av**2 * meC_vel

    else:
        meC = 0.0
        
    ## Spin-orbit force
    if li == lj and li == 2:
        meSO = 1.5 * (3.0 + 4.0 * fong) / m_av**2 \
             * (gg1_2lm1 + gg2_2l - 0.5 * Lam2m2 * gij_2lp1) # 1.5 = l(l+1)/4
    else:
        meSO = 0.0
    
    ## Tensor force
    lij = li + lj
    if lij == 0:
        cg6j = 0.0
    elif lij == 2:
        cg6j = 2.0 * np.sqrt(2.0)
    elif lij == 4:
        cg6j = -2.0
              
    g3 = lambda m: 3.0 / m_av**2 * g_ninteg(m, nuij, lij - 1) \
                 + 3.0 * m / m_av**2 * g_ninteg(m, nuij, lij) \
                 + (m / m_av)**2 * g_ninteg(m, nuij, lij + 1)
             
    meT = g3(mass) - g3(Lam) \
        -0.5 * (Lam**2 - mass**2) / m_av**2 \
        * (g_ninteg(Lam, nuij, lij + 1) + Lam * g_ninteg(Lam, nuij, lij + 2))
    meT *= -1.0 / 12.0 * cg6j * (1.0 + 2.0 * fong + fong**2)
    
    return meC, meSO, meT


#------------------------
# Isospin matrix elements
#------------------------
def tautau(meson):
    """
    Args:
        meson: string, a character from "pesrod"
    """
    
    if meson in ("p", "d", "r"): # Isovector
        me = -3.0
    elif meson in ("e", "s", "o"): # Isoscalar
        me = 1.0
    else:
        me = 0.0
    
    return me


#------------------------------
# Matrix elements of each meson
#------------------------------
def me_pssv(meson, li, lj, nui, nuj, meson_bundle):
    """
    Args:
        meson: string, a character from "pesrod"
        li, lj: int, orbital angular momenta
        nui, nuj: float, Gaussian range parameters
    
    Returns:
        fac: float, factor for matrix elements
        wC, wSO, wT: float, matrix elements for central, spin-orbit, tensor forces
    """

    mass, gsq, Lam = get_mesoninfo(meson, meson_bundle)
    fac = gsq * tautau(meson)
    nuij = nui + nuj
        
    if meson in ("p", "e"): # Pseudoscalar meson
        wC, wT = me_ps(mass, Lam, li, lj, nuij)
        wSO = 0.0

    elif meson in ("s", "d"): # Scalar meson
        if li == lj:
            wC, wSO = me_s(mass, Lam, li, nuij, nuj)
        else:
            wC = 0.0; wSO = 0.0
        wT  = 0.0
        
    elif meson in ("r", "o"): # Vector meson
        wC, wSO, wT = me_v(meson, mass, Lam, li, lj, nuij, nuj, meson_bundle)
        
    return fac, wC, wSO, wT


#------------------------
# Matrix elements of OBEP
#------------------------
def me_obep(idxmx, nbmx, bmn, rho, meson_bundle):
    """
    Args:
        idxmx: int, size of matrices (2 * nbmx)
        nbmx: int, number of Gaussian basis functions
        bmn, rho: float, Gaussian range parameters
    
    Return values:
        nu: list of Gaussian range parameters
        Nfac: list of normalization factors
        Nij: list of norm matrix elements
        Hij: list of Hamiltonian matrix elements
        V00, V22, V02: list of matrix elements for visualization
    """

    meson_list = meson_bundle["meson_list"]
    print("Mesons included:", meson_list)

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
        nui = nu[idx]

        for jdx in range(idx + 1):
            lj = int(jdx / nbmx) * 2
            j = int(jdx - nbmx * lj / 2)
            nuj = nu[jdx]
            
            Vij_C = 0.0; Vij_SO = 0.0; Vij_T = 0.0
            for meson in meson_list:
                fac, wC, wSO, wT = me_pssv(meson, li, lj, nui, nuj, meson_bundle)
                Vij_C  += fac * wC
                Vij_SO += fac * wSO
                Vij_T  += fac * wT

            if li == lj and li == 0:
                Vij = hc * Nfac[idx] * Nfac[jdx] * Vij_C
                V00[i, j] = Vij
            elif li == lj and li == 2:
                Vij = hc * Nfac[idx] * Nfac[jdx] * (Vij_C + Vij_SO + Vij_T)
                V22[i, j] = Vij
            else:
                Vij = hc * Nfac[idx] * Nfac[jdx] * Vij_T
                V02[i, j] = Vij

            Hij[idx, jdx] = Tij[idx, jdx] + Vij
            Hij[jdx, idx] = Hij[idx, jdx]
            V00[j, i] = V00[i, j]
            V22[j, i] = V22[i, j]
            V02[j, i] = V02[i, j]        

    return nu, Nfac, Nij, Hij, V00, V22, V02


#+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/
#+-*/+-*/ Obsolete functions +-*/+-*/  
#+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/
#--------------------------
# Kahan summation algorithm
#--------------------------
def kahan_sum(value, total, c):
    """
    Kahan summation algorithm

    Args:
        value: float, value to be added
        total: float, current sum
        c: float, compensation for lost bits
    
    Returns
        total: float, updated sum
        c: float, updated compensation
    """

    if abs(value) <= abs(total):
        tmp_sum = total + (value + c)
        c = (value + c) - (tmp_sum - total)
    else:
        tmp_sum = (total + c) + value
        c = (total + c) - (tmp_sum - value)
    total = tmp_sum

    return total, c


#-----------------
# Initegration I_k
#-----------------
def ei_integ(nuij, gamma, k, xasy):
    """
    Args:
        nuij: float, Gaussian range parameter
        gamma: float, gamma = 0.5 * m / nuij
        k: int, power index
        xasy: float, assumed value for asymptotic expansion
    """
    
    x = np.sqrt(nuij) * gamma
    if x < xasy:
        gerfc = np.exp(x**2) * math.erfc(x)
    else:
        gerfc = (1.0 / x - 0.5 / x**3 + 0.75 / x**5 - 1.875 / x**7) / np.sqrt(pi) # Ignore O(x^{-9}) terms
        
    ei_k = 0.0
    if k == 0:
        ei_k = 0.5 * np.sqrt(pi / nuij) * gerfc

    elif k == 1:
        ei_k = 0.5 / nuij

    elif k == 2:
        ei_k = 0.25 * np.sqrt(pi / nuij**3) * gerfc \
            + 0.5 * gamma / nuij

    elif k == 3:
        ei_k = 0.5 * (x**2 + 1.0) / nuij**2

    elif k == 4:
        ei_k = 0.375 * np.sqrt(pi / nuij**5) * gerfc \
            + 0.25 * gamma * (2.0 * x**2 + 3.0) / nuij**2

    elif k == 5:
        ei_k = 0.5 * (x**2 * (x**2 + 2.0) + 2.0) / nuij**3

    elif k == 6:
        ei_k = 0.9375 * np.sqrt(pi / nuij**7) * gerfc \
            + 0.125 * gamma * (2.0 * x**2 * (2.0 * x**2 + 5.0) + 15.0) / nuij**3

    elif k == 7:
        ei_k = 0.5 * (x**2 * (x**2 * (x**2 + 3.0) + 6.0) + 6.0) / nuij**4
            
    return ei_k


#-----------------------------
# Radial initegration G_ij^(n)
# using analytic formula
#-----------------------------
def g_integ(m, nuij, n):
    """

    .. math::

        \\int_0^\\infty dr\\, r^n e^{-nuij\\, r - m\\, r}
        
    Args:
        m: float, meson mass or cutoff momentum
        nuij: float, Gaussian range parameter
        n: int, power of r
    
    Returns:
        gijn1, gijn2, gijn3: float, radial integral
    """
    
    ## Normal summation
    gijn1 = 0.0; gijn2 = 0.0; gijn3 = 0.0
    if n > 0:       
        gamma = 0.5 * m / nuij
        xasy = 10.0 # Assumed for asymptotic expansion of erfc(x): exp(10**2) \sim 10^{43}
        gijn1 = 0.0
        for k in range(n + 1):
            gijn1 += math.comb(n, k) * (-gamma)**(n - k) * ei_integ(nuij, gamma, k, xasy)

        ## Kahan summation algorithm
        gijn2 = 0.0
        c = 0.0
        for k in range(n + 1):
            value_add = math.comb(n, k) * (-gamma)**(n - k) * ei_integ(nuij, gamma, k, xasy)
            gijn2, c = kahan_sum(value_add, gijn2, c)

        ## math.fsum
        value_list = np.array([
            math.comb(n, k) * (-gamma)**(n - k) * ei_integ(nuij, gamma, k, xasy)
            for k in range(n + 1)
        ])
        gijn3 = math.fsum(value_list)
        
        return gijn1, gijn2, gijn3

    
#-----------------------------
# Radial initegration G_ij^(n)
# using special functions
#-----------------------------
def g_integ_sp(m, nuij, n):
    """

    .. math::

        \\int_0^\\infty dr\\, r^n e^{-nuij\\, r - m\\, r}

    Args:
        m: float, meson mass or cutoff momentum
        nuij: float, Gaussian range parameter
        n: int, power of r
    """
    
    gijn = 0.0
    if n > 0:
        fac1 = np.sqrt(pi) / gamma(n / 2 + 1)
        fac2 = np.sqrt(2.0 * pi) * m / (np.sqrt(2.0 * nuij) * gamma((n + 1) / 2))
        chfs = fac1 * hyp1f1((n + 1) / 2, 0.5, 0.25 * m**2 / nuij) \
             - fac2 * hyp1f1(n / 2 + 1, 1.5, 0.25 * m**2 / nuij)
        gijn = 1.0 / np.sqrt((4.0 * nuij))**(n+1) * gamma(n + 1) * chfs

    return gijn