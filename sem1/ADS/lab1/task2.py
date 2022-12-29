n, m = 3, 3
def array_print(array):
	n, m = len(array), len(array[0])
	for i in range(n):
		for j in range(m):
			print(f'{array[i][j]:3d}', end=' ')
		print()


def transp(array, n, m):
	transp_array = [[0 for i in range(n)] for j in range(m)]
	for i in range(n):
		for j in range(m):
			transp_array[j][i] = array[i][j]
	return transp_array


def mult(arr1, arr2):
	h1, w1, h2, w2 = len(arr1), len(arr1[0]), len(arr2), len(arr2[0])
    mult_array = [[0 for i in range(w2)] for j in range(h1)]
    for i in range(h1):
		for j in range(w2):
			val = 0
			for k in range(min(w1, h2)):
				val += arr1[i][k]*arr2[k][j]
			mult_array[i][j] = val
	return mult_array


def array_rang(arr):
    minors2 = [[0 for i in range(n)] for j in range(n)] # все детерминанты миноров 2-го порядка
    rang = 0
    for x in range(n):
        for y in range(n):
            # alg dopolnenie dlya elementa arr[x][y]
            ar = [[0 for i in range(n-1)] for j in range(n-1)]
            for i in range(n):
                for j in range(n):
                    if i<x and j<y: ar[i][j] = arr[i][j]
                    elif i<x and j>y: ar[i][j-1] = arr[i][j]
                    elif i>x and j<y: ar[i-1][j] = arr[i][j]
                    elif i>x and j>y: ar[i-1][j-1] = arr[i][j]
            det = ar[0][0]*ar[1][1]-ar[0][1]*ar[1][0]
            if arr[x][y] != 0: rang=max(rang,1)
            if det != 0: rang=max(rang, 2)
            minors2[x][y] = det
    det3 = arr[0][0]*minors2[0][0]\
        -arr[0][1]*minors2[0][1]\
            +arr[0][2]*minors2[0][2]
    if det3 != 0: rang = max(rang, 3)
    return rang


print('Введите матрицу 3 x 3: ')
array = [[i for i in map(int, input().split())] for j in range(n)]
print("Исходная матрица: ")
array_print(array)
transp_array = transp(array, n, m)
print("Транспонированная матрица: ")
array_print(transp_array)
print("Произведение матриц: ")
mult_array = mult(array, transp_array)
array_print(mult_array)
print('Ранг матрицы =', array_rang(array))
