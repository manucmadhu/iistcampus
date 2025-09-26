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
        # Points before t
        before = col3[col3 < t]
        # Points after t
        after = col3[col3 > t]
        
        # Check boundaries
        if before.size == 0 or after.size <2:
            return np.nan  # or handle extrapolation if desired
        
        # Nearest neighbors
        x0 = before[-1]      # largest value < t
        x1 = after[0]        # smallest value > t
        x2= after[1]
        # Corresponding flux values
        y0 = float(col10[np.where(col3 == x0)[0][0]])
        y1 = float(col10[np.where(col3 == x1)[0][0]])
        y2= float(col10[np.where(col3 == x2)[0][0]])
        # Linear Lagrange interpolation
        flux = ( y0 * (t - x1) * (t - x2) / ((x0 - x1)*(x0 - x2)) +
         y1 * (t - x0) * (t - x2) / ((x1 - x0)*(x1 - x2)) +
         y2 * (t - x0) * (t - x1) / ((x2 - x0)*(x2 - x1)) )

        return flux
time = np.linspace(np.min(col3), np.max(col3),int(abs(min(col3)-max(col3))))

print(time)
flux_range=[]
for t in time:
    flux=lagrange(t,col3,col10)
    flux_range.append(flux)
plt.plot(time,flux_range,label="Lagrange Found")
col3,col10=np.loadtxt('Week4\LC-1543.dat',skiprows=3,usecols=(2,9),unpack=True)
plt.plot(col3,col10,'--',label="Data2")
plt.legend()
plt.show()  
