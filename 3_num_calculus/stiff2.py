#!/usr/bin/python3
from scipy.integrate import ode
from math import exp

# Function
def f(t,y,arg1):
    return [998*y[0]+1998*y[1],-999*y[0]-1999*y[1]]

# Initial conditions
yinit=[1,0]

# Set up stiff integrator and parameters
r=ode(f).set_integrator('zvode',method='bdf')
r.set_initial_value(yinit,0).set_f_params(2.0).set_jac_params(2.0)
h=0.05

# Loop while the time is less than 2
while r.successful() and r.t<2:
    r.integrate(r.t+h)

    # Print solution and comparison with exact answer
    ex1=2*exp(-r.t)-exp(-1000*r.t)
    ex2=-exp(-r.t)+exp(-1000*r.t)
    print(r.t,float(r.y[0]),float(r.y[1]),ex1,ex2,float(r.y[0])-ex1,float(r.y[1])-ex2)
