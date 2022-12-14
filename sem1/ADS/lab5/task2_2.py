'''
Дано дерево, необходимо найти эксцентриситет вершины.

В первой строке три числа: 1)количество вершин в дереве 2)количество ребер 3)вершина
Затем следует m пар чисел – ребра дерева.

Вывести эксцентриситет введенной вершины

Пример ввода:
3 2 3
1 2
1 3
Вывод:
2
'''
n, m, s = map(int, input().split())
adj = [[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    adj[a], adj[b] = adj[a]+[b], adj[b]+[a]
queue = [s]
vis = [False]*(n+1)
dist = [-1]*(n+1)
dist[s] = 0
while len(queue) != 0:
    v = queue.pop(0)
    vis[v] = True
    for u in adj[v]:
        if not vis[u]:
            dist[u] = dist[v]+1
            queue.append(u)
print(max(dist))