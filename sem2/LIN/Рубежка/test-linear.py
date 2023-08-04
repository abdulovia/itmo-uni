import numpy as np

A2 = np.zeros((3, 3, 3, 3))
for i in range(1, 4):
    for j in range(1, 4):
        for l in range(1, 4):
            for k in range(1, 4):
                A2[l-1][k-1][i-1][j-1] = -3*l + 2*k - 2*i + 3*j
                
# print(A2)
C2 = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        for k in range(3):
            C2[i][j] += A2[k][k][i][j]
# print(C2)

a = np.array([[1, 0], [0, 6]])
b = np.array([[-2], [5]])
c = np.array([[5, 2]])
d = np.array([[-4]])
e = np.array([[-4, 3], [4, 5]])
f1, f2 = np.kron(b, c), np.kron(d, e)
# print(f2)
f3 = f1 + f2
# print(f3)
f4 = -3*np.kron(a, f3)
print(f4)

A = np.array([[-5, 4, 1], [2, -4, 1], [-3, 4, 1]])
x = np.zeros((3, 3))

c = np.array([[1, 3, -2], [-4, -3, 3], [8, 8, -7]])
d = np.array([[-3, 5, 3], [-4, 9, 5], [-8, 16, 9]])

for i in range(3):
    for k in range(3):
        for j in range(3):
            for l in range(3):
                x[i][k] += A[j][l] * c[l][k] * d[i][j]
                
print(x)