# print(eval(input()))
s = input()
for i in '+-*/':
    if s.find(i)!=-1:
        a, b = map(float, s.split(i))
        if i=='+': print(a+b)
        if i=='-': print(a-b)
        if i=='*': print(a*b)
        if i=='/': print(a/b)