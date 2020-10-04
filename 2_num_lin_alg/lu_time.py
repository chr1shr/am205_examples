#!/usr/bin/python
from time import process_time,time
import numpy as np
import scipy.linalg

# Loop over a variety of matrix sizes
m=10
while m<4500:

    # Construct a random matrix to apply the LU factorization to
    a=np.random.random((m,m))

    # Store the initial wall clock time
    t=process_time()

    # Measure the wall clock time
    e=time()
    n=0
    f=e

    # Do as many LU factorizations as possible within a 0.2 second interval of
    # wall clock time
    while f-e<0.2:
        n+=1
        (p,l,u)=scipy.linalg.lu(a)
        f=time()

    # Print the average wall clock time and process time to do an LU
    # factorization
    print("%d %d %.5g %.5g"%(m,n,(f-e)/n,(process_time()-t)/n))

    # Increase m by a multiplicative factor
    m+=m//10
