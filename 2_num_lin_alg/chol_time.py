#!/usr/bin/python
from time import process_time,time
import numpy as np
import scipy.linalg

# Loop over a variety of matrix sizes
m=10
while m<4500:

    # Construct a symmetric positive-definite (SPD) matrix
    # by multiplying a random matrix by its transpose
    a=np.random.random((m,m))
    b=np.dot(a,a.T)

    # Store the initial process time
    t=process_time()

    # Measure the wall clock time
    e=time()
    n=0
    f=e

    # Do as many Cholesky factorizations as possible within a 0.2 second
    # interval of wall clock time
    while f-e<0.2:
        n+=1
        l=scipy.linalg.cholesky(b)
        f=time()

    # Print the average wall clock time and process time to do a Cholesky
    # factorization
    print("%d %d %.5g %.5g"%(m,n,(f-e)/n,(process_time()-t)/n))

    # Increase m by a multiplicative factor
    m+=m//10
