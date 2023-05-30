def checkIndexes(i, j, n, m):
    return i < n and j < m # не вышли за пределы матрицы

def getInd(a, x):
    '''
    Метод поиска элемента в матрице MxN,
    в кoтopoй кaждaя стpoкa и стoлбeц oтсopтиpoвaны
    пo вoзpaстaнию
    
    Принимает на вход матрицу a и искомый элемент x
    Возвращает два индекса i, j – строка и столбец,
    в которой находится элемент x 
    '''
    n, m = len(a), len(a[0])
    # реализуем алгоритм поиска в ширину
    queue = [(0, 0)] # начинаем поиск с верхнего левого элемента, заносим его в очередь
    vis = [[False for i in range(m)] for j in range(n)]
    while queue:
        el = queue.pop(0)
        i, j = el[0], el[1]
        if not vis[i][j]:
            vis[i][j] = True
        else:
            continue
        if a[i][j] == x: # элемент найден
            return i, j
        if checkIndexes(i+1, j+1, n, m) and a[i+1][j+1] <= x:
            queue.append((i+1, j+1))
        if checkIndexes(i+1, j, n, m) and a[i+1][j] <= x:
            queue.append((i+1, j))
        if checkIndexes(i, j+1, n, m) and a[i][j+1] <= x:
            queue.append((i, j+1))
    return -1, -1 # элемент не был найден

a = [
    [1, 2, 3],
    [3, 4, 4],
    [3, 4, 5],
    [4, 11, 12],
]
x = int(input("Введите искомый элемент: "))
i, j = getInd(a, x)
if i != -1:
    print('Указанный элемент находится на (', i, ', ', j, ')', sep='')
else:
    print('Данного элемента нет в матрице')