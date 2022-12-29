# O(3n) - создать три пустых массива
mas1 = [0]*10
mas2 = [0]*10
mas3 = [0]*10

# O(nlog n)
mas1 = [-3, 4, 2, 0]
mas2 = sorted(mas1)
print(mas1)
print(mas2)
for i in mas1:
  l, r = 0, len(mas2)-1
  while l < r:
    mid = (l+r)//2
    if mas2[mid] < i:
      l = mid + 1
    else:
      r = mid
  print(l, end=' ') # Индекс элемента в сортированном массиве
  
# O(n!) - количество перестановок
m1 = [1, 3, -2]
def rec(a, m1):
  if len(a) == len(m1):
    print(a)
    return
  for i in m1:
    if i not in a:
      rec(a+[i], m1)
rec([], m1)

# O(n^3) - 3 цикла
for i in range(n):
  for j in range(n):
    for z in range(n):
      b[z] += a[i]-m[j]
      
# O(3log(n)) - 3 бинпоиска, поиск индекса элемента в массиве m1
from random import randint
m1.sort()
print(m1)
for i in range(3):
  elem = randint(-4, 4)
  l, r = 0, len(m1)-1
  while l < r:
    mid = (l+r)//2
    if m1[mid] < elem:
      l = mid + 1
    else:
      r = mid
  if elem == m1[l]:
    print(elem, l)
  else:
    print('no', elem, 'in the list')