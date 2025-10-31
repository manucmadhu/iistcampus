import numpy as np
import matplotlib.pyplot as plt

# Gaussian PDF
def gaussian(x, mu, sigma):
    return np.exp(-((x - mu)**2) / (2 * sigma**2)) / (np.sqrt(2 * np.pi) * sigma)

# Main loop
mean_array = []
variance_array = []

for N in [5, 10, 100]:
    M = 10**4
    mean_arr = []

    # --- Generate M sample means ---
    for _ in range(M):
        y = np.random.uniform(0.0, 1.0, N)
        x = -np.log(y)
        mean_arr.append(np.mean(x))

    # --- Compute actual mean & variance ---
    m = np.mean(mean_arr)
    var = np.var(mean_arr)
    mean_array.append(m)
    variance_array.append(var)

    # --- Plot histogram ---
    plt.figure(figsize=(8, 5))
    counts, bins, _ = plt.hist(mean_arr, bins=50, density=True, edgecolor='black', color='lightgray', alpha=0.7)

    # --- Generate Gaussian curve using same m and var ---
    x_vals = np.linspace(min(mean_arr), max(mean_arr), 500)
    y_gauss = gaussian(x_vals, m, np.sqrt(var))
    plt.plot(x_vals, y_gauss, 'r-', lw=2, label=f'Gaussian Fit\nμ={m:.3f}, σ²={var:.3f}')

    plt.title(f'N = {N}, M = 1e4')
    plt.xlabel('Sample Mean (X̄)')
    plt.ylabel('Normalized Frequency')
    plt.legend()
    plt.grid(alpha=0.4)
    plt.show()

print('Mean values for N = [5, 10, 100]:', mean_array)
print('Variance values for N = [5, 10, 100]:', variance_array)

# Explanation:
"""
As N increases:
- The mean stabilizes around 1 (expected value of exponential distribution).
- The variance decreases (distribution becomes narrower).
- The histogram approaches a Gaussian shape.
This demonstrates the Central Limit Theorem.
"""
