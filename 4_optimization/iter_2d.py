#!/usr/bin/python3
from math import sqrt

# Function to perform root-finding on
def f(x1,x2):
    return (x1*x1+x2*x2-1,5*x1*x1+21*x2*x2-9)

# Function to print out solution
def print_sol(k,x1,x2):
    (f1,f2)=f(x1,x2)
    print("%4d %18.12g %18.12g %19.12g %19.12g" \
          %(k,x1,x2,f1,f2))

# Define starting position
(x1,x2)=(0.,0.)
print_sol(0,x1,x2)

# Perform fixed-point iteration
for k in range(1,31):
    (x1,x2)=(sqrt(1-x2*x2),sqrt((9.-5.*x1*x1)/21.))
    print_sol(k,x1,x2)
