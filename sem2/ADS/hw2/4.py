from random import uniform

def dehash(hs, c, m):
    res = ''
    for i in hs:
        n = int(i, 2)/m
        x = chr(int(n/c+31)+1)
        res += x
    return res

def hash(s, c, m):
    res = []
    for i in s:
        x = (ord(i)-31)*c
        res += [bin(int(m*x))[2:]]
    return res

c, m = uniform(0, 1), 97
s = input('Введите текст, который нужно хэшировать: ')
print(f'Константа: {c}, размер алфавита: {m}')
hash_t = hash(s, c, m)
hash_s = ''.join(hash_t)
print(f'Хэшированный текст (умножение): {hex(int(hash_s, 2))}')
deh_s = dehash(hash_t, c, m)
print(f'Исходный текст (умножение): {deh_s}')
print(f'Корректность дехеширования: {deh_s==s}')
