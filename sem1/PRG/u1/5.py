num = int(input('Введите число: '))
d, h, m, s = num//3600//24, num//3600%24, num//60%60, num%60
print(f'{d}:{h}:{m}:{s}')
