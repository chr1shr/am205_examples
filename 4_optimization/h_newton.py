#!/usr/bin/python3
import numpy as np
from himmelblau import *

# Find minimum using Newton's method
x=np.array([5,5])
s=1e10
print(x[0],x[1],f(x[0],x[1]))
while np.linalg.norm(s)>1e-12:

    # Take a Newton step by solving the linear system constructed using the
    # Hessian and gradient
    s=np.linalg.solve(hess_f(x[0],x[1]),-grad_f(x[0],x[1]))
    x=x+s

    # Print the components of the current position and the norm of the gradient
    print(x[0],x[1],f(x[0],x[1]),np.linalg.norm(s))
