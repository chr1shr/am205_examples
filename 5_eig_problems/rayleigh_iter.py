#!/usr/bin/python
import numpy as np
from math import *

# Setup
A=np.array([[5.,1.,1],[1.,6.,1.],[1.,1.,7.]])
x=np.array([[1],[1],[1]])/sqrt(3)

# Compute reference solution
[V,D]=np.linalg.eig(A)
eig_solution=V[0]

# set a tolerance and initialize guess of eigenvalue
TOL=1.e-10
sig=1e30

# Perform Rayleigh Quotient Iteration
count=1
while 1:
    sig_old=sig

    # Calculate Rayleigh quotient
    sig=np.dot(np.dot(x.T,A),x)/np.dot(x.T,x)

    # Perform inverse iteration
    A_shifted=A-sig*np.eye(3)
    y=np.linalg.solve(A_shifted,x)
    x=y/np.linalg.norm(y)

    sig_diff=abs((sig-sig_old)/sig)

    print("Iteration %d: eigenvalue error=%.10g" % (count,abs(sig-eig_solution)))

    # Break out of the loop if lambda_diff < TOL
    if sig_diff<TOL:
        break

    count=count+1

print("\nEigenvalues from eig are",V[0],V[1],V[2])
print("Eigenvalue from Rayleigh iteration is",sig[0,0])
