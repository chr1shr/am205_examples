#!/usr/bin/python
# Import math functions
from math import *

# Initial variables and constants
y=1
t=0
dt=0.1

# Choose the constant in the ODE, dx/dt=-lam*x. We need -2=<dt*lam=<0 for
# stability.
lam=-25

# Apply Euler step until t>2
while t<=2:

    # Analytical solution
    yexact=exp(lam*t)

    # Print the solutions and error
    print t,y,yexact,y-yexact

    # Euler step
    y=y+dt*(lam*y)

    # Update time
    t+=dt
