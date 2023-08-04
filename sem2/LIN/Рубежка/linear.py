import numpy as np

a = np.array([[[-7, 5, -4], [-5, 0, 1], [-2, 5, -4]],
              [[-1, 1, -3], [-5, -7, -2], [5, 2, -4]],
              [[1, -4, -8], [-2, -2, 6], [-2, 1, -5]]])
# print(A)
x = np.zeros((3, 3, 3))

c = np.array([[9, -7, -4], [20, -15, -8], [-23, 17, 9]])
d = np.array([[1, -5, -4], [4, -11, -8], [-5, 8, 5]])

for i in range(3):
    for k in range(3):
        for l in range(3):
            for j in range(3):
                for p in range(3):
                    for n in range(3):
                        x[l][i][k] += a[n][j][p] * c[n][l] * d[i][j] * d[k][p]
                
print(x)