#administering the difference between round-off and truncation error
#for function f(x)=sin(x) calculate the derivative using taylor series equation 
#compare with original values and find the truncation error
#x0=pi/4 
#h=[-10e10,10e2]

import numpy as np
x0=np.pi/4

def taylordervative(h):
    return (np.sin(x0+h)-np.sin(x0))/h
    

h_space=np.logspace(-10,-2,500)#taking log-scale so as to cover larger set of values
#print(h)
og_value=[]
derivative_value=[]
for h in h_space:    
    og_value.append(np.cos(x0+h))
    derivative_value.append(taylordervative(h))
error=[]
for og, der in zip(og_value, derivative_value):
    error.append(abs(og - der)* 100 / abs(og))
import matplotlib.pyplot as plt
plt.loglog(h_space, error, label="Value or relative error")

# plt.xscale("log")
plt.xlabel("h (in log-space)")
plt.ylabel("Relative Error (%)")
plt.legend()
plt.show()
