#!/usr/bin/python
from time import clock,time
import numpy as np
import scipy.linalg

# Get the current time() (a measure of "wall clock time", the physical passage of
# time as you would observe by looking at a wall clock)
t0=time()

# Get the current clock() (a measure of the time that this program has actually
# spent on the processor)
c0=clock()

# Carry out a large, arbitrary calculation
k=0
for i in range(1000):
	for j in range(1000):
		k+=i+j

# Print the elapsed time, using both the time() routine and the clock() routine
ttotal=time()-t0
ctotal=clock()-c0
print "time routine:",ttotal
print "clock routine:",ctotal
print "clock/time ratio:",ctotal/ttotal
