import matplotlib.pyplot as plt
speed=int(60)
time=int(0)
MAX_TIME=int(120)
distance=0
x=[]
y=[]
while(time<=MAX_TIME):
    distance=speed*time
    x.append(time)
    y.append(distance)
    time=time+10

import numpy as np
t=np.linspace(0,120,13) #minutes
d=speed*t/60.0 # in units of km
plt.plot(t,d)
plt.xlabel('Time in Minutes')
plt.ylabel('Distance in Kilometres')
plt.title('Distance-Time Graph') 
plt.show()