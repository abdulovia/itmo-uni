INF = int(10 ** 9 + 7)  # const

n = int(input())
x = {}  # словарь (ключ: номинал, значение: количество)
print("Введите количество и номинал через пробел на отдельных строках:")
dp = [(INF, []) for i in range(n + 1)]
dp[0] = (0, [])
while True:
    cin = input()  # ввод
    if not cin: break  # ничего не ввели
    try:
        m, s = map(int, cin.split())
    except:
        break
    if m > 0 and s <= n: dp[s] = (1, [s])
    x[s] = m
# Применяется идея динамического программирования
for i in range(n + 1):
    for s in x.keys():
        if dp[i][0] != INF and i + s < n + 1 and dp[i][0] + 1 < dp[i + s][0]:
            if dp[i][1].count(s) < x[s]:
                t = dp[i][1].copy()
                t.append(s)
                dp[i + s] = (dp[i][0] + 1, t)
if dp[n] == (INF, []):
    print("сумма не достижима")
else:
    print(dp[n])
