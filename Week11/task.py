import numpy as np
import matplotlib.pyplot as plt
data=np.loadtxt("Week11\data11.txt",delimiter=',')
# print(data) # The data is loaded to the array properly

# Task 1 and Task 2 is theory done in paper

N_data=len(data)

# Define negative log likelihood function

def log_likelihood(alpha, x_data):

    n = len(x_data)
    
    
    if alpha < -1.0: 
        return -np.inf 
  
    
    term1 = n * np.log(1.5)              # n * ln(3/2)
    term2 = n * (-1 * np.log(3 + alpha)) # n * -ln(3 + alpha)
    term3 = np.sum(np.log(1 + alpha * x_data**2))
    
    log_L = term1 + term2 + term3
    
    return log_L

# to check the value of log likelihood over a range of alpha values


Log_like=[]
alpha_range=np.arange(0.1,10,0.1)
for i in alpha_range:
    Log_like.append(log_likelihood(i,data)) 
print(min(Log_like))
# print(Log_like)
plt.plot(alpha_range,Log_like)
plt.show() 
#from plot observed that the minimum is near to alpha=5


# Create the log maximisation function

#definining the range of values of alpha
i=0.001 
j=10.0
max_alpha=4
while(i<j):
    k=(i+j)/2
    min=log_likelihood(i,data)
    mid=log_likelihood(k,data)
    max=log_likelihood(j,data)
    
    maxima=log_likelihood(max_alpha,data)
    # print(i,j,k)
    if(maxima < mid ):
        # print(min_alpha,k)
        max_alpha=k
    
    if(min < mid):
        i=k
    elif(max < mid ):
        j=k
    else:
        break
print(max_alpha)

L_max=log_likelihood(max_alpha,data)
Normalized_L=Log_like/L_max
print(L_max)

plt.plot(alpha_range,Normalized_L)
plt.show()

