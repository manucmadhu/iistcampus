# Task1: Read column number 3 (time in day) and 10 (flux) of the LC-coarse.dat
# data files. Store the data into an array. Do not forget to skip the first three lines
# of the data files and note that value of the flux is very small (10-8 order). Hint:
# you can use “loadtxt”
import numpy as np
import matplotlib.pyplot as plt
# data=np.loadtxt('Week4\LC-coarse.dat',skiprows=3)  #to load the entire dat aand skip the three rows
col3,col10=np.loadtxt('Week4\LC-coarse.dat',skiprows=3,usecols=(2,9),unpack=True)
# Task2: Consider a regular time interval (bin) of 1 day and interpolate the missing
# data in LC-course.dat using Lagrange method of linear polynomial. 
import numpy as np
def lagrange(t, col3, col10):
    # If t exactly matches a known point
    if t in col3:
        ind = np.where(col3 == t)[0][0]
        return float(col10[ind])
    else:
        
        x0 = col3[0]      # largest value < t
        x1 = col3[1]        # smallest value > t
        
        # Corresponding flux values
        y0 = float(col10[np.where(col3 == x0)[0][0]])
        y1 = float(col10[np.where(col3 == x1)[0][0]])
        
        # Linear Lagrange interpolation
        flux = y0 * (t - x1) / (x0 - x1) + y1 * (t - x0) / (x1 - x0)
        return flux
time=[col3[0],col3[1]]
x=sum(time)/2
y_val=[col10[0],col10[1]]
y=lagrange(x,time,y_val)
print(x,y)