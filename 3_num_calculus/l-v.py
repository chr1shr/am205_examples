#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants in model
alpha1=1.2
beta1=0.4
alpha2=0.2
beta2=0.1

# Function that evaluates the RHS of the ODE. It has two components,
# representing the changes in prey and predator populations.
def f(y,t):
    return np.array([alpha1*y[0]-beta1*y[0]*y[1], \
                     -alpha2*y[1]+beta2*y[0]*y[1]])

# Specify the range of time values where the ODE should be solved at
time=np.linspace(0,70,500)

# Initial conditions, set to the initial populations of prey and predators
yinit=np.array([10,5])

# Solve ODE using the "odeint" library in SciPy
y=odeint(f,yinit,time)

# Print the solutions
#for i in range(0,500):
#    print(time[i],x[i,0],x[i,1])

# Plot the solutions
plt.figure()
p0,=plt.plot(time,y[:,0])
p1,=plt.plot(time,y[:,1])
plt.legend([p0,p1],["Prey","Predators"])
plt.xlabel('t')
plt.ylabel('Population')
plt.show()
