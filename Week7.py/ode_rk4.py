import numpy as np
import matplotlib.pyplot as plt

# ---------------- Constants ----------------
kB = 1.38e-16       # Boltzmann constant (erg/K)
me = 9.1e-28        # mass of electron (gm)
mp = 1.6e-24        # mass of proton (gm)
c = 3e10            # speed of light (cm/s)
pi = np.pi
M = 10              # Mass in Solar masses (M/M_sun)
rg = 3e5 * M        # Schwarzschild radius (cm) (r_g = 3e5 * M/M_sun)

# ---------------- Helper functions (Coupled ODE structure) ----------------

def n(x, mdot):
    """Calculates number density n(x)."""
    # n(x) = m_dot / (2 * pi * m_p * r_g^2 * c * x^(3/2))
    return mdot / (2 * pi * mp * (rg**2) * c * x**1.5)

def Gamma_ep(Te, Tp, x, mdot):
    """Calculates Coulomb coupling Gamma_ep."""
    Te = max(Te, 1e-8) # Safety check
    # Gamma_ep = 3.2e-12 * (kB / mp) * n^2 * (Tp - Te) * sqrt(m_e / Te^3)
    return 3.2e-12 * (kB / mp) * n(x, mdot)**2 * (Tp - Te) * np.sqrt(me / (Te**3))

def Lambda_e(Te, x, mdot):
    """Calculates Bremsstrahlung cooling Lambda_e."""
    Te = max(Te, 1e-8) # Safety check
    # Lambda_e = 1.4e-27 * n^2 * sqrt(Te)
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

# ---------------- RK4 Integration Method ----------------
def rk4_method(x0, xf, h, Tp0, Te0, mdot):
    """
    Solves the coupled ODEs using the Runge-Kutta 4th-order method.
    h is negative for inward integration (x0 > xf).
    """
    # Number of steps
    n_steps = int(abs((xf - x0) / h))
    
    # Arrays for storing results
    xs = np.zeros(n_steps + 1)
    Tp = np.zeros(n_steps + 1)
    Te = np.zeros(n_steps + 1)
    
    # Initial conditions
    xs[0] = x0
    Tp[0], Te[0] = Tp0, Te0
    
    for i in range(n_steps):
        x = xs[i]
        Tp_i = Tp[i]
        Te_i = Te[i]
        
        # --- RK4 Steps for Tp ---
        k1_p = dTp_dx(x, Tp_i, Te_i, mdot)
        k1_e = dTe_dx(x, Tp_i, Te_i, mdot)
        
        k2_p = dTp_dx(x + h/2, Tp_i + h*k1_p/2, Te_i + h*k1_e/2, mdot)
        k2_e = dTe_dx(x + h/2, Tp_i + h*k1_p/2, Te_i + h*k1_e/2, mdot)
        
        k3_p = dTp_dx(x + h/2, Tp_i + h*k2_p/2, Te_i + h*k2_e/2, mdot)
        k3_e = dTe_dx(x + h/2, Tp_i + h*k2_p/2, Te_i + h*k2_e/2, mdot)

        k4_p = dTp_dx(x + h, Tp_i + h*k3_p, Te_i + h*k3_e, mdot)
        k4_e = dTe_dx(x + h, Tp_i + h*k3_p, Te_i + h*k3_e, mdot)
        
        # --- Update Tp and Te ---
        Tp[i+1] = Tp_i + (h/6) * (k1_p + 2*k2_p + 2*k3_p + k4_p)
        Te[i+1] = Te_i + (h/6) * (k1_e + 2*k2_e + 2*k3_e + k4_e)
        xs[i+1] = x + h
        
        # Safety: Ensure temperatures are non-negative
        Tp[i+1] = max(Tp[i+1], 1e-8)
        Te[i+1] = max(Te[i+1], 1e-8)
        
    return xs, Tp, Te

# ---------------- Main Execution and Plotting Loop ----------------

# Common parameters
x0 = 1e3
xf = 2.0
# Use a negative step size for inward integration
h = -0.01 

# --- Case (a) & (b): Te(xo)=Tp(xo)=10^8 K, m_dot=10^17 gm/cc ---
T_e_a = 1e8
T_p_a = 1e8
m_dot_a = 1e17
x_a, Tp_a, Te_a = rk4_method(x0, xf, h, T_p_a, T_e_a, m_dot_a)

plt.figure(figsize=(8, 6))
plt.loglog(x_a, Te_a, color='red', label='Electron Temperature $T_e$')
plt.loglog(x_a, Tp_a, '--', color='blue', label='Proton Temperature $T_p$')
plt.xlabel("Radial Distance $x = r/r_g$ (log scale)")
plt.title(f"Case (a)/(b): $T_e=T_p={T_e_a:.0e}$ K, $\dot{{m}}={m_dot_a:.0e}$ gm/cc")
plt.ylabel("Temperature (K) (log scale)")
plt.legend()
plt.show()


# --- Case (c): T_e(xo)=10^8 K, T_p(xo)=5x10^8 K, m_dot=10^17 gm/cc ---
T_e_c = 1e8
T_p_c = 5 * 1e8
m_dot_c = 1e17
x_c, Tp_c, Te_c = rk4_method(x0, xf, h, T_p_c, T_e_c, m_dot_c)

plt.figure(figsize=(8, 6))
plt.loglog(x_c, Te_c, color='red', label='Electron Temperature $T_e$')
plt.loglog(x_c, Tp_c, '--', color='blue', label='Proton Temperature $T_p$')
plt.xlabel("Radial Distance $x = r/r_g$ (log scale)")
plt.title(f"Case (c): $T_e={T_e_c:.0e}$ K, $T_p={T_p_c:.0e}$ K, $\dot{{m}}={m_dot_c:.0e}$ gm/cc")
plt.ylabel("Temperature (K) (log scale)")
plt.legend()

plt.show()

# --- Case (d): T_e(xo)=Tp(xo)=10^8 K, m_dot=10^19 gm/cc ---
T_e_d = 1e8
T_p_d = 1e8
m_dot_d = 1e19
x_d, Tp_d, Te_d = rk4_method(x0, xf, h, T_p_d, T_e_d, m_dot_d)

plt.figure(figsize=(8, 6))
plt.loglog(x_d, Te_d, color='red', label='Electron Temperature $T_e$')
plt.loglog(x_d, Tp_d, '--', color='blue', label='Proton Temperature $T_p$')
plt.xlabel("Radial Distance $x = r/r_g$ (log scale)")
plt.title(f"Case (d): $T_e=T_p={T_e_d:.0e}$ K, $\dot{{m}}={m_dot_d:.0e}$ gm/cc")
plt.ylabel("Temperature (K) (log scale)")
plt.legend()

plt.show()