#given quadratic equation ax^2 + bx +c
#solution is given by quadratic formula
#a=0.001 c=0.001 b=-1000.0
#write a small code to calculate x1 and x2
import numpy as np

a=0.001
c=0.001
b=-1000.0

def rootsolution(a,b,c): # find the solution with the quadratic equation -b+- sqrt(b^2-4ac)/2a
    k=np.sqrt((b**2) -(4*a*c))
    x1=(-b+k)/(2*a)
    x2=(-b-k)/(2*a)
    return x1,x2
x1,x2=rootsolution(a,b,c)
print("The Roots of the equation ax^2 + bx +c is :",x1,x2,"\n")
relative_error1=abs(1e6-x1)*100/x1
relative_error2=abs(1e-6-x2)*100/x2
#The Roots of the equation ax^2 + bx +c is : 999999.0 9.999894245993346e-07
# one is on the order of 10^7 and other 10^-7
print("Relative errors are :",relative_error1,"%",relative_error2,"%","\n")
def rootsolutionnew(a,b,c): # find the solution with the quadratic equation 2c/ -b-+sqrt(b^2-4ac)
    k=np.sqrt((b**2) -(4*a*c))
    x1= 2*c/-(b+k)
    x2=2*c/(k-b)
    return x1,x2
x1,x2=rootsolution(a,b,c)
x1,x2=rootsolutionnew(a,b,c)
print("The Roots of the equation ax^2 + bx +c is :",x1,x2,"\n")
relative_error1=abs(1e6-x1)*100/x1
relative_error2=abs(1e-6-x2)*100/x2
print("Relative errors are :",relative_error1,"%",relative_error2,"%")
#fundamental concept that the numerical computation may result in consequences and may result in many errors which need to be reduced
