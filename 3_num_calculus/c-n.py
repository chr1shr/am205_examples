#!/usr/bin/python3
import numpy as np
from math import sin,exp,pi,sqrt

# Solves the heat equation using the Crank-Nicolson method using
# a given number of grid points, and computes the L2 norm to a reference
# solution
def c_n(m):
    a=np.empty((m+1))
    b=np.empty((m+1))

    # Set grid spacing, timestep, and mu
    dx=1.0/m
    dt=0.1/m
    mu=dt/(dx*dx)

    # Set initial condition
    for j in range(m+1):
        a[j]=sin(j*pi*dx)
    b[0]=0;b[m]=0

    # Create linear system matrix for implicit step in Crank-Nicolson. Note
    # that here the matrix is represented and solved using dense linear
    # algebra, which is inefficient for large m. Using a dedicated tridiagonal
    # solver would be more efficient.
    A=np.diag(np.ones(m+1)*(1+mu))+ \
      np.diag(np.ones(m)*(-0.5*mu),1)+ \
      np.diag(np.ones(m)*(-0.5*mu),-1)
    A[0,0]=1;A[0,1]=0
    A[m,m]=1;A[m,m-1]=0

    # Perform timesteps
    for i in range(m):
        for j in range(1,m):
            b[j]=(1-mu)*a[j]+0.5*mu*(a[j-1]+a[j+1])
        a=np.linalg.solve(A,b)

    # Evaluate L2 norm to reference solution
    s=0;f=exp(-pi*pi*0.1)
    for j in range(1,m):
        du=a[j]-sin(j*pi*dx)*f
        s+=du*du
    return sqrt(dx*s)

# Loop over a range of grid sizes
m=4
while m<=512:

    # Print the number of grid points, the grid spacing, and the L2 norm
    # for Crank-Nicolson
    print(m,1.0/m,c_n(m))

    # Double the number of grid points
    m*=2
