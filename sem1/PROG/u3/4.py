x, y = map(float, input().split())
if x > 0:
    if y > 0:
        print('I четверть')
    elif y < 0:
        print('IV четверть')
    else: # y = 0
        print('ось абсцисс')
elif x < 0:
    if y > 0:
        print('II четверть')
    elif y < 0:
        print('III четверть')
elif x == 0:
    if y == 0:
        print('начало координат')
    else: # x = 0, y != 0
        print('ось ординат')