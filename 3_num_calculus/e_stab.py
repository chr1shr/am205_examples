#!/usr/bin/python3
from math import exp

# Initial variables and constants
y=1
t=0
h=0.1

# Choose the constant in the ODE, dy/dt=-lam*y. We need -2=<h*lam=<0 for stability.
lam=-21

# Apply forward Euler step until t>1
while t<=1:

    # Analytical solution
    yexact=exp(lam*t)

    # Print the solutions and error
    print(t,y,yexact,y-yexact)

    # Euler step
    y=y+h*(lam*y)

    # Update time
    t+=h
