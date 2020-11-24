#!/usr/bin/python3
from math import exp

# Function to perform root-finding on
def f(x):
    return exp(x)-x-2

# Analytical derivative (only needed for Newton)
def df(x):
    return exp(x)-1

# Newton method setup
xa=2

# Secant method setup
xb=2

# Initialize previous step x_{k-1} in secant method
xbb=2.1
fxbb=f(xbb)

for k in range(20):

    print("%17.10g %17.10g %17.10g %17.10g" \
          %(xa,f(xa),xb,f(xb)))

    # Newton
    xa=xa-f(xa)/df(xa)

    # Secant
    fxb=f(xb)
    tem=xb-fxb*(xb-xbb)/(fxb-fxbb)
    xbb=xb;fxbb=fxb
    xb=tem
