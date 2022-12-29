s = input()
c = 0
for i in s:
    if i.isnumeric():
        c += int(i)
print(c)