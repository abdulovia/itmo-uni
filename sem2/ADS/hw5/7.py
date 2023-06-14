a = [10, 8, 2, 9, 4, 5, 3, 6, 1]
Min = min(a)
b = max(a) - Min
# Элемент находится в пределах отрезка [0, b]
vis = [0 for i in range(b+1)] # список посещенных элементов
for i in a:
    vis[i-Min] = 1
for i in range(b+1):
    if not vis[i]:
        print("Пропущенный элемент:", Min+i)
