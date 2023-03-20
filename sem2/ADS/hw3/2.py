INF = int(10 ** 9 + 7)  # const

n = int(input("Количество экспонатов: "))
print("Введите цену и вес каждого экспоната через пробел на отдельных строках:")
x = []
for i in range(n):
    c, w = map(int, input().split())
    x.append([c, w])
m, k = map(int, input("Число заходов и вместимость через пробел: ").split())  # число заходов и вместимость рюкзака
M, ans = m, 0
while m:
    dp = [(-1, []) for i in range(k + 1)]
    dp[0] = (0, [])
    for i in range(k + 1):
        for expo in x:
            c, w = expo[0], expo[1]
            if dp[i][0] != -1 and i + w < k + 1 and dp[i][0] + c > dp[i + w][0]:
                if dp[i][1].count(expo) < x.count(expo):
                    t = dp[i][1].copy()
                    t.append(expo)
                    dp[i + w] = (dp[i][0] + c, t)
    print(f"{M - m + 1} заход:")
    mx = max(k[0] for k in dp)
    for i in dp:
        if i[0] == mx:
            print(i)
            for expo in i[1]:
                x.remove(expo)
            break
    ans += mx
    m -= 1
print("Цена награбленного: ", ans)

''' Тест 1
20

10 2
1 1
1 1
2 2
20 8
30 9
10 3
10 10
5 5
4 4
10 2
1 1
1 1
2 2
20 8
30 9
10 3
10 10
17 5
16 5

3 10
'''
