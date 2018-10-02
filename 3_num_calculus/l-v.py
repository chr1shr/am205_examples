#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import *

# Constants in model
alpha=1.5
beta=0.5
gamma=0.4
delta=0.4

# Function
def deriv(x,t):
    return np.array([alpha*x[0]-beta*x[0]*x[1],-gamma*x[1]+delta*x[0]*x[1]])

# Solve ODE using the "odeint" library in SciPy
time=np.linspace(0,70,500)

# Initial conditions, set to the initial
xinit=np.array([10,5])
x=odeint(deriv,xinit,time)

for i in range(0,500):
    print time[i],x[i,0],x[i,1]

# Plot the solutions
plt.figure()
p0,=plt.plot(time,x[:,0])
p1,=plt.plot(time,x[:,1])
plt.legend([p0,p1],["B(t)","C(t)"])
plt.xlabel('t')
plt.ylabel('Population')
plt.show()
