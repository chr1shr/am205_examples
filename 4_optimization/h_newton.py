#!/usr/bin/python
import numpy as np

# Himmelblau function - a common example used for testing optimization algorithms
def f(x,y):
    return (x*x+y-11)**2+(x+y*y-7)**2

# Gradient of the Himmelblau function
def grad_f(x,y):
    return np.array([4*x*(x*x+y-11)+2*(x+y*y-7),2*(x*x+y-11)+4*y*(x+y*y-7)])

# Hessian of the Himmelblau function
def hess_f(x,y):
    return np.array([[4*(x*x+y-11)+8*x*x+2,4*x+4*y],[4*x+4*y,2+4*(x+y*y-7)+8*y*y]])

# Find minimum using Newton's method
x=np.array([-4,-4])
s=1e10
while np.linalg.norm(s)>1e-8:

    # Take a Newton step by solving the linear system constructed using the
    # Hessian and gradient
    s=np.linalg.solve(hess_f(x[0],x[1]),-grad_f(x[0],x[1]))
    x=x+s

    # Print the components of the current position and the norm of the gradient
    print x[0],x[1],np.linalg.norm(s)
