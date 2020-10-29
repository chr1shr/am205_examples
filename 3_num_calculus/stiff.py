#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import *

# Matrices
a=np.array([[998,1998],[-999,-1999]])
i=np.identity(2)

# Initial conditions
ye=np.array([[1],[0]])
yi=np.array([[1],[0]])

# Starting time and timestep (currently chosen within the stability region of
# the explicit method)
t=0
dt=0.1

while t<2:

    # Print solutions and exact solution
    ex1=2*exp(-t)-exp(-1000*t)
    ex2=-exp(-t)+exp(-1000*t)
    print(t,ex1,ex2,ye[0,0],ye[1,0],yi[0,0],yi[1,0])

    # Explicit step
    ye=ye+dt*np.dot(a,ye)

    # Implicit step
    yi=np.linalg.solve(i-dt*a,yi)

    t+=dt
