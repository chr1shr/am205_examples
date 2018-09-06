#!/usr/bin/python

# This program tests the accuracy of the Python floating point numbers, by
# testing to see if 1+h=1 for different values of h 
h=1

# Loop until h becomes too small
while h>1e-20:
    
    # Check if 1+h==1 in floating point arithmetic
    if 1+h==1:
        print h,"  1+h=1"
    else:
        print h,"  1+h!=1"
    
    h*=0.1
