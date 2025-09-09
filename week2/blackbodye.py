
# continuation of blackbody with semilog plot on x axis
import matplotlib.pyplot as plt
import numpy as np
T=int(6000)
min_limit=1e12
max_limit=1e17
c=3e8
h=6.626e-34
Kb=1.3e-23
def black(frequencies):
    Bv = (2*h*frequencies**3) / (c**2 * (np.exp((h*frequencies)/(Kb*T)) - 1))
    return Bv
    
    
    
def main():
    frequencies = np.linspace(min_limit, max_limit, 1000)
    Bv=black(frequencies)
    #plt.plot(frequencies,Bv)
    #plt.xlabel('Frequency v')  
    plt.semilogx(frequencies,Bv)
    plt.xlabel('log Frequency v')    
    plt.ylabel('Spectral Radiance per unit frequency Bv')
    plt.show()
# Planck's Law (spectral radiance per unit frequency)

if __name__ == "__main__":
    main()