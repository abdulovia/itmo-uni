from random import randint
n = randint(1, 100)
x = int(input())
c = 1
while x != n:
    if x < n:
        print('больше')
    else:
        print('меньше')
    x = int(input())
    c += 1
    if c>10: break
if c>10:
    print('Вы не угадали')
else:
    print(f'Вы угадали число {n}')
    print(c, '- количество ходов')