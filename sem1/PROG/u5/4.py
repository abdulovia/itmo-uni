def dcrypt(s, key):
    msg = ''
    for i in range(len(s)):
        msg += chr(ord(s[i]) ^ ord(key[i%len(key)]))
    return msg

while True:
    s = input('Введите строку для зашифровки: ')
    if s == 'Q': break
    key = input('Введите ключ шифрования: ')
    msg = dcrypt(s, key)
    print('Зашифрованная строка: ', msg)
    msg = dcrypt(msg, key)
    print('Расшифрованная строка: ', msg)