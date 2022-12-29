def temp(data): # считает среднюю температуру
    return sum(data)/len(data)

def clear(data): # убирает все None из списка
    ans = []
    for i in data:
        if i != None:
            ans += [i]
    return ans


data = [3, None, 11, 12.4, -1, None, 8, 4, 6, 0]
data = clear(data)
print(data)
print("%.2f" % temp(data))