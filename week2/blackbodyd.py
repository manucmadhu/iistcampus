import math
import matplotlib.pyplot as plt
import numpy as np
T=int(6000)
min_limit=int(10e13)
max_limit=int(10e14)
c=3e8
h=6.626e-34
Kb=1.3e-23
def black(frequencies):
    Bv = (2*h*frequencies**3) / (c**2 * (np.exp((h*frequencies)/(Kb*T)) - 1))
    return Bv
def blackwein(frequencies):
    f_list = [f for f in frequencies if (h*f) > Kb*T]
    B_list = [(2*h*f**3)/(c**2) * np.exp(-(h*f)/(Kb*T)) for f in f_list]
    return f_list, B_list

# Rayleigh–Jeans approximation (valid when hν << kT)
def blackray(frequencies):
    f_list = [f for f in frequencies if h*f < Kb*T]
    B_list = [(2*f**2*Kb*T)/(c**2) for f in f_list]
    return f_list, B_list
def main():
    frequencies = np.linspace(min_limit, max_limit, 1000)
    Bv=black(frequencies)
    plt.plot(frequencies,Bv)
    R_list,Br_list=blackray(frequencies)
    plt.plot(R_list,Br_list,"--",label="Rayleigh-Jeans")
    W_list,Bl_list=blackwein(frequencies)
    plt.plot(W_list,Bl_list,"--",label="Wein's Approximation'")
    plt.xlabel('Frequency v')    
    plt.ylabel('Spectral Radiance per unit frequency Bv')
    plt.legend()
    plt.show()
# Planck's Law (spectral radiance per unit frequency)

if __name__ == "__main__":
    main()