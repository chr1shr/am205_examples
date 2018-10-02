#!/usr/bin/python
from math import *

# Function to integrate
def f(x):
    return sin(x)

# Trapezoidal rule
def trap(f,a,b,n):

    # Step size
    h=(b-a)/float(n)

    # Trapezoidal formula
    fi=0.5*(f(a)+f(b))
    for i in range(1,n):
        fi+=f(a+i*h)

    # Return scaled answer
    return fi*h

# Simpson's rule
def simp(f,a,b,n):

    # Step size
    h=(b-a)/float(n)

    # Simpson's formula
    fi=f(a)+f(b)
    for i in range(1,n):
        fi+=4*f(a+(i-0.5)*h)+2*f(a+i*h)
    fi+=4*f(b-0.5*h)

    # Return scaled answer
    return fi*h/6.0

# Exact answer
ex=cos(1)-cos(5)

# Integrate with grids of different sizes. The errors for the trapezoidal rule
# decay like O(h^2), matching the error bound derivation presented in the
# lecture. The errors for Simpson's rule decay like O(h^4), which is actually
# better than the expected O(h^3) based on the derivation in the lecture. It
# turns out the the h^3 error terms cancel, leading to better performance,
# which can be proved with a more careful analysis. Note however that there is
# nothing wrong with the O(h^3) bound derived in the lecture - all it gives is
# an upper bound, which is still true.
j=1
while j<=65536:
    print j,4./float(j),trap(f,1,5,j)-ex,simp(f,1,5,j)-ex
    j*=2
