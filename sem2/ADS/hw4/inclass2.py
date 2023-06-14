# from random import randint

# a = [randint(0, 100) for i in range(9)]
# a = [17, 19, 22, 57, 70, 86, 99, 104, 124, 125, 130, 134, 153, 159, 186]
# a = [1, 228, 1488, 1487, 227, 1]
a = [1, 1, 1, 1, 1, 1, 100]
n = len(a)
print("Последовательность: ")
print(*a)

s = sum(a)

dp = [s for i in range(n+1)] # абсолютная разница между сумами двух массивов
p = [-1 for i in range(n+1)] # массив для восстановления ответа
for i in range(n): # по элементам массива
    m, t = s, -1
    for j in range(i+1): # по посчитанным разницам между сумами
        if abs(dp[j]-2*a[i]) <= m:
            m = abs(dp[j]-2*a[i])
            t = j
    dp[i+1] = m
    p[i+1] = t
print(*dp)

value = min(dp)
ix = dp.index(value)
print("Минимальная разница: ", value)
# Восстановление ответа
print("Массив A1: ")
vis = [False for i in range(n)]
while p[ix] != -1:
    print(a[ix-1], end=" ")
    vis[ix-1] = True
    ix = p[ix]
print()
print("Массив A2: ")
for i in range(n):
    if not vis[i]:
        print(a[i], end=" ")
print()
# print("Списки: ", a[:ix], a[ix:])

# 4, 2, 3, 2, 3
