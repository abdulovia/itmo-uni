n = int(input())
a = []
for i in range(n):
    h, k = map(int, input().split())
    a += [[k, h]]
a.sort()
print(a)
for i in range(n):
    c = a[i][0]
    j = 0
    while c != 0:
        if a[j][1] >= a[i][1] and j != i:
            c -= 1
        j += 1
    while a[j][1] < a[i][1] and a[j][0] == a[i][0]:
        j += 1
    if i == j: continue
    elif i > j:
        x = a.pop(i)
        a.insert(j, x)
    else:
        x = a.pop(i)
        a.insert(j-1, x)
    print(a)
    # print(a)
b = [[i[1], i[0]] for i in a]
print(b)

''' Test 1
6
7 0
4 4
7 1
5 0
6 1
5 2
'''
''' Test 2
10
11 2
17 0
9 6
9 7
15 1
12 0
11 5
10 6
10 0
11 1
'''
''' Test 3
5
4 1
7 0
5 2
6 0
8 0
'''