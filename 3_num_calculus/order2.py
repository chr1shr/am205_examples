#!/usr/bin/python3
from math import cos,sin,exp

# Initial variables and constants
t=0
h=0.05

# Function to integrate
def f(t,y):
    return exp(-0.5*t*t)-y*t

# Starting values for modified Euler, improved Euler, and Ralston
yme=0
yie=0
yre=0

# Apply timesteps until t>6
while t<=6:

    # Analytical solution
    yexact=t*exp(-0.5*t*t)

    # Print the solutions and error
    print(t,yme,yie,yre,yexact,yme-yexact,yie-yexact,yre-yexact)

    # Modified Euler step
    k1=h*f(t,yme)
    k2=h*f(t+0.5*h,yme+0.5*k1)
    yme+=k2

    # Improved Euler step
    k1=h*f(t,yie)
    k2=h*f(t+h,yie+k1)
    yie+=0.5*(k1+k2)

    # Ralston's method
    k1=h*f(t,yre)
    k2=h*f(t+2*h/3.,yre+k1*2/3.)
    yre+=0.25*k1+0.75*k2

    # Update time
    t+=h
