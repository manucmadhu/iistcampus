#Vmax vs T for the plancks law
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
        frequencies = np.linspace(min_limit, max_limit, 1000)
        Tees=[1000, 3000, 10000, 50000, 100000]
        # Different Temperatures
        for T in Tees :
            Bv = black(frequencies, T) 
            idx = np.argmax(Bv)
            peak_freq.append(frequencies[idx])
            #plt.plot(frequencies[idx],T,marker='o',label=f'T={T}')
            plt.plot(frequencies[idx], T, 'ro')
        plt.plot(peak_freq,Tees,label='Vmax vs T')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    main()
