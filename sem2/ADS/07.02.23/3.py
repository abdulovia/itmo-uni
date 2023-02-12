def guess():
    while True:
        try:
            x = int(input('Выберите колоду карты [1-4]: '))
        except:
            print("Введите число")
            continue
        if not(1 <= x <= 4):
            print('Такой колоды не существует, введите корректное значение!')
            continue
        
        try:
            y = int(input('Выберите номер карты [1-9]: '))
        except:
            print("Введите число")
            continue
        if not(1 <= y <= 9):
            print('Такого номера не существует, введите корректное значение!')
            continue
        
        return x, y

import random
d = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] # diamonds = бубны
random.shuffle(d)
h = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] # hearts = черви
random.shuffle(h)
c = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] # clubs = трефы
random.shuffle(c)
s = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] # spades = пики
random.shuffle(s)
print('\n', *d, '\n', *h, '\n', *c, '\n', *s, '\n')
deck = [d, h, c, s]

cards = 36
while cards != 0:
    x1, y1 = guess()
    print(f'Карта на позиции ({x1}, {y1}): {deck[x1-1][y1-1]}')
    x2, y2 = guess()
    if x1 == x2 and y1 == y2:
        print('Вы выбрали ту же карту, попробуйте заново!')
        continue
    print(f'Карта на позиции ({x2}, {y2}): {deck[x2-1][y2-1]}')
    if deck[x1-1][y1-1]==deck[x2-1][y2-1]:
        print("Вы угадали, карты совпадают!")
        deck[x1-1][y1-1]=deck[x2-1][y2-1]='*'
        cards -= 2
    else:
        print("К сожалению карты различаются, попробуйте еще раз!")
    for i in deck:
        print(*i)
print("Ура, вы нашли все пары!")
    