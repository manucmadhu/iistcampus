import numpy as np
import matplotlib.pyplot as plt
import math

y=np.random.uniform(low=0.0,high=1.0,size=1000)
plt.hist(y,bins=50,edgecolor='black',color='grey')
plt.xlabel('y')
plt.ylabel('frequency')
plt.show()

x_values=-np.log(y)

bin_width = 0.3
bins = np.arange(0, max(x_values) + bin_width, bin_width)
hist, bin_edges = np.histogram(x_values, bins=bins, density=False)
hist_norm = hist / (1e3 * bin_width)

# Step 4: Plot normalized histogram
plt.bar(bin_edges[:-1], hist_norm, width=bin_width,
        color='lightgrey', edgecolor='black', )

# Step 5: Overlay theoretical e^{-x}
x_ar = np.linspace(0, max(x_values), 1000)
plt.plot(x_ar, np.exp(-x_ar), color='r', linewidth=2, label=r'Theoretical $e^{-x}$')
plt.xlabel('X')
plt.ylabel('Normalized Frequency of X values')
plt.legend()
plt.show()