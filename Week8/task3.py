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