alpha=np.dot(np_A_t,np_A)
epsilon=np.linalg.inv(alpha)
beta=np.dot(np_A_t,np_b)