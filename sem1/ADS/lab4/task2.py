def bucketSort(array): # Блочная сортировка
    bucket = []
    for i in range(len(array)):
        bucket.append([])
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


arr = [.42, .32, .33, .52, .37, .47, .51]
print(bucketSort(arr))





def heapSort(arr): # Пирамидальная сортировка
    def heapify(arr, n, i): # Наибольший в вершину дерева
        largest = i
        l, r = 2*i+1, 2*i+2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [4, -3.9, -1, 0, -8, 2.4, 1, -14.01]
heapSort(arr)
print(arr)