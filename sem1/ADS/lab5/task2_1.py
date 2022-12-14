'''
Дано дерево, необходимо найти его диаметр. Корень дерева – вершина 1.

В первой строке два числа: 1)количество вершин в дереве 2)количество ребер
Затем следует m пар чисел – ребра дерева.

Вывести диаметр дерева

Пример ввода:
3 2
1 2
1 3
Вывод:
2
'''
def dfs(v, p=-1, c=0):
    global maxlen1, maxlen2
    for u in adj[v]:
        if u != p:
            dfs(u, v, c+1)
    if len(adj[v])==1:
        if c >= maxlen1:
            maxlen2, maxlen1 = max(maxlen1, maxlen2), c
        elif c > maxlen2:
            maxlen2 = c


n, m = map(int, input().split())
adj = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a], adj[b] = adj[a]+[b], adj[b]+[a]
maxlen1, maxlen2 = 0, 0
dfs(1)
print(maxlen1+maxlen2)
