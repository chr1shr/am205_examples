#!/usr/bin/python
from time import clock,time
import numpy as np
import scipy.linalg

# Loop over a variety of matrix sizes
for m in range(10,1600,10):

    # Construct a random matrix to apply the LU factorization to
    a=np.random.random((m,m))
    
    # Measure the clock
    e=clock()
    n=0
    f=e

    # Do as many LU factorization as possible within a 0.2 second interval
    while f-e<0.2:
        n+=1
        (p,l,u)=scipy.linalg.lu(a)
        f=clock()

    # Print the average time to do an LU factorizations
    print m,n,(f-e)/n
