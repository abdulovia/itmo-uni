import numpy as np
print('Введите матрицу 3 x 3: ')
N = 3
array = [[i for i in map(int, input().split())] for j in range(N)]
array = np.array(array)
print('матрица:\n', array)
print('транспонированная матрица:\n', array.T)
print('умножение матриц:\n', array.dot(array.T))
print('ранг матрицы =', np.linalg.matrix_rank(array))

''' TEST
1 2 3    
4 5 6
7 8 9
'''