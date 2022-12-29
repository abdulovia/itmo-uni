def circle(r):
    return 3.14*r**2


def triangle(a, b, c):
    p = (a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**0.5


def rectangle(a, b):
    return a*b


t = ""
while t != 'Q':
    t = input('Площадь чего вы хотите вычислить?\n (1) Круга\n (2) Прямоугольника\n (3) Треугольника\n Введите 1/2/3/Q: ')
    if t=='1':
        try:
            r = float(input('Введите радиус круга: '))
        except Exception:
            print('Ошибка ввода радиуса!')
            continue
        if r < 0:
            print('Радиус не отрицателен!')
            continue
        print(circle(r))
    elif t=='2':
        try:
            a, b = map(float, input('Введите стороны прямоугольника через пробел: ').split())
        except Exception:
            print('Ошибка ввода сторон!')
            continue
        if a < 0 or b < 0:
            print('Стороны не отрицательны')
            continue
        print(rectangle(a, b))
    elif t=='3':
        try:
            a, b, c = map(float, input('Введите стороны треугольника через пробел: ').split())
        except Exception:
            print('Ошибка ввода сторон!')
            continue
        if a < 0 or b < 0 or c < 0 or a + b < c or a + c < b or b + c < a:
            print('Треугольника не существует')
            continue
        print(triangle(a, b, c))
    elif t!='Q':
        print('Ввод неверный!')