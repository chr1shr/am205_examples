#!/usr/bin/python
# Import math functions
from math import *

# Initial variables and constants
t=0
h=0.05
lam=2

# Function to integrate
def f(t,y):
    return cos(t)

# Starting values for modified Euler and improved Euler
yme=0
yie=0
yhe=0

# Apply Euler step until t>6
while t<=2:

    # Analytical solution
    yexact=sin(t)

    # Print the solutions and error
    print t,yme,yie,yhe,yexact,yme-yexact,yie-yexact,yhe-yexact

    # Modified Euler step
    k1=h*f(t,yme)
    k2=h*f(t+0.5*h,yme+0.5*k1)
    yme+=k2

    # Improved Euler step
    k1=h*f(t,yie)
    k2=h*f(t+h,yie+k1)
    yie+=0.5*(k1+k2)

    # Ralston's method
    k1=h*f(t,yhe)
    k2=h*f(t+2*h/3.,yhe+k1*2/3.)
    yhe+=0.25*k1+0.75*k2

    # Update time
    t+=h
