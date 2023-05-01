import numpy as np
import time


def split_to_2x2_blocks(matrix):
    m = len(matrix)
    c11, c12, c21, c22 = [[matrix[i][j] for i in range(m//2)] for j in range(m//2)], [[matrix[i][j] for i in range(m//2)] for j in range(
        m//2, m)], [[matrix[i][j] for i in range(m//2, m)] for j in range(m//2)], [[matrix[i][j] for i in range(m//2, m)] for j in range(m//2, m)]
    return np.array([[c11, c12], [c21, c22]])


def strassen(X, Y):
    if len(X) == 2:
        return np.matmul(np.array(X), np.array(Y))
    A, B = split_to_2x2_blocks(X), split_to_2x2_blocks(Y)
    S1 = B[0][1] - B[1][1]
    S2 = A[0][0] + A[0][1]
    S3 = A[1][0] + A[1][1]
    S4 = B[1][0] - B[0][0]
    S5 = A[0][0] + A[1][1]
    S6 = B[0][0] + B[1][1]
    S7 = A[0][1] - A[1][1]
    S8 = B[1][0] + B[1][1]
    S9 = A[0][0] - A[1][0]
    S10 = B[0][0] + B[0][1]
    P1 = strassen(A[0][0], S1)
    P2 = strassen(S2, B[1][1])
    P3 = strassen(S3, B[0][0])
    P4 = strassen(A[1][1], S4)
    P5 = strassen(S5, S6)
    P6 = strassen(S7, S8)
    P7 = strassen(S9, S10)
    return np.array([[P5 + P4 - P2 + P6, P1 + P2],
                     [P3 + P4, P5 + P1 - P3 - P7]])


def standardMult(A, B):
    return np.matmul(A, B)


def solve():
    k = 2
    A, B, Z = map(np.array, [
        [
            [1*i, 2*i]*k,
            [3*i, 4*i]*k,
        ]*k for i in range(1, 4)
    ])
    # print(A)
    # print(B)

    start = time.time()
    print(standardMult(A, B))
    end = time.time()
    print(f'время стандартного умножения матриц {((end-start)*1000):.3f} ms')

    start = time.time()
    strassen(A, B)
    end = time.time()
    print(f'время алгоритма Штрассена {((end-start)*1000):.3f} ms')


if __name__ == '__main__':
    solve()
