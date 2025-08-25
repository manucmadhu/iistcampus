import math
import matplotlib.pyplot as plt
import numpy as np

# Constants
c = 3e8
h = 6.626e-34
Kb = 1.3e-23

# Frequency range
min_limit = 1e12
max_limit = 1e17
peak_Bv=[]
peak_freq=[]
def black(frequencies,T):
    Bv = (2*h*frequencies**3) / (c**2 * (np.exp((h*frequencies)/(Kb*T)) - 1))
    return Bv

def main():
    for split in [25,100]:   
        frequencies = np.linspace(min_limit, max_limit, split)
        
        # Different Temperatures
        for T in [1000, 3000, 10000, 50000, 100000]:
            Bv = black(frequencies, T) 
            plt.plot(frequencies, Bv, label=f"T={T}K")
            idx = np.argmax(Bv)
            plt.scatter(frequencies[idx], Bv[idx], marker="o")
            peak_Bv.append(Bv[idx])
            peak_freq.append(frequencies[idx])
        plt.plot(peak_freq,peak_Bv,label='Peak Connecting Line',color='brown')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Spectral Radiance per unit frequency Bv')
        plt.title("Blackbody Radiation Spectrum (Planck's Law)")
        plt.legend()
        plt.show()

if __name__ == "__main__":
    main()
