from random import randint

n = 9 # длина массива
# a = [randint(0, 100) for i in range(n)]
a = [1, 0, 1, 3, 4, 6, 7, 8, 9]
print("Последовательность: ")
print(*a)

s = sum(a)
dp = [0 for i in range(n+1)] # абсолютная разница между сумами
dp[0] = s
for i in range(1, n+1):
    s -= 2*a[i-1]
    dp[i] = abs(s)
print(*dp)

value = min(dp)
ix = dp.index(value)
print("Минимальная разница: ", value)
print("Списки: ", a[:ix], a[ix:])

