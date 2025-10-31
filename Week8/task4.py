import numpy as np
import matplotlib.pyplot as plt

all_mean=[]
for i in [5,10,100]:
    mean_arr=[]
    for j in range(10**4):
        y=np.random.uniform(low=0.0,high=1.0,size=i)
        x=-np.log(y)
        mean=np.sum(x)/len(x)
        mean_arr.append(mean)
    all_mean.append(mean_arr)
    plt.hist(mean_arr,bins=50,edgecolor='black')
    plt.title(f'N={i},M=1e4')
    plt.legend()
    plt.show()


mean_array=[]
variance_array=[]
for k in range(len(all_mean)):
    m=sum(all_mean[k])/len(all_mean[k])
    varaince=0
    for z in range(len(all_mean[k])):
        varaince += (m-all_mean[k][z])**2
    varaince /= len(all_mean[k])
    mean_array.append(m)
    variance_array.append(varaince)
    
print('The mean corresponding to 5,10 and 100 are ',mean_array)
print('The variance corresponding to 5,10 and 100 are ',variance_array)

#as the Values of N increase the Variance decreases and become more centralized towards Gaussian
'''Thus when we take sufficiently large number of samples we get a gaussian probability distribution regardless the origin of the function
Here in the case the origin is exponential and the final outcome is Gaussian'''