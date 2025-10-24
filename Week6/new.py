import numpy as np

# --- True Value for Comparison ---
TRUE_VALUE = (np.pi**4) / 15.0
print(f"True Value (π^4/15) for comparison: {TRUE_VALUE:.8f}\n")

# The constants h, K, T, c are NOT needed for the numerical calculation 
# since we evaluate the dimensionless integral which equals pi^4/15.
# They are only necessary to find the physical value of the original integral.

# ----------------------------------------------------
# Task 1: Rewrite Integral and Convert Limits [-1, 1]
# ----------------------------------------------------

def integrand_f_x(x):
    """The simplified function f(x) = x^3 / (e^x - 1)."""
    # The limit is 0 as x approaches 0, but this isn't strictly necessary 
    # for the substitution x=(1+u)/(1-u) since u=-1 gives x=0.
    if x == 0:
        return 0.0
    return (x**3) / (np.exp(x) - 1.0)

def blackbody_g_u(u):
    """
    The transformed integrand g(u) for Gauss Quadrature (Task 1).
    Substitution: x = (1+u)/(1-u) | dx = 2/(1-u)^2 du
    Integral: I = Integral_{-1}^{1} g(u) du
    """
    if u == 1.0:
        # u=1 corresponds to x=infinity. The function should approach 0.
        return 0.0
    
    x = (1.0 + u) / (1.0 - u)
    
    # Differential term dx/du
    dx_du = 2.0 / (1.0 - u)**2
        
    # The full transformed integrand g(u) = f(x) * dx/du
    g_u = integrand_f_x(x) * dx_du
    return g_u

# Set integration limits for all methods
MIN_LIMIT = -1.0
MAX_LIMIT = 1.0

# ----------------------------------------------------
# Task 2: 2-Point and 3-Point Gauss Quadrature
# ----------------------------------------------------

def twopoint_quadrature(func, a, b):
    """
    Performs 2-point Gauss Quadrature on interval [a, b].
    Roots (xi) for [-1, 1]: +/- 1/sqrt(3) (approx +/- 0.57735)
    Weights (wi) for [-1, 1]: 1.0
    """
    # Normalized roots for [-1, 1]
    u1, u2 = -1.0/np.sqrt(3.0), 1.0/np.sqrt(3.0) 
    w1, w2 = 1.0, 1.0 # Weights for [-1, 1]

    # Transform roots from [-1, 1] to [a, b]
    x1 = ((b - a) / 2.0) * u1 + ((b + a) / 2.0)
    x2 = ((b - a) / 2.0) * u2 + ((b + a) / 2.0)
    
    # Transformed weights for [a, b] (Scaling Factor)
    scaling_factor = (b - a) / 2.0
    
    return scaling_factor * (w1 * func(x1) + w2 * func(x2))

def threepoint_quadrature(func, a, b):
    """
    Performs 3-point Gauss Quadrature on interval [a, b].
    Roots (xi) for [-1, 1]: +/- sqrt(3/5) (approx +/- 0.774597), 0
    Weights (wi) for [-1, 1]: 5/9, 8/9, 5/9
    """
    # Normalized roots for [-1, 1]
    u1, u2, u3 = -np.sqrt(3.0/5.0), 0.0, np.sqrt(3.0/5.0) 
    w1, w2, w3 = 5.0/9.0, 8.0/9.0, 5.0/9.0 # Weights for [-1, 1]

    # Transform roots from [-1, 1] to [a, b]
    x1 = ((b - a) / 2.0) * u1 + ((b + a) / 2.0)
    x2 = ((b - a) / 2.0) * u2 + ((b + a) / 2.0)
    x3 = ((b - a) / 2.0) * u3 + ((b + a) / 2.0)
    
    # Transformed weights for [a, b] (Scaling Factor)
    scaling_factor = (b - a) / 2.0
    
    return scaling_factor * (w1 * func(x1) + w2 * func(x2) + w3 * func(x3))

# Calculate Gauss Quadrature Results
I_2_gauss = twopoint_quadrature(blackbody_g_u, MIN_LIMIT, MAX_LIMIT)
I_3_gauss = threepoint_quadrature(blackbody_g_u, MIN_LIMIT, MAX_LIMIT)

print("--- Task 2: Gauss Quadrature ---")
print(f"2-Point Quadrature Result: ",I_2_gauss)

print(f"3-Point Quadrature Result: ",I_3_gauss)

print("-" * 40)

# ----------------------------------------------------
# Task 3: Simpson's 1/3 Rule
# ----------------------------------------------------

def simpsons_1_3_rule(func, a, b, n):
    """
    Estimates the integral of func(x) from a to b using Simpson's 1/3 rule.
    n must be an even number.
    """
    if n % 2 != 0:
        print("Error: n must be an even number for Simpson's 1/3 rule.")
        return np.nan
        
    h = (b - a) / n
    s = func(a) + func(b) # f(x0) + f(xn)
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            s += 2 * func(x) # Even terms (except first/last)
        else:
            s += 4 * func(x) # Odd terms
            
    return s * h / 3.0

# Using a large even number of intervals for good accuracy
N_SIMPS = 1000 
I_simps = simpsons_1_3_rule(blackbody_g_u, MIN_LIMIT, MAX_LIMIT, N_SIMPS)

print("--- Task 3: Simpson's 1/3 Rule ---")

print(f"Simpson's 1/3 Rule Result: ",I_simps)

#four point quadrature
def fourquadrature(func):
    x1=-0.861136
    x2=-0.339981
    x3=0.339981
    x4=0.861136
    w1=0.347855
    w2=0.652145
    w3=0.652145
    w4=0.347855
    return w1*func(x1) + w2*func(x2) + w3*func(x3) + w4*func(x4)

print("The value of integration with 4 point quadrature:",fourquadrature(blackbody_g_u))

def fivequadrature(func):
    """
    Performs 5-point Gauss Quadrature over the standard interval [-1, 1].
    The roots and weights are standard values for N=5 Gauss-Legendre Quadrature.
    """
    # Roots (xi)
    x1 = -0.9061798459
    x2 = -0.5384693101
    x3 = 0.0
    x4 = 0.5384693101
    x5 = 0.9061798459
    
    # Weights (wi)
    w1 = 0.2369268851
    w2 = 0.4786286705
    w3 = 0.5688888889
    w4 = 0.4786286705
    w5 = 0.2369268851
    
    # Summation: I = sum(wi * f(xi))
    return w1 * func(x1) + w2 * func(x2) + w3 * func(x3) + w4 * func(x4) + w5 * func(x5)

print("The value of integration with 5 point quadrature:",fivequadrature(blackbody_g_u))