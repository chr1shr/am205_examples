#!/usr/bin/python3
import numpy as np

# Initialize the matrix
A=np.array([[6,1,2],[1,0,-4],[2,-4,4]])

# Loop over a range of shifts
for shift in np.linspace(-10,10,201):
    
    # Set up starting vector
    x=np.array((1,0.7,0.3))
    count=1

    # Perform inverse iteration until the relative eigenvalue change is
    # below a tolerance
    rel_change=1
    lam=1e30
    while rel_change>1e-8:
        lam_old=lam
        x_old=x

        # Solve linear system and normalize
        y=np.linalg.solve((A-shift*np.eye(3)),x)
        x=y/np.linalg.norm(y)

        # Estimate eigenvalue by comparing an entry of y and x_old
        lam=y[1]/x_old[1]
        rel_change=abs((lam-lam_old)/lam)
        count+=1

    # Output the shift, the computed eigenvalue, and the number of
    # iterations required
    print(shift,1/lam+shift,count)
