#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

# Make an arbitrary vector
x=np.array([1.2,0.5,-0.1,2.3,-1.05,-2.35])

# Calculate the p-norm for a range of values of p
pr=range(1,100)
nx=[np.linalg.norm(x,p) for p in pr]

# Calculate the infinity norm
ni=[np.linalg.norm(x,np.inf) for p in pr]

# Plot the norms
plt.plot(pr,nx,pr,ni)
plt.xlabel('p')
plt.ylabel('norm value')
plt.legend(['p-norm','infinity norm'],loc='best')
plt.show()
