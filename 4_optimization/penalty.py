#!/usr/bin/python3
import numpy as np

# Objective function, gradient, and Hessian
def f(x,y): return x+y
def grad_f(x,y): return np.array([1.,1.])
def hess_f(x,y): return np.zeros((2,2))

# Constraint function, gradient, and Hessian
def g(x,y): return 2*x*x+y*y-5
def grad_g(x,y): return np.array([4*x,2*y])
def hess_g(x,y): return np.array([[4.,0.],[0.,2.]])

# Function with constraint as penalty term
def phi(x,y,rho):
    g0=g(x,y)
    return f(x,y)+0.5*rho*g0*g0

# Gradient of penalty function
def grad_phi(x,y,rho):
    return grad_f(x,y)+rho*g(x,y)*grad_g(x,y)

# Hessian of penalty function
def hess_phi(x,y,rho):
    gg=grad_g(x,y)
    return hess_f(x,y)+rho*(g(x,y)*hess_g(x,y)+np.outer(gg,gg))

# Find stationary point of phi function
def solve(z,rho):
    s=1e10
    sumhc=0;n=0

    # Do Newton steps until size falls below tolerance
    while np.linalg.norm(s)>1e-14:

        # Compute condition number of Hessian to store its average value
        hphi=hess_phi(z[0],z[1],rho)
        sumhc+=np.linalg.cond(hphi);n+=1

        # Perform Newton step
        s=np.linalg.solve(hphi,-grad_phi(z[0],z[1],rho))
        z+=s
    return (z,sumhc/n,n)

# Loop over a range of values of rho
rho=1
z=np.array([-1.,-1.])
while rho<1e13:

    # Solve with the given rho. Print the solution, the average condition
    # number of the Hessian, and the number of Newton steps.
    (z,avghc,n)=solve(z,rho)
    print(rho,z[0],z[1],avghc,n)

    rho*=10
