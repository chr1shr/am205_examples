#!/usr/bin/python3
from scipy.optimize import linprog
import numpy as np

# Constraints
a=np.array([[1.,-1.,1.],[3.,2.,4.],[3.,2.,0.],[-1.,0,0],[0,-1,0],[0,0,-1]])
b=np.array([20.,42.,30.,0.,0.,0.])

# Coefficients in the objective function
c=np.array([-5.,-4.,-6.])

# Solve the linear program
options={'disp': 1}
sol=linprog(c,A_ub=a,b_ub=b,options=options)
print((sol['x']))
