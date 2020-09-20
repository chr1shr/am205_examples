#!/usr/bin/python
from math import *
import numpy as np
import matplotlib.pyplot as plt

# Vandermonde interpolation function
n=12
def vand_f(x,b):
    fx=b[0]
    for i in range(n-1):
        fx*=x
        fx+=b[i+1]
    return fx

# Create data and a truncated Vandermonde matrix
x=np.linspace(0,1,50)
A=np.vander(x,n)
y=np.cos(4*x)

# Solve using the least-squares function
b1=np.linalg.lstsq(A,y,rcond=None)[0]

# Solve the normal equations directly
AT=np.transpose(A)
ATA=np.dot(AT,A)
print("Condition number: ",np.linalg.cond(ATA))
b2=np.linalg.solve(ATA,np.dot(AT,y))

# Evaluate difference between the two parameter sets
print(b1-b2)

# Plot results
xnew=np.linspace(0,1,200)
vnew=[vand_f(q,b1) for q in xnew]
v2new=[vand_f(q,b2) for q in xnew]
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,'o',xnew,vnew,'-',xnew,v2new)
plt.legend(['data','least sq.','direct'],loc='best')
plt.show()
