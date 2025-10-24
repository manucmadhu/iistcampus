import numpy as np
import matplotlib.pyplot as plt
h=6.626e-34
K=1.38e-23
T=5000 #K
c=3e8

#task 1 convert the function for the x=hv/KT 

#Revised blackbody function
def integrand_f_x(x):
    """The simplified function f(x) = x^3 / (e^x - 1)."""
    if x == 0:
        # Limit of x^3 / (e^x - 1) as x->0 is 0 (by L'Hopital's rule)
        return 0.0
    return (x**3) / (np.exp(x) - 1.0)

def blackbody(u):
    """
    The transformed integrand g(u) for Gauss Quadrature,
    where x = (1+u)/(1-u) and dx = 2/(1-u)^2 du.
    """
    x = (1.0 + u) / (1.0 - u)
    
    # Handle the singular point at u=1, corresponding to x=infinity.
    # The exponential term should dominate, making the integrand approach 0.
    if u == 1.0:
        return 0.0
        
    # The full integrand g(u) = f(x) * dx/du
    g_u = integrand_f_x(x) * (2.0 / (1.0 - u)**2)
    return g_u

#limit of integration
min_limit=-1
max_limit=1

#2-point gauss quadrature

def twopoint(func,a,b):
    x1=((b-a)*(-1/np.sqrt(3))/2)+((b+a)/2)
    x2= ((b-a)*np.sqrt(1/3)/2)+((b+a)/2)
    c1=c2=(b-a)/2
    return (c1*func(x1))+(c2*func(x2))


# #to test the two point quadrature
# def square(x):
#     return x**2

# print(twopoint(square,-1,1))
# print(twopoint(square,0,1))

#tested and working fine

def threepoint(func,a,b):
    x1=((b-a)*(-1*np.sqrt(3/5))/2)+((b+a)/2)
    x2= (b+a)/2
    x3= ((b-a)*np.sqrt(3/5)/2)+((b+a)/2)
    c1=((b-a)/2)*5/9
    c2=((b-a)/2)*8/9
    c3=((b-a)/2)*5/9
    return (c1*func(x1))+(c2*func(x2))+(c3*func(x3))

# #to test the three point quadrature
# def square(x):
#     return x**2

# print(threepoint(square,-1,1))
# print(threepoint(square,0,1))
# #tested and working fine

#to calculate the value of balckbody between[-1,1]
print("The value of the Integration in interval[-1,1] by two-point quadrature is:",twopoint(blackbody,-1,1))
print("The value of the Integration in interval[-1,1] by three-point quadrature is:",threepoint(blackbody,-1,1))

# #fincding the weight values in table
# print("____________________________________________________________________________________")
# print("|    n            |xi                                      |wi           ")
# print("|____________________________________________________________________________________|")
# a=-1
# b=1
# n=2
# x1=((b-a)*(-1/np.sqrt(3))/2)+((b+a)/2)
# x2= ((b-a)*np.sqrt(1/3)/2)+((b+a)/2)
# c1=c2=(b-a)/2
# print("|    %s            |%s                    |%s           "%(n,x1,c1))
# print("|____________________________________________________________________________________|")
# print("|    %s            |%s                    |%s           "%(n,x2,c2))
# print("|____________________________________________________________________________________|")

# n=3
# x1=((b-a)*(-1*np.sqrt(3/5))/2)+((b+a)/2)
# x2= (b+a)/2
# x3= ((b-a)*np.sqrt(3/5)/2)+((b+a)/2)
# c1=((b-a)/2)*5/9
# c2=((b-a)/2)*8/9
# c3=((b-a)/2)*5/9

# print("|    %s            |%s                    |%s           "%(n,x1,c1))
# print("|____________________________________________________________________________________|")
# print("|    %s            |%s                    |%s           "%(n,x2,c2))
# print("|____________________________________________________________________________________|")
# print("|    %s            |%s                    |%s           "%(n,x3,c3))
# print("|____________________________________________________________________________________|")




#task 3
# import scipy.integrate as integr
# x_values=np.linspace(-1,1,100)
# y_values=[]
# for x in x_values:
#     y_values.append(blackbody(x))
# value=integr.simpson(x=x_values,y=y_values)
# print("The value from the integration using inbuilt simpsons rule routine is :" ,value)
def simps(func, a, b, n):
    if n % 2 != 0:
        return np.nan
    h = (b - a) / n
    s = func(a) + func(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            s += 2 * func(x)
        else:
            s += 4 * func(x)
    return s * h / 3
print("The value from the integration using coded simpsons rule  is :" ,simps(blackbody,-1,1,1000))