#!/usr/bin/python
import numpy as np
from math import *

# Grid size
m=64
a=np.zeros((m))
b=np.zeros((m))
snaps=40
iters=400
z=np.zeros((m,snaps+1))

# PDE-related constants. The timestep is chosen to be just larger than the
# point of stability, causing the 2-gridpoint oscillation to slowly grow.
alpha=0.1
dx=1.0/m
dt=0.501*dx*dx/alpha
nu=alpha*dt/(dx*dx)
lam=1

# Initial condition
for i in range(m):
    x=dx*i
    if x>0.25 and x<0.75: a[i]=1
z[:,0]=a

# Integrate the PDE
for i in range(1,snaps+1):
    for k in range(iters):
        for j in range(m):
            jl=j-1
            if jl<0: jl+=m
            jr=j+1
            if jr>=m: jr-=m
            b[j]=((1-2*nu)*a[j]+nu*(a[jl]+a[jr]))+dt*a[j]**3*0.01
        a=np.copy(b)
    z[:,i]=a

# Output results
for j in range(m):
    e=[str(j*dx)]
    for i in range(snaps+1):
        e.append(str(z[j,i]))
    print " ".join(e)
