def array_print(array):
	n, m = len(array), len(array[0])
	for i in range(n):
		for j in range(m):
			print(f'{array[i][j]:3d}', end=' ')
		print()
		
		
def determinant(arr): # size of n x n
	n = len(arr)
	if n==0: return 0
	if n==1: return arr[0][0]
	ar = [[0 for i in range(n-1)] for j in range(n-1)]
	for i in range(1, n):
		for j in range(1, n):
			ar[i-1][j-1] = arr[i][j]
	det = arr[0][0]*determinant(ar)
	for k in range(1, n):
		for i in range(1, n): ar[i-1][k-1] = arr[i][k-1]
		if k%2==0: det += arr[0][k]*determinant(ar)
		else: det -= arr[0][k]*determinant(ar)
	return det


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


def array_rang(arr_list, rang):
	arr_s = [] # arrrays for next array_rang recursion
	ar = [[0 for i in range(rang-1)] for j in range(rang-1)]
	if len(arr_list) == 0: return 0
	for arr in arr_list:
		if determinant(arr) != 0: return rang
		for x in range(rang):
			for y in range(rang):
				for i in range(rang):
					for j in range(rang):
						if i<x and j<y:
							ar[i][j] = arr[i][j]
						elif i<x and j>y:
							ar[i][j-1] = arr[i][j]
						elif i>x and j<y:
							ar[i-1][j] = arr[i][j]
						elif i>x and j>y:
							ar[i-1][j-1] = arr[i][j]
				arr_s += [ar]
	return array_rang(arr_s, rang-1)
		# split take all the rang-1 arrays from arr and determinant(arr)


def arr_li(arr):
    n, m, li = len(arr), len(arr[0]), []
    s = min(n, m)
    ar = [[array[i][j] for i in range(s)] for j in range(s)]
    li += [ar]
    if m > n:
        pass # still to finish
    else:
        pass 
    return li

n, m = map(int, input("Введите размерность матрицы через пробел: ").split())
array = [[i for i in map(int, input().split())] for j in range(n)]
print("Исходная матрица: ")
array_print(array)
transp_array = transp(array, n, m)
print("Транспонированная матрица: ")
array_print(transp_array)
print("Произведение матриц: ")
mult_array = mult(array, transp_array)
array_print(mult_array)
print('Ранг матрицы =', array_rang(arr_li(array), min(len(array), len(array[0]))))
