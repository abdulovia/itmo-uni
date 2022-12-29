s = input()
x = ''
for i in s:
    if i.lower() == i:
        x += i.upper()
    else:
        x += i.lower()
print(x)