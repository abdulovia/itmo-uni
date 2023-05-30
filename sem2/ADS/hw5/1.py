def aCheck(a):
    return a[0] == a[1] == a[2] and a[0] != '.'

def result(deck):
    a = ['.']*3 # последовательность из трех
    for i in range(3): # главная диагональ
        a[i] = deck[i][i]
    if aCheck(a):
        # print(0)
        return a[0]
    for i in range(3): # побочная диагональ
        a[i] = deck[i][2-i]
    if aCheck(a):
        # print(1)
        return a[0]
    for i in range(3): # по горизонтали
        for j in range(3):
            a[j] = deck[i][j]
        if aCheck(a):
            # print(2)
            return a[0]
    for i in range(3): # по вертикали
        for j in range(3):
            a[j] = deck[j][i]
        if aCheck(a):
            # print(3)
            return a[0]
    return False
    
# o - нолик, x – крестик, . – пустое поле
deck = [[i for i in input().split()] for j in range(3)] # вводим расклад доски 
res = result(deck)
if res:
    print("The Winner is " + res)
else:
    print("It's a Draw!")
'''
x x o
. . x
o o x

x x o
o x o
o x .

o x x
x o x
o x o

x x o
o o x
x o x

. o o
o x x
x x o
'''