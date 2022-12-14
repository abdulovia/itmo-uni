matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
n, m = len(matrix), len(matrix[0])
moves = [[-1, 0], [1, 0], [0, -1], [0, 1]] # возможные ходы
vis = [[False for i in range(m)] for j in range(n)] # посещенные клетки
queue = [[i, 0] for i in range(n) if matrix[i][0]==0] 
p = [[[-1, -1] for i in range(m)] for j in range(n)] # список родительских клеток
vi, vj = -1, -1
while len(queue) != 0:
    a, b = queue.pop(0)
    vis[a][b] = True
    if b == m-1: # нашел выход
        vi, vj = a, b
        break
    for move in moves:
        i, j = a+move[0], b+move[1]
        if i < 0 or i > n or j < 0 or j > m or \
            matrix[i][j] == 1 or vis[i][j]: continue
        p[i][j] = [a, b] 
        queue += [[i, j]]
pp = [[[-1, -1] for i in range(m)] for j in range(n)]
while p[vi][vj] != [-1, -1]:
    pp[vi][vj] = p[vi][vj]
    vi, vj = p[vi][vj][0], p[vi][vj][1]
pp[vi][vj] = [0, 0]
for i in range(n):
    for j in range(m):
        if pp[i][j] == [-1, -1]: print('·', end=' ')
        else: print(0, end=' ')
    print()
