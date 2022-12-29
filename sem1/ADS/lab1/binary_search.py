a = [1, 4, 9, 3, 2, 0, -1, 3, 4, 11]
a.sort()
elem = 9
left, right = 0, len(a)-1
while left<right:
    mid = (left+right)//2
    if a[mid]<elem:
        left = mid+1
    else:
        right = mid
if a[left]==elem: print("Найден элемент", elem)
