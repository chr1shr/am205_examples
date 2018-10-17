#!/usr/bin/python
# Import math functions
from math import *

# Initial variables and constants
y=1
t=0
dt=0.05
hdt=dt*0.5
lam=0.5

# Apply Richardson method until t>2
while t<=2:

    # Analytical solution
    yexact=exp(lam*t)

    # Print the solutions and error
    print t,y,yexact,y-yexact

    # Euler step
    y_1=y+dt*(lam*y)

    # Two Euler half steps
    yh=y+hdt*(lam*y)
    y_2=yh+hdt*(lam*yh)

    # Richardson eytrapolation
    y=y_2+(y_2-y_1)/(2-1)

    # Update time
    t+=dt
