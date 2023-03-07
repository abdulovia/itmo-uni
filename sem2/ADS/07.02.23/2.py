peshki_pos = []
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
    flag &= a not in peshki_pos
    flag &= b not in peshki_pos
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
    

def get_board(p, b):
    second_board = [[-1 for i in range(8)] for j in range(8)]
    for j in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]:
        flag = False
        for i in range(1, 8):
            x, y = p[0]+j[0]*i, p[1]+j[1]*i
            if 0 <= x < 8 and 0 <= y < 8 and (b[x][y] == -2 or flag):
                second_board[x][y] = -2
                flag = True
    return second_board


num_of_pieces = 6
s1, s2 = "", ""
board0 = [[-1 for i in range(8)] for j in range(8)] # board with number of moves
while num_of_pieces > 0:
    A = input(f'Введите положение {6-num_of_pieces+1} пешки [A-H][1-8]: ')
    peshki_pos.append(A)
    s = [ord(A[0]) - ord('A'), ord(A[1]) - ord('1')]
    board0[s[0]][s[1]] = -2 # на данной позиции стоит пешка
    num_of_pieces -= 1
num_of_pieces = 2
while num_of_pieces > 0:
    board = [[-1 for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            if board0[i][j] == -2:
                board[i][j] = -2
    print(board)
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
        parents = [[[-1, -1] for i in range(8)] for j in range(8)] # запоминание ходов
        board[s[0]][s[1]] = 0
        queue = [[s[0], s[1]]]
        while queue:
            p = queue.pop(0)
            second_board = get_board(p, board)
            for i in moves:
                x, y = i[0]+p[0], i[1]+p[1]
                if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == -1 and second_board[x][y] != -2:
                    board[x][y] = board[p[0]][p[1]]+1
                    parents[x][y] = p
                    queue.append([x, y])
        if board[f[0]][f[1]] == -1 or board[f[0]][f[1]] == -2: # позиция недостижима шахматной фигурой
            print('Из точки A не возможно попасть в точку B')
        else:
            print(f'Искомое количество ходов: {board[f[0]][f[1]]}')
            ans, it = [], f
            while parents[it[0]][it[1]] != [-1, -1]:
                ans.append(it)
                x, y = it[0], it[1]
                it = parents[x][y]
            print('Этими ходами являются:', end=' ')
            for it in ans[::-1]:
                print(chr(it[0]+ord('A'))+chr(it[1]+ord('1')), end=' ')
                if num_of_pieces == 2:
                    s1 += chr(it[0]+ord('A'))+chr(it[1]+ord('1'))
                else:
                    s2 += chr(it[0] + ord('A')) + chr(it[1] + ord('1'))
            print()
        print(board)
        num_of_pieces -= 1
    else:
        print('Одно или несколько введенных значений не соответсвуют требуемым!')
print('Полученные строки: ')
print(s1)
print(s2)
for k in range(0, len(s1)-1, 2):
    pos = s1[k]+s1[k+1] # клетка
    flag = True
    i = 1
    while i < len(s2):
        j = i
        while j - i - 1 >= -2 and pos[j - i - 1] == s2[j]:  # j - i - 1 будет идти с конца шаблона и строки (справа налево)
            j -= 1
        if j - i - 1 == -3:
            print(f'Клетка (пересечение двух строк), в которой были обе фигуры: {pos}')
            flag = False
            break
        i += 2
    if not flag:
        break