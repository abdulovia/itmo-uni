# Правильная скобочная последовательность
tests = [
    '()', # OK
    '(())()', # OK
    '()()', # OK
    '((()))', # OK
    
    ')(', # W 1
    '())(()', # W 3
    '(', #  W 1
    '))))', # W 1
    '((())', # W 1
    '()()(((()', # W 5
    '((()))(()())(()(()', # W 13
    '((()'
]

def is_Correct(s):
    print(s)
    c, d = 0, 0 # '(' + 1 ')' -  1
    ans1, ans2 = True, 0
    for i in range(len(s)):
        if s[i] == '(': c, d = c+1, d+1
        else: c, d = c-1, d+1
        if c == 0:
            d = 0
        if c < 0:
            ans1, ans2 = False, i
            break
    if ans1 and c==0:
        print('Скобочная последовательность верна', end='\n\n')
    else:
        if ans1 == True: ans2 = len(s)-d
        print('Скобочная последовательность неверна. Номер первого символа, нарушающего правильность:', ans2+1, end='\n\n')
        

for test in tests:
    is_Correct(test)