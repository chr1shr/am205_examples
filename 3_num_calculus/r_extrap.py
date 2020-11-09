#!/usr/bin/python3
from math import exp

# Initial variables and constants
y=1
t=0
h=0.1
hh=h*0.5
lam=0.5

# Apply Richardson method until t>2
while t<=2:

    # Analytical solution
    yexact=exp(lam*t)

    # Print the solutions and error
    print(t,y,yexact,y-yexact)

    # Euler step
    y_1=y+h*(lam*y)

    # Two Euler half steps
    yh=y+hh*(lam*y)
    y_2=yh+hh*(lam*yh)

    # Richardson extrapolation
    y=y_2+(y_2-y_1)/(2-1)

    # Update time
    t+=h
