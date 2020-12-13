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
