import matplotlib.pyplot as plt
import numpy as np

# Constants
T = 6000
c = 3e8
h = 6.626e-34
Kb = 1.38e-23  # corrected constant

# Frequency range (better: wider than your original)
min_limit = 1e14
max_limit = 1e15
frequencies = np.linspace(min_limit, max_limit, 1000)

# Planck's Law
def black(frequencies):
    return (2*h*frequencies**3) / (c**2 * (np.exp((h*frequencies)/(Kb*T)) - 1))

# Wien approximation (valid when hν >> kT)
def blackwein(frequencies):
    f_list = [f for f in frequencies if h*f > Kb*T]
    B_list = [(2*h*f**3)/(c**2) * np.exp(-(h*f)/(Kb*T)) for f in f_list]
    return f_list, B_list

# Rayleigh–Jeans approximation (valid when hν << kT)
def blackray(frequencies):
    f_list = [f for f in frequencies if h*f < Kb*T]
    B_list = [(2*f**2*Kb*T)/(c**2) for f in f_list]
    return f_list, B_list

def main():
    # Full Planck
    Bv = black(frequencies)
    plt.plot(frequencies, Bv, label="Planck's Law", color="black")

    # Rayleigh–Jeans
    R_list, Br_list = blackray(frequencies)
    plt.plot(R_list, Br_list, "--", label="Rayleigh-Jeans", color="blue")

    # Wien
    W_list, Bw_list = blackwein(frequencies)
    plt.plot(W_list, Bw_list, "--", label="Wien", color="red")

    plt.xlabel("Frequency v (Hz)")
    plt.ylabel("Spectral Radiance per unit frequency Bv")
    plt.title(f"Blackbody Spectrum at T={T}K")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
