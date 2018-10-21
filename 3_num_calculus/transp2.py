#!/usr/bin/python
import numpy as np
from math import *

# Grid size
m=64
a=np.zeros((m))
b=np.zeros((m))
snaps=100
iters=40
z=np.zeros((m,snaps+1))

# PDE-related constants
c=0.1
dx=1.0/m
dt=0.01
nu=c*dt/dx

# Initial condition
for i in range(m):
    x=dx*i
    a[i]=exp(-20*(x-0.5)**2)
z[:,0]=a

# Integrate the PDE using centered-differencing
for i in range(1,snaps+1):
    for k in range(iters):
        for j in range(m):
            jl=j-1
            if jl<0: jl+=m
            jr=j+1
            if jr>=m: jr-=m

            b[j]=a[j]-0.5*nu*(a[jr]-a[jl])
        a=np.copy(b)
    z[:,i]=a

# Output results
for j in range(m):
    e=[str(j*dx)]
    for i in range(snaps+1):
        e.append(str(z[j,i]))
    print " ".join(e)
