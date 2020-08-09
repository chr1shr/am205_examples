# Harvard Applied Math 205: Code Examples
## Unit 0: Overview of Scientific Computing

###### acc\_test.py
This program tests the value of machine epsilon, by comparing how small a value
of h is needed before 1+h evaluates to the same as 1.

###### acc\_test.cc
This is a version of **acc_test.py** written in C++. With the GNU C++
compiler, the program can be compiled with
```Shell
g++ -o acc_test acc_test.cc
```
and then run with
```Shell
./acc_test
```
It finds the same value of h as the Python version, emphasizing that what is
being tested is due to the hardware-level implementation of floating point
arithmetic, as opposed to being due to the specific programming language.

###### paranoia.c
The lectures also discussed paranoia.c, originally written by Prof. William
Kahan (UC Berkeley), available here:

http://www.netlib.org/paranoia/paranoia.c

This C program performs a number of tests to ensure that the computer's
arithmetic system does not have any errors. 
