#!/usr/bin/python
# Import math functions
from math import *

# Initial variables and constants
x=1
t=0
dt=0.1

# Choose the constant in the ODE, dx/dt=-lam*x. We need -2=<dt*lam=<0 for
# stability 
lam=-25

# Apply Euler step until t>6
while t<=2:

    # Analytic solution
    xexact=exp(lam*t)
    
    # Print the solutions and error
    print t,x,xexact,x-xexact
    
    # Euler step
    x=x+dt*(lam*x)

    # Update time
    t+=dt
