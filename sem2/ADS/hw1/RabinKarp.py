from fib import s

X = 10 # размер алфавита (фиксированный)
M = 2 # длина двузначного шаблона (фиксированная)
def hash(s):
    '''
    Функция возвращает hash (число) от произвольной строки
    :param s:
    :return H:
    '''
    H = 0
    for i in range(len(s)):
        c = ord(s[i])-ord('0') # значение от 0 до 9 – порядковый номер символа
        H += c*X**(M-i)
    return H


ans = [0]*100
for num in range(10, 100):
    ans[num] = 0
    n = str(num)
    h1 = hash(n)
    for j in range(1, len(s)):
        st = s[j-1]+s[j] # берем два символа строки
        h2 = hash(st)
        if h1 == h2 and n == st:
            ans[num] += 1
mx = max(ans)
for i in range(len(ans)):
    if ans[i] == mx:
        print(i)