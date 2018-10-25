#!/usr/bin/python
import numpy as np
from scipy.optimize import *

def f(x):
    print x
    (x1,x2,w1,w2)=(x[0],x[1],x[2],x[3])
    x1s=x1*x1
    x2s=x2*x2
    f=np.array([w1+w2-2,w1*x1+w2*x2, \
           w1*x1s+w2*x2s-2./3,w1*x1s*x1+w2*x2s*x2])
    return f

def fprime(x):
    print "fprime called"
    (x1,x2,w1,w2)=(x[0],x[1],x[2],x[3])
    x1s=x1*x1
    x2s=x2*x2
    return np.array([[0,0,1,1],[w1,w2,x1,x2], \
           [2*w1*x1,2*w2*x2,x1s,x2s],[3*w1*x1s,3*w2*x2s,x1s*x1,x2s*x2]])

print "fsolve without Jacobian:"
x0=np.array([-1,1,1,1])
print fsolve(f,x0)

print "\nfsolve with Jacobian:"
x0=np.array([-1,1,1,1])
print fsolve(f,x0,fprime=fprime)
