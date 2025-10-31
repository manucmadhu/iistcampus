import numpy as np
import matplotlib.pyplot as plt
from math import factorial
import math

# --- Gaussian Probability Density Function ---
def GPx(x, mu, sigma):
    return np.exp(-((x - mu)**2) / (2 * sigma**2)) / (np.sqrt(2 * np.pi) * sigma)

# --- Poisson Probability Mass Function ---
def PPx(x, m):
    if x < 0 or x > 170:
        return 0
    return (m**x) * np.exp(-m) / factorial(int(x))

# --- Function to plot comparisons ---
def plots(m1, m2, m3,m4):
    m_values = [m1, m2, m3,m4]
    labels = [r'$\mu=\sigma^2=0.5$', r'$\mu=\sigma^2=4.0$', r'$\mu=\sigma^2=32.0$', r'$\mu=\sigma^2=10.0$']

    plt.figure(figsize=(10, 6))

    for i, m in enumerate(m_values):
        mu = m
        sigma = np.sqrt(m)

        # --- Gaussian curve ---
        x_gauss = np.linspace(0, mu + 10, 500)
        y_gauss = GPx(x_gauss, mu, sigma)
        y_gauss /= np.max(y_gauss)  # normalize

        # --- Poisson values ---
        x_pois = np.arange(0, (math.ceil(mu/10)+1)*10)
        y_pois = np.array([PPx(x, mu) for x in x_pois])
        y_pois /= np.max(y_pois)  # normalize

        # --- Plot both ---
        plt.plot(x_gauss, y_gauss, label=f'Gaussian {labels[i]}', lw=2)
        plt.plot(x_pois, y_pois, 'o--', label=f'Poisson {labels[i]}', alpha=0.7)
        plt.xlabel(r'$x$', fontsize=12)
        plt.ylabel('Normalized Probability', fontsize=12)
        plt.title('Comparison of Gaussian and Poisson Distributions', fontsize=14)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

# --- Run the function ---
plots(0.5, 4.0, 32.0,10.0)
