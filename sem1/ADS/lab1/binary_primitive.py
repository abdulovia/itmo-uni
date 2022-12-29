a = [1, 4, 9, 3, 2, 0, -1, 3, 4, 11, 17]
a.sort()
elem = -1
while len(a) != 1:
    print(a)
    middle = (len(a)-1)//2
    if a[middle]<elem: a = a[middle+1:]
    else: a = a[:middle+1]
if a[0]==elem: print("Найден", elem)