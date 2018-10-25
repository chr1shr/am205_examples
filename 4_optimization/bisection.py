#!/usr/bin/python
from math import *

# Function to consider
def f(x):
    return x*x-4*sin(x)

# Initial interval: assume f(a)<0 and f(b)>0
a=1
b=3

# Bisection search
while b-a>1e-8:
    print a,b
    c=0.5*(b+a)
    if f(c)<0: a=c
    else: b=c

print "# Root at",0.5*(a+b)
