#!/usr/bin/python
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Calculate two splines
x=np.array([0,2,0,-4,0,6])
y=np.array([1,0,-3,0,5,0])
t=np.linspace(0,5,6)
f=interp1d(t,x)
g=interp1d(t,y)
f2=interp1d(t,x,kind='cubic')
g2=interp1d(t,y,kind='cubic')

# Use splines to plot a spiral
tnew=np.linspace(0,5,200)
plt.plot(x,y,'o',f(tnew),g(tnew),'-',f2(tnew),g2(tnew),'--')
plt.legend(['data','linear','cubic'],loc='best')
plt.show()
