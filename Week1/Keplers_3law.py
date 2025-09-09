#write a python program to verify kleplers third law
import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.674e-11  # m^3/kg/s^2
M_sun = 1.989e30  # kg
a_earth = 1.496e11  # m, defines 1 AU
seconds_per_year = 3.154e7  # seconds in a year

# Planetary data for Venus, Earth, and Jupiter
planets_data = {
    'Venus': 1.082e11,
    'Earth': 1.496e11,
    'Jupiter': 7.785e11
}

# --- Calculation ---
# Dictionaries to store results
orbital_radii_au = {}
orbital_periods_years = {}

for name, a_meters in planets_data.items():
    # Normalize orbital radius to AU
    a_au = a_meters / a_earth
    orbital_radii_au[name] = a_au
    
    # Calculate period using Kepler's 3rd Law
    T_seconds = np.sqrt((4 * np.pi**2 * a_meters**3) / (G * M_sun))
    
    # Convert period to years
    T_years = T_seconds / seconds_per_year
    orbital_periods_years[name] = T_years

# --- Plotting ---
plt.figure(figsize=(8, 6))

# Get the lists of radii and periods
a_values = list(orbital_radii_au.values())
T_values = list(orbital_periods_years.values())
planet_names = list(orbital_radii_au.keys())

# Plot the points for each planet on a log-log scale
plt.loglog(a_values, T_values, 'o', markersize=8)

# Add labels for each point
for i, txt in enumerate(planet_names):
    plt.annotate(txt, (a_values[i], T_values[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Add a reference line showing the T^2 vs a^3 relationship
# This line will have a slope of 1.5 on a log-log plot
a_ref = np.array([min(a_values) / 2, max(a_values) * 2])
T_ref = a_ref**(1.5)
plt.loglog(a_ref, T_ref, 'k--', alpha=0.5)

plt.title("Kepler's Third Law Verification")
plt.xlabel("Orbital Radius ($a$) in AU")
plt.ylabel("Orbital Period ($T$) in years")
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
