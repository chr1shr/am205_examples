#!/usr/bin/python
import numpy as np

# Initialize the matrix and shift
A=np.array([[4.,1.],[1.,-2.]])
shift=-1

# Choose an initial guess
x=np.random.randn(2,1)

# Set a tolerance and initialize the guess of the eigenvalue
TOL=1.e-6
lam=1e30

count=1
while 1:
    lam_old=lam
    x_old=x

    # Power method steps
    y=np.dot((A-shift*np.eye(2)),x)
    x=y/np.linalg.norm(y)

    # Estimate lambda by comparing an entry of y and x_old
    lam=y[1,0]/x_old[1,0]
    lam_diff=abs((lam-lam_old)/lam)
    print("Iteration %d: lam=%.10g" % (count,lam))

    # Break out of the loop if lam_diff < TOL
    if lam_diff<TOL:
        break

    count=count+1

# Apply shift
lam=lam+shift

print("\nPower method with shift %d converged to %g" %(shift,lam))
