def correct(a, b, f):
    '''
    проверка корректности введенных позиций и выбранной фигуры
    возвращает True / False
    '''
    flag = True
    flag &= '1' <= f <= '6'
    mas = [] # все возможные позиции на доске
    for i in range(8):
        for j in range(8):
            c1, c2 = chr(ord('A')+i), chr(ord('1')+j)
            st = c1+c2
            mas += [st]
    flag &= a in mas
    flag &= b in mas
    return flag
    

def get_moves(f):
    '''
    возвращает список всех возможных ходов выбранной фигуры
    ''' 
    _moves = []
    if f == 1: # пешка
        _moves += [[0, 1], [0, -1]] # если цвет пешки не имеет значения
    elif f == 2: # ладья
        for i in range(1, 8):
            _moves += [[i, 0], [-i, 0], [0, i], [0, -i]]
    elif f == 3: # конь
        _moves += [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]
    elif f == 4: # слон
        for i in range(1, 8):
            _moves += [[i, i], [-i, i], [i, -i], [-i, -i]]
    elif f == 5: # король
        _moves += [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    elif f == 6: # ферзь
        for i in range(1, 8):
            _moves += [[i, 0], [-i, 0], [0, i], [0, -i]] # ходы ладьи
            _moves += [[i, i], [-i, i], [i, -i], [-i, -i]] # ходы слона
    return _moves
    
    
A = input('Введите начальное положение [A-H][1-8]: ')
B = input('Введите конечное положение [A-H][1-8]: ')
f = {
    1: 'пешка',
    2: 'ладья',
    3: 'конь',
    4: 'слон',
    5: 'король',
    6: 'ферзь',
}
for k, v in f.items():
    print(f'{k}: {v};', end=' ')
fig = input('Выберите фигуру [1-6]: ')
if correct(A, B, fig):
    s = [ord(A[0])-ord('A'), ord(A[1])-ord('1')] # start postion
    f = [ord(B[0])-ord('A'), ord(B[1])-ord('1')] # finish position
    moves = get_moves(int(fig))
    board = [[-1 for i in range(8)] for j in range(8)] # board with number of moves
    parents = [[[-1, -1] for i in range(8)] for j in range(8)] # запоминание ходов
    board[s[0]][s[1]] = 0
    queue = [[s[0], s[1]]]
    while queue:
        p = queue.pop(0)
        for i in moves:
            x, y = i[0]+p[0], i[1]+p[1]
            if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == -1:
                board[x][y] = board[p[0]][p[1]]+1
                parents[x][y] = p
                queue.append([x, y])
    if board[f[0]][f[1]] == -1: # позиция недостижима шахматной фигурой
        print('Из точки A не возможно попасть в точку B')
    else:
        print(f'Искомое количество ходов: {board[f[0]][f[1]]}')
        ans, it = [], f
        while parents[it[0]][it[1]] != [-1, -1]:
            ans.append(it)
            x, y = it[0], it[1]
            it = parents[x][y]
        print('Этими ходами являются: ')
        for it in ans[::-1]:
            print(chr(it[0]+ord('A'))+chr(it[1]+ord('1')), end=' ')
        print()
else:
    print('Одно или несколько введенных значений не соответсвуют требуемым!')