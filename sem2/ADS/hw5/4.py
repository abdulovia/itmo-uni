def Count(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return Count(n-1) + Count(n-2) + Count(n-3)
    


n = int(input("Количество ступенек на лестнице: "))
x = Count(n)
print("Количество вариантов перемещения по лестнице:", x)