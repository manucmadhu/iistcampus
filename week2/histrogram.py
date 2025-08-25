import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(150, 181, 999)  # random ints 150–180
plt.hist(data, bins=range(150, 185, 5), edgecolor="black")
plt.xlabel("Value bins")
plt.ylabel("Count")
plt.title("Histogram of Random Values")
plt.show()
