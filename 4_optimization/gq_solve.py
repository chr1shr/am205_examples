#!/usr/bin/python3
import numpy as np
from scipy.optimize import fsolve

# Mode: 0 = custom Newton method 
#       1 = fsolve with Jacobian
#       2 = fsolve without Jacobian
mode=2

# Function to root-find on
def f(x):
    print(x)
    (x1,x2,w1,w2)=(x[0],x[1],x[2],x[3])
    x1s=x1*x1;x2s=x2*x2
    f=np.array([w1+w2-2,w1*x1+w2*x2, \
                w1*x1s+w2*x2s-2./3,w1*x1s*x1+w2*x2s*x2])
    return f

# Analytical Jacobian
def fprime(x):
    print("# fprime called")
    (x1,x2,w1,w2)=(x[0],x[1],x[2],x[3])
    x1s=x1*x1;x2s=x2*x2
    return np.array([[0,0,1,1],[w1,w2,x1,x2], \
           [2*w1*x1,2*w2*x2,x1s,x2s],[3*w1*x1s,3*w2*x2s,x1s*x1,x2s*x2]])

# Initial condition
x0=np.array([-1.,1.,1.,1.])

# Custom Newton method implementation
if mode==0:
    xk=x0
    fk=f(xk)
    err=np.linalg.norm(fk)
    while err>1e-14:
        xk-=np.linalg.solve(fprime(xk),fk)
        fk=f(xk)
        err=np.linalg.norm(fk)

# Call fsolve routines with and without Jacobian
elif mode==1:
    xk=fsolve(f,x0,fprime=fprime)
else:
    xk=fsolve(f,x0)

# Print solution
print("\n# Solution is",xk)
