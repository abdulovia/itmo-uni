def array_inv(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    det = a11*a22*a33+a12*a23*a31+a21*a32*a13-a13*a22*a31-a11*a23*a32-a33*a12*a21
    if det==0:
        print("Обратной матрицы нету! Определитель равен 0!")
        return None
    arr_adj = [[a22*a33-a23*a32, -(a21*a33-a23*a31), a21*a32-a22*a31],
               [-(a12*a33-a13*a32), a11*a33-a13*a31, -(a11*a32-a12*a31)],
               [a12*a23-a13*a22, -(a11*a23-a13*a21), a11*a22-a12*a21]]
    arr_inv = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            arr_inv[i][j] = 1/det*arr_adj[i][j]
    return arr_inv


import numpy as np
import timeit
print("Введите матрицу A:\n")
A = [[i for i in map(int, input().split())]for j in range(3)]
start1 = timeit.default_timer()
arr_inv = array_inv(A[0][0],A[1][0],A[2][0],A[0][1],A[1][1],A[2][1],A[0][2],A[1][2],A[2][2])
end1 = timeit.default_timer()
start2 = timeit.default_timer()
arr_inv = np.linalg.inv(A)
end2 = timeit.default_timer()
print('Время работы моего кода: ', '{:.10f}'.format(((end1 - start1)*10**(-3))), 'секунд')
print('Время работы библиотеки numpy: ', '{:.10f}'.format(((end2 - start2)*10**(-3))), 'секунд')


'''
print()
for i in range(3):
    print(*arr_inv[i])
print()
print(np_arr_inv)
'''

''' TEST
1 2 1
1 1 4
2 3 6
'''
