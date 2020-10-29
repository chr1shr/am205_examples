#!/usr/bin/python3
from cvxopt import matrix,solvers

# Constraints
a=matrix([[1.,3.,3.,-1.,0,0],[-1.,2.,2.,0,-1.,0],[1.,4.,0.,0.,0.,-1.]])
b=matrix([20.,42.,30.,0.,0.,0.])

# Components of the functional
c=matrix([-5.,-4.,-6.])

# Solve the linear program
sol=solvers.lp(c,a,b)
print((sol['x']))
