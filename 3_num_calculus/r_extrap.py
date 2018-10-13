#!/usr/bin/python
# Import math functions
from math import *

# Initial variables and constants
x=1
t=0
dt=0.05
hdt=dt*0.5
lam=0.5

# Apply Richardson method until t>2
while t<=2:

    # Analytic solution
    xexact=exp(lam*t)

    # Print the solutions and error
    print t,x,xexact,x-xexact

    # Euler step
    x_1=x+dt*(lam*x)

    # Two Euler half steps
    xh=x+hdt*(lam*x)
    x_2=xh+hdt*(lam*xh)

    # Richardson extrapolation
    x=x_2+(x_2-x_1)/(2-1)

    # Update time
    t+=dt
