#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg
from math import *

# Function to consider
def f(z):
    return 1/(2+cos(10*z))

# Derivative
def df(z):
    return 10*sin(10*z)/(2+cos(10*z))**2

# Differentiation matrix
n=100
h=1/float((n-1))
D=np.diag(-np.ones(n)/h)+np.diag(np.ones(n-1)/h,1)

# Fix the final row
D[n-1,n-2]=-1/h
D[n-1,n-1]=1/h

# Look at the fixed matrix
plt.spy(D)
plt.show()

# Plot function
x=np.linspace(0,1,n)
y=np.array([1/(2+cos(10*xx)) for xx in x])
plt.plot(x,y)
plt.show()

# Calculate derivative and plot
dy=np.dot(D,y)
plt.plot(x,y,x,dy)
plt.show()

# Plot error
err=np.array([dy[i] - df(x[i]) for i in range(n)])
plt.plot(x,err)
plt.show()
