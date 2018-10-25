#!/usr/bin/python
from math import sqrt

def f(x1,x2):
    return (x1*x1+x2*x2-1,5*x1*x1+21*x2*x2-9)

(x1,x2)=(0.,0.)

# Print zeroth step
(f1,f2)=f(x1,x2)
print 0,x1,x2,f1,f2

for i in range(1,31):

    # Do vector iteration
    (x1,x2)=(sqrt(1-x2*x2),sqrt((9.-5.*x1*x1)/21.))

    # Print ith step
    (f1,f2)=f(x1,x2)
    print i,x1,x2,f1,f2
