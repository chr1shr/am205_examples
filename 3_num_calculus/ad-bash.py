#!/usr/bin/python
# Import math functions
from math import *

lam=0.5
def f(x):
    return lam*x

# Initialize two values to exactly match solution
t=0
dt=0.05
y=[1,exp(lam*dt)]
t+=dt

# Apply second-order Adams-Bashforth scheme
while t<=2:

    # Analytical solution
    yexact=exp(lam*t)

    # Print the solutions and error
    print t,y[1],yexact,y[1]-yexact

    # Multi step
    yy=y[1]+dt*(1.5*f(y[1])-0.5*f(y[0]))
    y[0]=y[1]
    y[1]=yy

    # Update time
    t+=dt
