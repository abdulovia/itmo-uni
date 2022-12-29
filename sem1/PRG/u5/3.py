def dif(s):
    difficulty = 0
    if len(s) != 0:
        difficulty += 1
    if len(s) >= 8:
        difficulty += 1
    f1, f2, f3 = 1, 1, 1
    for i in s:
        if i.isnumeric() and f1:
            difficulty += 1
            f1 = 0
        elif i.isalpha() and f2:
            difficulty += 1
            f2 = 0
        elif not i.isalpha() and not i.isnumeric() and f3:
            difficulty += 1
            f3 = 0
    return difficulty


while True:
    s = input()
    if s == 'Q': break
    print(dif(s))
