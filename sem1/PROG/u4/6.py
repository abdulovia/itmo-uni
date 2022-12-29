# Список
s = []
while True:
    a = input()
    if a=='Q':
        break
    a = float(a)
    s.append(a)
print(len(s))
if len(s) != 0:
    print(sum(s)/len(s))
print(sum(s))
print(min(s), s.index(min(s)))
print(max(s), s.index(max(s)))
mt = 1
if s.index(min(s)) > s.index(max(s)):
    for i in range(s.index(max(s))+1, s.index(min(s))):
        mt *= s[i]
else:
    for i in range(s.index(min(s))+1, s.index(max(s))):
        mt *= s[i]
print(mt)