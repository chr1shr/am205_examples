#!/usr/bin/python
import numpy as np

# Define the vector A
n=10
diag_vector=np.concatenate((np.linspace(0.,2.,n),np.array([2.5,3.])))
A=np.diag(diag_vector)

# Initialize Q, alpha and beta
iters=11
Q=np.zeros((n+2,iters+1))
alpha=np.zeros((iters))
beta=np.zeros((iters))

# Define a random initial vector
b=np.random.randn(n+2)
Q[:,0]=b/np.linalg.norm(b)

# The Lanczos iteration loop
for m in range(iters):
    v=np.dot(A,Q[:,m])
    alpha[m]=np.dot(Q[:,m],v)
    if m==0:
        v=v-alpha[m]*Q[:,m]
    else:
        v=v-beta[m-1]*Q[:,m-1]-alpha[m]*Q[:,m]
    beta[m]=np.linalg.norm(v)
    Q[:,m+1]=v/beta[m]

H_m=np.dot(np.dot(Q.T,A),Q)
[V,D]=np.linalg.eig(H_m)

# Save the characteristic polynomial
p=np.poly(H_m)
f=open("poly","w")
x=-0.5
while x<=3.5:
    f.write(str(x)+" "+str(np.polyval(p,x))+"\n")
    x+=0.01
f.close()

# Save the roots
f=open("roots","w")
for i in range(n+2):
    f.write(str(diag_vector[i])+" 0\n")
f.write("\n\n")
for i in range(iters+1):
    f.write(str(V[i])+" 0\n")
f.close()
