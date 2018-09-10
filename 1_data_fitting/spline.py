#!/usr/bin/python
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Construct splines for two sets of similar data points
x=np.array([0,2,0,-4,0,6])
x2=np.array([0,2.1,0,-4,0,6])
t=np.linspace(0,5,6)
f=interp1d(t,x,kind='cubic')
f2=interp1d(t,x2,kind='cubic')

# Plot the splines and data
tnew=np.linspace(0,5,200)
plt.plot(t,x,'o',tnew,f(tnew),'-',t,x2,'o',tnew,f2(tnew),'--')
plt.legend(['data','cubic','data2','cubic2'],loc='best')

# Optional plot of the difference
#plt.plot(tnew,f(tnew)-f2(tnew),'-')

plt.show()
