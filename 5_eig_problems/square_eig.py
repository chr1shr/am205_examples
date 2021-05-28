#!/usr/bin/python3
import scipy.sparse as sp
import scipy.sparse.linalg as spl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Grid setup
m=40
mm=m*m
h=1/(m+1)

# Generate the centered difference differentiation matrix for the Laplacian
hfac=1/(h*h)
cen=np.ones(mm)*(4*hfac)
hor=np.ones(mm-1)*(-hfac)
ver=np.ones(m*(m-1))*(-hfac)
for i in range(m-1):
    hor[(i+1)*m-1]=0
D2=sp.diags([cen,hor,hor,ver,ver],[0,1,-1,m,-m])

# Calculate eigenvalues and eigenvectors
vals,vecs=spl.eigs(D2,k=8,which='SM')
print("Eigenvalues:")
print(vals)

# Assemble an eigenvector in a grid
uu=np.zeros((m+2,m+2))
for i in range(m):
    for j in range(m):
        uu[i+1,j+1]=vecs[i+m*j,2].real

# Plot the eigenvector
xa=np.linspace(0,1,m+2)
mgx,mgy=np.meshgrid(xa,xa);
fig=plt.figure()
ax=Axes3D(fig,auto_add_to_figure=False)
fig.add_axes(ax)
ax.plot_surface(mgx,mgy,uu,rstride=1,cstride=1,linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
