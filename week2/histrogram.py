import math
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randint(150, 181, 999)  # random ints 150–180

min_value=min(data)
count=[]
bins = list(range(150, 185, 5))
for i in range(150,185,5):
    count.append(0)
for i in data:
    index=math.floor((i-min_value)/5)
    count[index]=count[index]+1
plt.bar(bins,count,width=5,edgecolor='black')
plt.xlabel("Value bins")
plt.ylabel("Count")
plt.title("Histogram of Random Values")
plt.show()
