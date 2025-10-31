import numpy as np
import matplotlib.pyplot as plt

# ---------------- Constants ----------------
kB = 1.38e-16       # erg/K
me = 9.1e-28        # gm
mp = 1.6e-24        # gm
c = 3e10            # cm/s
pi = np.pi
M = 10              # Solar masses
rg = 3e5 * M        # Schwarzschild radius (cm)

# ---------------- Helper functions ----------------
def n(x, mdot):
    return mdot / (2 * pi * mp * (rg**2) * c * x**1.5)

def Gamma_ep(Te, Tp, x, mdot):
    Te = max(Te, 1e-8)
    return 3.2e-12 * (kB / mp) * n(x, mdot)**2 * (Tp - Te) * np.sqrt(me / (Te**3))

def Lambda_e(Te, x, mdot):
    Te = max(Te, 1e-8)
    return 1.4e-27 * n(x, mdot)**2 * np.sqrt(Te)

def dTp_dx(x, Tp, Te, mdot):
    """Derivative function for T_p (ODE 1)."""
    # ODE 1: dTp/dx = - Tp * B + A * Gamma_ep
    
    # Common Factor B = (3x - 4) / (3x(x-1))
    term_B = (3*x - 4) / (3*x*(x - 1))
    
    # A * Gamma_ep term
    common_coeff = (4 * pi * mp * rg**3) / (3 * kB * mdot)
    term_source = common_coeff * x**2 * Gamma_ep(Te, Tp, x, mdot)
    
    return -Tp * term_B + term_source

def dTe_dx(x, Tp, Te, mdot):
    """Derivative function for T_e (ODE 2)."""
    # ODE 2: dTe/dx = - Te * B - A * (Gamma_ep - Lambda_e)
    
    # Common Factor B = (3x - 4) / (3x(x-1))
    term_B = (3*x - 4) / (3*x*(x - 1))
    
    # A * (Gamma_ep - Lambda_e) term
    common_coeff = (4 * pi * mp * rg**3) / (3 * kB * mdot)
    term_source = common_coeff * x**2 * (Gamma_ep(Te, Tp, x, mdot) - Lambda_e(Te, x, mdot))
    
    return -Te * term_B - term_source

# ---------------- Euler integration ----------------
def euler_method(x0, xf, h, Tp0, Te0, mdot):
    n_steps = int(abs((xf - x0) / h)) + 1
    xs = np.linspace(x0, xf, n_steps)
    Tp = np.zeros_like(xs)
    Te = np.zeros_like(xs)
    Tp[0], Te[0] = Tp0, Te0
    
    for i in range(1, n_steps):
        x = xs[i-1]
        Tp[i] = Tp[i-1] + h * dTp_dx(x, Tp[i-1], Te[i-1], mdot)
        Te[i] = Te[i-1] + h * dTe_dx(x, Tp[i-1], Te[i-1], mdot)
        Tp[i] = max(Tp[i], 0)
        Te[i] = max(Te[i], 0)
    return xs, Tp, Te

x0=1e3
xi=1e3
xf=2.0
T_e=T_p=1e8
m_dot=1e17
h=-0.1
x, Tp, Te = euler_method(x0, xf, h, T_p, T_e, m_dot)
plt.loglog(x,Te,color='red',label='Electron Temperature Te')
plt.loglog(x,Tp,'--',color='blue',label='Proton Temperature Tp')
plt.xlabel("Radial distance in cm")
plt.title("Te=Tp=10^8 M_dot =10^17")
plt.ylabel("Distribution of Electron/Proton temperature in K")
plt.legend()
plt.show()

T_p=5*T_p

x, Tp, Te = euler_method(x0, xf, h, T_p, T_e, m_dot)
plt.loglog(x,Te,color='red',label='Electron Temperature Te')
plt.loglog(x,Tp,'--',color='blue',label='Proton Temperature Tp')
plt.xlabel("Radial distance in cm")
plt.title("Te=10^8 Tp=5x10^8 M_dot =10^17")
plt.ylabel("Distribution of Electron/Proton temperature in K")
plt.legend()
plt.show()

T_p=T_e
m_dot=1e19
x, Tp, Te = euler_method(x0, xf, h, T_p, T_e, m_dot)
plt.loglog(x,Te,color='red',label='Electron Temperature Te')
plt.loglog(x,Tp,'--',color='blue',label='Proton Temperature Tp')
plt.xlabel("Radial distance in cm")
plt.title("Te=Tp=10^8 M_dot =10^19")
plt.ylabel("Distribution of Electron/Proton temperature in K")
plt.legend()
plt.show()