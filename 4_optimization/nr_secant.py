#!/usr/bin/python
from math import *

def f(x):
    return exp(x)-x-2

def df(x):
    return exp(x)-1

# Newton-Raphson setup
xa=2

# Secant setup
xb=2
xbb=2.1
fxbb=f(xbb)

for i in range(20):

    # Newton-Raphson
    xa=xa-f(xa)/df(xa)

    # Secant
    fxb=f(xb)
    tem=xb-f(xb)*(xb-xbb)/(fxb-fxbb)
    xbb=xb;fxbb=fxb
    xb=tem

    print xa,f(xa),xb,f(xb)
