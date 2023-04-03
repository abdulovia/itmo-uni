def text(inp):
    s = ''
    for i in range(len(inp)):
        k = bin(ord(inp[i])) #получаем двоичный код из исходного текста
        s += k[2:]
        #print(s)
    return s

def main():
    codec = [
        '100000100110000010001110110110111',
        '100011110110111000110111101000001',
        '101110100000110111000110011010111',
        '110000001010000010100000110101011'
    ]

    s = input('Введите текст, который нужно закодировать ')
    x = int(input('Выберите кодировку:\n 1 - CRC-32 IEE-802.3,\n 2 - CRC-32C,\n 3 - CRC-32K,\n 4 - CRC-32Q\n '))
    a = text(s) + '0'*32
    
    if 4 >= x >= 1:
        c = ''
        b = int(codec[x-1],2)
        while len(a) + len(c) >= 33:
            while len(c) < 33:
                c += a[0]
                a = a[1:]
            xor = int(c,2) ^ b
            c = bin(xor)[2:]
        return f"Ответ: {c + a}"
    else:
        return 'Проверьте корректность ввода'
    
if __name__ == "__main__":
    print(main())
