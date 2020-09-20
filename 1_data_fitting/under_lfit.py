#!/usr/bin/python3
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

# Construct rectangular Vandermonde matrix
x=np.linspace(0.2,1,5)
A=np.vander(x,n)
y=np.cos(4*x)

# Solve using least squares routine. For an underdetermined system this finds
# the interpolant that minimizes the norm of the parameter vector b1.
b1=np.linalg.lstsq(A,y,rcond=None)[0]
print("lstsq solve : Norm(r): ",np.linalg.norm(y-np.dot(A,b1)))

# Solve using normal equations + regularizer
mu=0.05
AT=np.transpose(A)
ATA=np.dot(AT,A)
print("\nCondition number: ",np.linalg.cond(ATA))
b2=np.linalg.solve(ATA+mu*mu*np.identity(n),np.dot(AT,y))
print("Normal eqs. : Norm(r): ",np.linalg.norm(y-np.dot(A,b2)))

# Plot the two solutions
xnew=np.linspace(0,1,200)
vnew=[vand_f(q,b1) for q in xnew]
v2new=[vand_f(q,b2) for q in xnew]
plt.plot(x,y,'o',xnew,vnew,xnew,v2new)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['data','lstsq routine','Normal'],loc='best')
plt.show()
