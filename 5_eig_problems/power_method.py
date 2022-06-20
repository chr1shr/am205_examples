#!/usr/bin/python3
import numpy as np

# Initialize the matrix and shift
A=np.array([[4.,1.],[1.,-2.]])
shift=3

# Choose an initial guess and set iteration counter
x=np.random.randn(2)
count=1

# Perform iteration until the relative eigenvalue change is below a
# tolerance
rel_change=1
lam=1e30
while rel_change>1e-6:
    lam_old=lam
    x_old=x

    # Power method steps
    y=np.dot((A-shift*np.eye(2)),x)
    x=y/np.linalg.norm(y)

    # Estimate lambda by comparing an entry of y and x_old
    lam=y[1]/x_old[1]
    print("Iteration %d: lam=%.10g" % (count,lam))
    count+=1

    # Compute the relative change in the estimate of lambda
    rel_change=abs((lam-lam_old)/lam)

# Apply shift
lam=lam+shift

print("\nPower method with shift %d converged to %g" %(shift,lam))
