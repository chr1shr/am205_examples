#!/usr/bin/python
from math import *
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the sum of absolute value of Lagrange polynomials 
def lsum(x,xp):
    ls=0
    for k in range(xp.size):
        xc=xp[k]
        li=1
        for l in range(xp.size):
            if l!=k:
                li*=(x-xp[l])/(xp[k]-xp[l])
        ls+=abs(li)
    return ls

# Control points (either linearly spaced, or Chebyshev)
n=16
#xp=np.linspace(-1,1,n)
xp=np.array([cos((2*j+1)*pi/(2*n)) for j in range(n)])

# Sample points
xx=np.linspace(-1,1,500)
yy=np.array([lsum(q,xp) for q in xx])

# Plot figure using Matplotlib
plt.figure()
plt.plot(xx,yy)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
