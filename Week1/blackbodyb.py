#question to write the code to plot the blackbody fucntion over the range 1e14 to 1e17
import math
import matplotlib.pyplot as plt
import numpy as np
T=int(6000)
min_limit=int(1e14)
max_limit=int(1e17)
c=3e8
h=6.626e-34
Kb=1.3e-23
frequencies = np.linspace(min_limit, max_limit, 1000) # will generate the list of fequencies
# frequencies =np.logspace(13,14,500)
# Planck's Law (spectral radiance per unit frequency)
Bv = (2*h*frequencies**3) / (c**2 * (np.exp((h*frequencies)/(Kb*T)) - 1))
plt.loglog(frequencies,Bv)
plt.xlabel('Frequency v')    
plt.ylabel('Spectral Radiance per unit frequency Bv')
plt.show()