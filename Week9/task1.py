import numpy as np
import matplotlib.pyplot as plt

x_values,y_values,y_err=np.loadtxt('Week9\data1.unknown',usecols=(0,1,2),unpack=True)
#data initialized to three arrys and checked where stored correctly
# print(x_values)
# print(y_values)
# print(y_err)

# Task 1 to plot the data with uncertainites 
plt.plot(x_values,y_values,label='Original Given Data')
plt.errorbar(x_values,y_values,yerr=y_err,fmt ='o',label="Error")

# plt.show()

# Task 2 Linear Regression

# f(x) = a0 + a1 x

'''
sigma = y_error
a1 = ( S Sxy -SxSy ) /( SS(x^2)-(Sx)^2 )

a0 = ( S(x^2) Sy - Sx Sxy ) / ( SS(x^2) - S(x^2))

S = sum of (1/sigma(i)^2)
Sx = sum of (xi/sigma(i)^2)
Sy = sum of (yi/sigma(i)^2)
Sxy = sum of (xiyi/sigma(i)^2)

chi^2 = sum (f(x,a0,a1)-yi)/sigma(i)^2
'''
S=0
Sx=0
Sy=0
Sxy=0
Sx2=0
for x,y,sigma in zip(x_values,y_values,y_err):
    k = 1/(sigma**2)
    # print(k) # To Check if the 
    S += k
    Sx += x*k
    Sy += y*k
    Sxy += x*y*k
    Sx2 += x*x*k

a1 = ( S*Sxy - Sx*Sy ) /( S*Sx2 - Sx**2 )
a0 = ( Sx2*Sy - Sx*Sxy ) / ( S*Sx2 - Sx**2)
# print(a0,a1)
new_y=[]

for x in x_values:
    new_y.append(a0 + a1*x)
    
plt.plot(x_values,new_y,label='Linear Regression ')
plt.legend()
plt.show()

# To Calculate Chi Square

chi_square = 0.0

for yold,ynew,err in zip(y_values,new_y,y_err):
    chi_square += ((yold-ynew)**2) / err**2
  
print("Chi_Square = ",chi_square)
print("Chi-Square per degrees of freedom = ",chi_square/(len(y_values)-2))

y_diff = y_values-new_y
# print(y_diff)
plt.title("Difference between Y value and Model")
plt.axhline(y=0,color='blue')
plt.bar(x_values,y_diff,color='orange')
plt.show()