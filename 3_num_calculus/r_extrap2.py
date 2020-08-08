#!/usr/bin/python
# Import math functions
from math import *

# Initial variables and constants
x=1
t=0
dt=0.05
hdt=dt*0.5
qdt=dt*0.25
lam=0.5

# Apply Richardson method until t>2
while t<=2:

    # Analytical solution
    xexact=exp(lam*t)

    # Print the solutions and error
    print(t,x,xexact,x-xexact)

    # Euler step
    x_1=x+dt*(lam*x)

    # Two Euler half steps
    xh=x+hdt*(lam*x)
    x_2=xh+hdt*(lam*xh)

    # Four Euler quarter steps
    x_4=x
    for i in range(4):
        x_4=x_4+qdt*(lam*x_4)

    # Richardson extrapolation (2-1) and (4-2)
    xr1=x_2+(x_2-x_1)/(2-1)
    xr2=x_4+(x_4-x_2)/(2-1)

    # Richardson extrapolation of Richardson extrapolations
    x=xr2+(xr2-xr1)/(4-1)

    # Update time
    t+=dt
