#!/usr/bin/python
from time import clock,time
import numpy as np
import scipy.linalg

# Loop over a variety of matrix sizes
for m in range(10,1600,10):

    # Construct a symmetric positive-definite (SPD) matrix
    # by multiplying a random matrix by its transpose
    a=np.random.random((m,m))
    b=np.dot(a,a.T)

    # Measure the clock
    e=clock()
    n=0
    f=e

    # Do as many Cholesky factorizations as possible within a 0.2 second
    # interval
    while f-e<0.2:
        n+=1
        l=scipy.linalg.cholesky(b)
        f=clock()

    # Print the average time to do a Cholesky factorization
    print m,n,(f-e)/n
