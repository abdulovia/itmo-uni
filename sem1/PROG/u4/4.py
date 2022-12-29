s = input()
t = ''
rus = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
eng = 'a b v g d e yo zh z i j k l m n o p r s t u f h z ch sh sha _ i _ ae yu ya'.split()
for i in s:
    if i.lower() not in rus: # Если это не буква
        t += i
        continue
    ix = rus.index(i.lower())
    if eng[ix] != '_':
        if i.lower() == i:
            t += eng[ix]
        else:
            t += eng[ix].upper()
print(t)