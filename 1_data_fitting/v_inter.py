#!/usr/bin/python
from math import *
import numpy as np

# Initialize x points and function values
n=5
x=np.linspace(0,3,n)
y=np.array([exp(-q) for q in x])

# Solve Vandermonde problem
V=np.vander(x)
b=np.linalg.solve(V,y)

# Add optional random perturbation
#b+=1e-6*np.random.rand(n);

# Plot interpolant
xx=0
while xx<3:

    # Use Horner's method to construct polynomial. Note that because of
    # Python's Vandermonde ordering convention, b[0] holds the coefficient of
    # the highest power.
    yy=b[0];
    for i in range(1,n):
        yy*=xx
        yy+=b[i]

    # Print output and increment x position
    print xx,yy,exp(-xx),yy-exp(-xx)
    xx+=0.01
