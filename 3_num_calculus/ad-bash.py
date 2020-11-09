#!/usr/bin/python3
from math import exp

# RHS of differential equation to integrate
lam=0.5
def f(y):
    return lam*y

# Function to perform Adams-Bashforth integration over the range 0<=t<=2, and
# evaluate error
def ad_bash(n):

    # Calculate timestep size
    h=2./n

    # Initialize two values to exactly match solution
    y=[1,exp(lam*h)]

    # Perform (n-1) Adams-Bashforth updates
    for i in range(n-1):
        yy=y[1]+h*(1.5*f(y[1])-0.5*f(y[0]))
        y[0]=y[1]
        y[1]=yy

    # Return error between numerical result and exact solution
    return y[1]-exp(lam*2)

# Evaluate error for different numbers of timesteps
n=1
while n<=65536:

    # Print the number of timesteps, the timestep size, and the error
    print(n,2./n,ad_bash(n))

    # Double the number of timesteps
    n*=2
