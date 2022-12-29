def counter(s, k): # считалочка для n человек в кругу, каждый k выходит
    n = len(s)
    a = [i for i in range(1, n+1)]
    i = 0
    while len(a) != 1:
        i = (i+k-1)%len(a)
        a.pop(i)
    return(s[a[0]-1])

print(counter(["Masha", "Vanya", "Kolya"], 2))
# 