a = [0, 1]
for i in range(2, 500):
    x = a[i-1]+a[i-2]
    a += [x]
a = [str(i) for i in a]
s = "".join(a)