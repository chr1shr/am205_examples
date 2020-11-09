#!/usr/bin/python3
from math import exp

# Initial variables and constants
y=1
t=0
h=0.1
hh=h*0.5
qh=h*0.25
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

    # Four Euler quarter steps
    y_4=y
    for i in range(4):
        y_4=y_4+qh*(lam*y_4)

    # Richardson extrapolation (2-1) and (4-2)
    yr1=y_2+(y_2-y_1)/(2-1)
    yr2=y_4+(y_4-y_2)/(2-1)

    # Richardson extrapolation of Richardson extrapolations
    y=yr2+(yr2-yr1)/(4-1)

    # Update time
    t+=h
