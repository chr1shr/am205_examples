#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg
from math import *

# ODE parameters
alpha=0.5
beta=-2.0
gamma=0.1

# Length of interval and boundary conditions
c_1=0.0
c_2=0.0
a=0.0
b=1.0

# Set grid resolution
n=100
h=(b-a)/(n-1)
x=np.linspace(a,b,n)

# Generate the centered difference differentiation matrix for u'
f=1.0/(2*h)
D1=np.diag(-np.ones(n-1)*f,-1)+np.diag(np.ones(n-1)*f,1)

# Generate the centered difference differentiation matrix for u''
f=1/(h*h)
D2=np.diag(-np.ones(n)*f*2)+np.diag(np.ones(n-1)*f,1)+np.diag(np.ones(n-1)*f,-1)

# Build the system matrix, A
A=-alpha*D2+beta*D1+gamma*np.identity(n)

# Define the right-hand side vector
F=np.array([-alpha*exp(z)*(4*pi*cos(2*pi*z)+(1-4*pi*pi)*sin(2*pi*z))+ \
beta*exp(z)*(sin(2*pi*z)+2*pi*cos(2*pi*z))+ \
gamma*exp(z)*sin(2*pi*z) for z in x])

# Set first and last rows of A to enforce Dirichlet conditions
A[0,0]=1
A[0,1]=0
A[n-1,n-2]=0
A[n-1,n-1]=1

# Set first and last rows of F
F[0]=c_1
F[n-1]=c_2

# Solve the linear system
U=np.linalg.solve(A,F)

# Print the exact and approximate solutions
for i in range(n):
    uex=exp(x[i])*sin(2*pi*x[i])
    print x[i],U[i],uex,U[i]-uex
