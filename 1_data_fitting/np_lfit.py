#!/usr/bin/python
from math import *
import numpy as np
import matplotlib.pyplot as plt

# Maximum exponential term, and total number of terms
n=5
s=2*n+1

# Function to evaluate sum of exponentials at a particular x
def sum_exp_f(x,b):
    fx=0
    for i in range(s):
        fx+=b[i]*exp((i-n)*x)
    return fx

# Create matrix where each column is an exponential, as opposed to a monomial
# in the usual Vandermonde construction 
x=np.linspace(-1,1,20)
A=np.array([[exp((i-n)*xx) for i in range(s)] for xx in x])
y=np.cos(4*x)*np.exp(-x)

# Solve using the least-squares function
b=np.linalg.lstsq(A,y)[0]
print "Norm(r)/Norm(b) :",np.linalg.norm(y-np.dot(A,b))/np.linalg.norm(b)

# Plot results
xnew=np.linspace(-1,1,200)
vnew=[sum_exp_f(q,b) for q in xnew]
plt.plot(x,y,'o',xnew,vnew,'-')
plt.legend(['data','least sq.'],loc='best')
plt.show()
