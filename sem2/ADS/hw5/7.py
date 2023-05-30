a = [10, 8, 2, 9, 4, 5, 3, 6, 1]
Min = min(a)
Max = max(a) - Min
# Элемент находится в пределах отрезка [0, Max]
vis = [0 for i in range(Max+1)] # список посещенных элементов
for i in a:
    vis[i-Min] = 1
for i in range(Max+1):
    if not vis[i]:
        print("Пропущенный элемент:", i+Min)
