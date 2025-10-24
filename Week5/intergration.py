import numpy as np
import matplotlib.pyplot as plt

# Define constants
c=3e10 #cm/s
H0=67.2 #Km/s/Mpc
Omega_m=0.2726
Omega_a=0.7274

#task One
# define c/H0 in Gpc 
#one Gpc = 1e3 Mpc
c_H0=c/(H0*1e5) #1e5 multiplied to covert the value of H0 to cm/s/Mpc
c_H0=c_H0/1e3 # The value in Mpc converted to Gpc
print("The Value of c/H0",c_H0,"Gpc")

#Task 2 Impelemeted function to calculate the value D(z) at any point
def D(x):
    temp=np.sqrt(  Omega_m*(1+x)**3 + Omega_a)
    return c_H0 * 1/temp

#Task 3

#Implementing trapeziodal rule
def trapeziodal(func,a,b,n):
   h=(b-a)/n
   integral=(func(a)+func(b))/2.0
   for i in range(1,n):
       integral +=func(a+ i*h)
   integral*=h 
   return integral

#check working of the trapeziodal
# def square(x):
#     return x**2
# print(trapeziodal(square,0,3,100))

print("_______________________________________________________")
print("Trapezioidal Rule using 100 intervals")
D_1=trapeziodal(D,0,1,100)
D_2=trapeziodal(D,0,15,100)
print("The value of integral D(z) from 0 to 1 trapeziodal rule is :",D_1)
print("The value of integral D(z) from 0 to 15 trapeziodal rule is :",D_2)

# simpsons 1/3 rule

def simpsons(func, a, b, n):
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


# # check working of the simpsons
# def square(x):
#     return x**2
# print(simpsons(square,0,3,100))


print("_______________________________________________________")
print("Simpsons 1/3rd  Rule using 100 Intervals")
D_1=simpsons(D,0,1,100)
D_2=simpsons(D,0,15,100)
print("The value of integral D(z) from 0 to 1 Simpsons rule is :",D_1,"Gpc")
print("The value of integral D(z) from 0 to 15 Simpsons rule is :",D_2,"Gpc")

# Task 4 to find the number of ideal intervals
n=np.arange(10,10000,10)
index=0
tol=1e-7
print("_________________________________________________")
#for trapeziodal z ->[0,1]
for i in range(len(n)-1):
    D_1=trapeziodal(D,0,1,n[i])
    D_2=trapeziodal(D,0,1,n[i+1])
    if abs(D_1-D_2) < tol:
        # print(f"D(z=1) = {D_1:.6f}")
        # print(f"D(z=1) = {D_2:.6f}")
        index=n[i]
        break
print("_____Trapeziodal z->[0,1]_____")
print("The ideal number of bins = ",index)
print("The ideal bin size = ",1/index)
print(" ")
# print(trapeziodal(D,0,1,n[i]))
# print(trapeziodal(D,0,1,n[i+1]))
index=0
for i in range(len(n)-1):
    D_1=trapeziodal(D,0,15,n[i])
    D_2=trapeziodal(D,0,15,n[i+1])
    if abs(D_1-D_2) < tol:
        # print(f"D(z=1) = {D_1:.6f}")
        # print(f"D(z=1) = {D_2:.6f}")
        index=n[i]
        break
print("_____Trapeziodal z->[0,15]_____")
print("The ideal number of bins = ",index)
if index >0:
    print("The ideal bin size = ",15/index)



index=0
#for simpsons z ->[0,1]
for i in range(len(n)-1):
    D_1=simpsons(D,0,1,n[i])
    D_2=simpsons(D,0,1,n[i+1])
    if abs(D_1-D_2) < tol:
        # print(f"D(z=1) = {D_1:.6f}")
        # print(f"D(z=1) = {D_2:.6f}")
        index=n[i]
        break
print("_____Simpsons z->[0,1]_____")
print("The ideal number of bins = ",index)
print("The ideal bin size = ",1/index)
print(" ")
# print(trapeziodal(D,0,1,n[i]))
# print(trapeziodal(D,0,1,n[i+1]))
index=0

for i in range(len(n)-1):
    D_1=simpsons(D,0,15,n[i])
    D_2=simpsons(D,0,15,n[i+1])
    if abs(D_1-D_2) < tol:
        # print(f"D(z=1) = {D_1:.6f}")
        # print(f"D(z=1) = {D_2:.6f}")
        index=n[i]
        break
print("_____Simpsons z->[0,15]_____")
print("The ideal number of bins = ",index)
print("The ideal bin size = ",15/index)

#the ideal bin size is 140 for integrating from 0 to 15 thus ideal bin  size is 15/140

#task 5

D_z=[]
z_values=np.arange(0,16,1)
# print(z_values)
for z in z_values:
    D_z.append(simpsons(D,0,z,index))
    
plt.scatter(z_values,D_z,color='red',label='Using Simpsons')
plt.xlabel("Z values ")
plt.ylabel("Red-Shift Distance")


D_trap=[]
D_simp=[]
import scipy.integrate as integr
D_trapezoid_scipy = []
D_simpson_scipy = []

# Calculate the integral D_C(z) = integral from 0 to z of D(x) dx
for z in z_values:
    if z == 0:
        integral_trap = 0
        integral_simp = 0
    else:
        # Create a dense set of points for integration
        x_points = np.linspace(0, z, 140)
        y_points = D(x_points)
        
        # Calculate integral using scipy.integrate.trapezoid
        integral_trap = integr.trapezoid(y=y_points, x=x_points)
        
        # Calculate integral using scipy.integrate.simpson
        integral_simp = integr.simpson(y=y_points,x= x_points)

    D_trapezoid_scipy.append(integral_trap)
    D_simpson_scipy.append(integral_simp)
plt.plot(z_values, D_trapezoid_scipy, marker='o', linestyle='-', 
         label='scipy.integrate.trapezoid', alpha=0.7)
plt.plot(z_values, D_simpson_scipy, marker='x', linestyle='--', 
         label='scipy.integrate.simpson', alpha=0.7)
plt.legend()
plt.show()