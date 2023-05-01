from random import randint

n = 15 # длина массива
N = [randint(-100, 100) for i in range(n)]
# N = [-1, 0, 1, 3, 4, 6, 7, 8, 9]
print("Последовательность: ")
print(*N)

dp = [0 for i in range(n)]
for i in range(n-1):
    if N[i] < N[i+1]:
        dp[i+1] = dp[i] + 1
length = max(dp) # длина максимальной непрерывной последовательности
r = dp.index(length) # последний индекс МНП
b = N[r-length:r+1] # МНП
print("Возрастающая подпоследовательность: ", *b)