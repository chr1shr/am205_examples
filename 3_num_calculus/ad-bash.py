#!/usr/bin/python
# Import math functions
from math import *

lam=0.5
def f(x):
    return lam*x

# Initialize two values to exactly match solution
t=0
dt=0.05
x=[1,exp(lam*dt)]
t+=dt

# Apply second-order Adams-Bashforth scheme
while t<=2:

    # Analytic solution
    xexact=exp(lam*t)

    # Print the solutions and error
    print t,x[1],xexact,x[1]-xexact

    # Multi step
    xx=x[1]+dt*(1.5*f(x[1])-0.5*f(x[0]))
    x[0]=x[1]
    x[1]=xx

    # Update time
    t+=dt
