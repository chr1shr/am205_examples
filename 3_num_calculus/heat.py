#!/usr/bin/python3
import numpy as np
from math import *

# Grid size
m=64
a=np.zeros((m))
b=np.empty((m))
snaps=40
iters=400
z=np.empty((m,snaps+1))

# PDE-related constants. Change the timestep prefactor to 0.5001 to go slightly
# beyond the point of stability, where the 2-gridpoint oscillation will slowly
# grow.
dx=1.0/m
dt=0.1*dx*dx
mu=dt/(dx*dx)

# Initial condition
for j in range(m):
    x=dx*j
    if x>0.25 and x<0.75: a[j]=1
z[:,0]=a

# Integrate the PDE
for i in range(1,snaps+1):
    for k in range(iters):
        for j in range(m):
            jl=j-1
            if jl<0: jl+=m
            jr=j+1
            if jr>=m: jr-=m
            b[j]=((1-2*mu)*a[j]+mu*(a[jl]+a[jr]))
        a=np.copy(b)
    z[:,i]=a

# Output results
for j in range(m):
    e=[str(j*dx)]
    for i in range(snaps+1):
        e.append(str(z[j,i]))
    print(" ".join(e))
