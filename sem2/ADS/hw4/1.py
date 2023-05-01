def backpack(n, items, m, k):
    # n - экспонатов нужно украсть
    # m - количество заходов, которое можно сделать
    # k - количество килограмм, которое можно унести за раз
    # items - кортеж, который хранит информацию об экспонатах(вес, цена)

    result = [ [0]* (n+1) for i in range(m+1) ] # таблица куда будет заноситься результат
    for i in range(1, m+1):
        for j in range(1, n+1):
            price, weight = items[j-1] # присваиваем соответствующие данные об экспонате
            if weight <= k*i: # сравниваем вес экспоната с максимально возможным
                result[i][j] = max( result[i-1][j], result[i][j-1], result[i-1][j-1]+price)
            else: # если не можем взять текущий экспонат, берем все что уже есть в рюкзаке на предыдущем шаге
                result[i][j] = result[i-1][j]
    return print(result[m][n])

m = 3
k = 5
items = [ (10,5), (7,2), (5,1), (8,4), (6,3)]
# print(backpack(len(items), items, m, k))

if __name__ == '__main__':
    backpack(len(items), items, m, k)

