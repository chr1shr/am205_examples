#!/usr/bin/python3
import numpy as np
import scipy.optimize as op
from himmelblau import *

# Calculates the Himmelblau function (accepting a vector input)
def f_vec(z):
    ff=f(z[0],z[1])
    print(z[0],z[1],ff)
    return ff

# Calculates the gradient of the Himmelblau function (accepting a vector input)
def grad_f_vec(z):
    return grad_f(z[0],z[1])

# Find minimum using BFGS
x=op.fmin_bfgs(f_vec,x0=np.array([-1.2,-3]),fprime=grad_f_vec,disp=False)
#print("Solution is (%.17g,%.17g)"%(x[0],x[1]))
