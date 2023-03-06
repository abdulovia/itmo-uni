M = 29 # алфавит – латинские буквы

def hash(s):
    hsh = ''
    for i in s:
        hsh += str((ord(i)-ord('a')) % M)
    return int(hsh)

def main():
    s = input('Введите строку: ')
    print(f'Результат хэширования: {hash(s)}')
main()
