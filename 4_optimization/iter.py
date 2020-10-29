#!/usr/bin/python3
from math import *

def f(x):
    return exp(x)-x-2

xa=1.15
xb=1.15

for i in range(20):
    xa=log(xa+2)
    #xb=exp(xb)-2

    print(xa,f(xa))#,xb,f(xb))
