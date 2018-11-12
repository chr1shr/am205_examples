import numpy as np

A=np.matrix([[2.9766,0.3945,0.4198,1.1159],
     [0.3945,2.7328,-0.3097,0.1129],
     [0.4198,-0.3097,2.5675,0.6079],
     [1.1159,0.1129,0.6079,1.7231]])
max_iters=100

# Initialize A_k
A_k=A

# Initialize the matrix in which we store the product of our Q matrices
Q_prod=np.eye(4)

# Perform the QR algorithm
for i in range(max_iters):
    (Q_k,R_k)=np.linalg.qr(A_k)
    A_k=np.dot(R_k,Q_k)
    Q_prod=np.dot(Q_prod,Q_k)

# Print eigenvalues
print np.diag(A_k)

# Print eigenvectors
print Q_prod

print np.linalg.eig(A)
