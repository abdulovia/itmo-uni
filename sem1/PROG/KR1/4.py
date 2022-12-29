a = [i for i in map(float, input().split())]
for i in range(len(a)):
    if a[i] < 10:
        a[i] *= 1.135
    elif a[i] > 10:
        a[i] *= 0.642
a.sort()
f = open('out.txt', 'w')
for i in a:
    print(format(i, '.2f'), end=' ')
    print(format(i, '.2f'), end=' ', file=f)
f.close()
