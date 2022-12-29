def roots(a, b, c):
    D = b**2-4*a*c
    if D < 0:
        return "нет корней"
    elif D == 0:
        return -b/2/a
    else:
        return [(-b+D**0.5)/2/a, (-b-D**0.5)/2/a]


while True:
    s = input()
    if s == 'Q': break
    try:
        a,b,c = map(int, s.split())
    except Exception:
        print('Ошибка ввода')
        continue
    print(roots(a,b,c))
    