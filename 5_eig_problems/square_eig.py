#!/usr/bin/python
import scipy.sparse as sp
import scipy.sparse.linalg as spl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys

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
D2=sp.diags([cen,hor,hor,ver,ver],[0,1,-1,nn,-nn])

# Calculate eigenvalues and eigenvectors
vals,vecs=spl.eigs(D2,k=8,which='SM')

print(vals)

# Assemble an eigenvector in a grid
uu=np.zeros((n,n))
for i in range(nn):
    for j in range(nn):
        uu[i+1,j+1]=vecs[i+nn*j,0]

# Plot the eigenvector
xa=np.linspace(a,b,n)
mgx,mgy=np.meshgrid(xa,xa);
fig=plt.figure()
ax=fig.gca(projection='3d')
surf=ax.plot_surface(mgx,mgy,uu,rstride=1,cstride=1,linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
