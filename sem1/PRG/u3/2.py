n = int(input())
for i in range(2, n+1):
    F = True
    for d in range(2, int(i**0.5)+1):
        if i%d==0:
            F = False
            break
    if F:
        print(i, end=' ')
print()