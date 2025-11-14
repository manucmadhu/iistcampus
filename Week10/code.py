import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('Week10/data-stellar.txt', skiprows=1) # Read the data a a single array
data = data.reshape(-1, 3) # Done as data is given as a single line instead of multiple rows

#Now split data to multiple lists
time = data[:, 0]
mag  = data[:, 1]
mag_err = data[:, 2]

# print(time)
# print(mag)
# print(mag_err)
# #Tested if the readed columns are fine

#Task 1 to plot the data with the error-bars
plt.plot(time,mag,color="blue")
plt.xlabel("Time(in days)")
plt.ylabel("Magnitude")
plt.errorbar(time,mag,yerr=mag_err,fmt ='',capsize=3,ecolor='lightblue',label="Error",color='orange')
plt.legend()
plt.title("Data")
plt.show()

# Task 2 Guess a polynomial which may potentially fit the data. Construct the necessary matrixes to calculate the polynomial coefficients and its uncertainties. You can use built-in Python routine for matrix multiplication and inverse calculations.
'''
The general polynomial y=a1 + a2 x + a3 x^2 can be used as there is a cureve in the plotted graph
Which can be modelled by the Quadratic polynomial'''

#defining B matrix
b=mag/mag_err

# print(b)
# # Tested the array b

#defining A matrix
A=[]
a=[]

for xi,sigma in zip(time,mag_err):
    a=[]
    for k in range(3):
        a.append((xi**k)/sigma)
    A.append(a)
        
# print(A)
# # Tested matrix A

'''
a = [A^T A]^-1  [A^T b]'''

#defining A Transpose
A_T = []
rows = len(A)
cols = len(A[0])

for j in range(cols):        # column index
    newrow = []
    for i in range(rows):    # row index
        newrow.append(A[i][j])
    A_T.append(newrow)

# #Tested the array transpose is working
# print(A_T)
np_A=np.array(A)
np_A_t=np.array(A_T)
np_b=np.array(b)

alpha=np.dot(np_A_t,np_A)
epsilon=np.linalg.inv(alpha)
beta=np.dot(np_A_t,np_b)


a=np.dot(epsilon,beta)
# # Checked values of a
# print(a)

calculated_y=[]
for i in time:
    calculated_y.append(a[0] + a[1]*i + a[2]*(i**2))
plt.plot(time,calculated_y,label=" Quadratic - Fitted Values")
plt.plot(time,mag,color="blue")
plt.xlabel("Time(in days)")
plt.ylabel("Magnitude")
plt.errorbar(time,mag,yerr=mag_err,fmt ='',capsize=3,ecolor='lightblue',label="Error",color='orange')
plt.legend()
plt.title("Data + Quadratic Fitting")
plt.show()

# Task 3:To calculate Chi^2
chi_square=0
for cal_y,y,chi in zip(calculated_y,mag,mag_err):
    chi_square += ((cal_y-y)**2)/(chi**2)

print("Chi Square is for qudratic is : ",chi_square)
print("Reduced Chi Square is : ",chi_square/(len(time)-3))

# Task 4 : Increase and decrease the order of polynomial by one and repeat Task2 and Task3

# For linear Fitting
A=[]
a=[]
b=mag/mag_err
for xi,sigma in zip(time,mag_err):
    a=[]
    for k in range(2):
        a.append((xi**k)/sigma)
    A.append(a)
        
# print(A)
# # Tested matrix A

'''
a = [A^T A]^-1  [A^T b]'''

#defining A Transpose
A_T = []
rows = len(A)
cols = len(A[0])

for j in range(cols):        # column index
    newrow = []
    for i in range(rows):    # row index
        newrow.append(A[i][j])
    A_T.append(newrow)

# #Tested the array transpose is working
# print(A_T)
np_A=np.array(A)
np_A_t=np.array(A_T)
np_b=np.array(b)

alpha=np.dot(np_A_t,np_A)
epsilon=np.linalg.inv(alpha)
beta=np.dot(np_A_t,np_b)

a=np.dot(epsilon,beta)
# # Checked values of a
# print(a)

calculated_y=[]
for i in time:
    calculated_y.append(a[0] + a[1]*i )
plt.plot(time,calculated_y,label=" Linear - Fitted Values")
plt.plot(time,mag,color="blue")
plt.xlabel("Time(in days)")
plt.ylabel("Magnitude")
plt.errorbar(time,mag,yerr=mag_err,fmt ='',capsize=3,ecolor='lightblue',label="Error",color='orange')
plt.legend()
plt.title("Data + Linear Fitting")
plt.show()
chi_square=0
for cal_y,y,chi in zip(calculated_y,mag,mag_err):
    chi_square += ((cal_y-y)**2)/(chi**2)

print("Chi Square is for Linear is : ",chi_square)
print("Reduced Chi Square is : ",chi_square/(len(time)-2))

# For Cubic Fitting
A=[]
a=[]
b=mag/mag_err
for xi,sigma in zip(time,mag_err):
    a=[]
    for k in range(4):
        a.append((xi**k)/sigma)
    A.append(a)
        
# print(A)
# # Tested matrix A

'''
a = [A^T A]^-1  [A^T b]'''

#defining A Transpose
A_T = []
rows = len(A)
cols = len(A[0])

for j in range(cols):        # column index
    newrow = []
    for i in range(rows):    # row index
        newrow.append(A[i][j])
    A_T.append(newrow)

# #Tested the array transpose is working
# print(A_T)
np_A=np.array(A)
np_A_t=np.array(A_T)
np_b=np.array(b)

alpha=np.dot(np_A_t,np_A)
epsilon=np.linalg.inv(alpha)
beta=np.dot(np_A_t,np_b)

a=np.dot(epsilon,beta)
# # Checked values of a
# print(a)

calculated_y=[]
for i in time:
    calculated_y.append(a[0] + a[1]*i + a[2]*(i**2) + a[3]*(i**3)  )
plt.plot(time,calculated_y,label=" Cubic - Fitted Values")
plt.plot(time,mag,color="blue")
plt.xlabel("Time(in days)")
plt.ylabel("Magnitude")
plt.errorbar(time,mag,yerr=mag_err,fmt ='',capsize=3,ecolor='lightblue',label="Error",color='orange')
plt.legend()
plt.title("Data + Cubic Fitting")
plt.show()
chi_square=0
for cal_y,y,chi in zip(calculated_y,mag,mag_err):
    chi_square += ((cal_y-y)**2)/(chi**2)

print("Chi Square is for Cubic is : ",chi_square)
print("Reduced Chi Square is : ",chi_square/(len(time)-4))