#!/usr/bin/python
from scipy.optimize import linprog
import numpy as np

# Constraints
a=matrix([[1.,3.,3.,-1.,0,0],[-1.,2.,2.,0,-1.,0],[1.,4.,0.,0.,0.,-1.]])
b=matrix([20.,42.,30.,0.,0.,0.])

# Components of the functional
c=[-5.,-4.,-6.]

# Solve the linear program
options={'disp': 1}
sol=linprog(c,A_ub=a,b_ub=b,options=options)
print((sol['x']))
