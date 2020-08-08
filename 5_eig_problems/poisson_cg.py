import numpy as np
import scipy.sparse as sp
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameter setup
a=0.0
b=1.0
n=41
h=(b-a)/(n-1)
de=1/(h*h)

# Generate the centered difference differentiation matrix for the Laplacian
nn=n-2
cen=np.ones(nn*nn)*(4*de)
hor=np.ones(nn*nn-1)*(-de)
ver=np.ones(nn*(nn-1))*(-de)
for i in range(nn-1):
    hor[(i+1)*nn-1]=0
A=sp.diags([cen,hor,hor,ver,ver],[0,1,-1,nn,-nn])

# Right hand side: a vector of ones
rhs=np.ones((nn*nn,1))

# Solve for U using the conjugate gradient method
TOL=1.e-4
x_k=np.zeros((nn*nn,1))
r_k=rhs
p_k=r_k

count=1
while True:
    alpha_k=np.dot(r_k.T,r_k)/np.dot(p_k.T,A*p_k)
    x_k=x_k+alpha_k[0,0]*p_k
    r_k_old=r_k
    r_k=r_k-alpha_k[0,0]*(A*p_k)

    rel_residual=np.linalg.norm(r_k)/np.linalg.norm(rhs)
    print("iteration=%d, relative residual=%g" % (count, rel_residual))

    if rel_residual < TOL:
        break

    beta_k=np.dot(r_k.T,r_k)/np.dot(r_k_old.T,r_k_old)

    p_k=r_k+beta_k[0,0]*p_k

    count+=1

# Print grid spacing and condition number. This may get very expensive for a
# big grid, since it uses a dense linear algebra routine to compute the
# condition number.
print("h=%g, condition number=%g\n" % (h,np.linalg.cond(A.todense())))

# Assemble solution in a grid
uu=np.zeros((n,n))
for i in range(nn):
    for j in range(nn):
        uu[i+1,j+1]=x_k[i+nn*j,0]

# Plot the solution
xa=np.linspace(a,b,n)
mgx,mgy=np.meshgrid(xa,xa);
fig=plt.figure()
ax=fig.gca(projection='3d')
surf=ax.plot_surface(mgx,mgy,uu,rstride=1,cstride=1,linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
