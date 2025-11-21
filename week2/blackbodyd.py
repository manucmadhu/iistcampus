import math
import matplotlib.pyplot as plt
import numpy as np

T = int(6000)
min_limit = int(10e13)
max_limit = int(10e14)
c = 3e8
h = 6.626e-34
Kb = 1.3e-23

def black(frequencies):
    Bv = (2*h*frequencies**3) / (c**2 * (np.exp((h*frequencies)/(Kb*T)) - 1))
    return Bv  # <-- return only Bv (not tuple)

def main():
    frequencies = np.linspace(min_limit, max_limit, 1000)

    # Full Planck curve
    Bv = black(frequencies)
    plt.title("Blackbody Curve")
    plt.plot(frequencies, Bv, label="")
    plt.legend()
    plt.show()

    # Find split index
    index = 0
    for i in range(len(frequencies)):
        if h*frequencies[i] > Kb*T:
            index = i
            break

    # Rayleigh-Jeans region
    freq_R = frequencies[:index-1]
    Br_list = black(freq_R)
    plt.plot(freq_R, Br_list, "--", label="Rayleigh-Jeans")

    # Wien region
    freq_W = frequencies[index:]
    Bl_list = black(freq_W)
    plt.plot(freq_W, Bl_list, "--", label="Wien Approximation")

    plt.xlabel('Frequency v')    
    plt.ylabel('Spectral Radiance Bv')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
