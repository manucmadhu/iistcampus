import math
import numpy as np
import matplotlib.pyplot as plt
'''
N0=int(1000)
to=5
MAX_LIMIT=int(20)
time=int(0)
x=[]
y=[]
N=0
while(time<=20):
    N=N0*math.exp(-time/to)
    x.append(time)
    y.append(N)
    time=time+1
# plot.plot(x,y)
plot.semilogy(x,y)
plot.xlabel('Time in s')
plot.ylabel('Number of Nuclei in Sample')
# plot.show()
to=10
time=int(0)
x=[]
y=[]
N=0
while(time<=20):
    N=N0*math.exp(-time/to)
    x.append(time)
    y.append(N)
    time=time+1
# plot.plot(x,y)
plot.semilogy(x,y)
# plot.xlabel('Time in s')
# plot.ylabel('Number of Nuclei in Sample')
plot.show()
'''

'''
N0 = 1000.
t = np.linspace(0,20,21)
tau1 = 5.0 ; tau2 = 10.
N1=N0*np.exp(-t/tau1)
N2=N0*np.exp(-t/tau2)
plt.plot(t,N1,'r-',lw=2,label='tau = 5',alpha=0.3)
plt.plot(t,N2,'g-',lw=3,label='tau = 10')
plt.xlabel('Time in s')
plt.ylabel('Number of Nuclei in Sample')   
plt.legend()
plt.show() 
'''
def radioact(N0,tau):
    t = np.linspace(0,20,21)
    N1=N0*np.exp(-t/tau)
    return N1
def main():
    N1=radioact(1000.0,5.0)
    N2=radioact(1000.0,10.0)
    t = np.linspace(0,20,21)
    plt.plot(t,N1,'r-',lw=2,label='tau = 5',alpha=0.3)
    plt.plot(t,N2,'g-',lw=3,label='tau = 10')
    plt.xlabel('Time in s')
    plt.ylabel('Number of Nuclei in Sample')   
    plt.legend()
    plt.show() 
if __name__ == "__main__":
    main()