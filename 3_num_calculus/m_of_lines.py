#!/usr/bin/python3
import numpy as np
from scipy.integrate import odeint
from math import exp

# Grid size and snapshots
m=64
snaps=40

# RHS of ODE system from semi-discretization
def deriv(u,t):
    return -cidx*(u-np.roll(u,1))

# PDE-related constants
c=0.1
dx=1.0/m
cidx=c/dx
dt=0.1

# Initial condition
uinit=np.empty((m))
for i in range(m):
    x=dx*i
    uinit[i]=exp(-20*(x-0.5)**2)

# Define the times for saving snapshots
time=np.linspace(0,dt*snaps,snaps+1)

# Integrate the semi-discretized PDE
u=odeint(deriv,uinit,time);

# Output results
for j in range(m):
    e=[str(j*dx)]
    for i in range(snaps+1):
        e.append(str(u[i,j]))
    print(" ".join(e))
