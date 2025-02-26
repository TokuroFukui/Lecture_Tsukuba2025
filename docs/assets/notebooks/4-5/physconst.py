#--------
# Modules
#--------
import numpy as np


#-------------------
# Physical constants
#-------------------
pi = np.pi
hc = 197.3269601               # \hbar c (MeV fm)
m_p = 938.2720                 # Proton mass (MeV)
m_n = 939.5654                 # Neutron mass (MeV)
muac = m_p * m_n / (m_p + m_n) # Reduce mass (MeV)
m_av = 0.5 * (m_p + m_n)       # Average nucleon mass (MeV)
m_av /= hc                     # Average nucleon mass (fm^{-1})