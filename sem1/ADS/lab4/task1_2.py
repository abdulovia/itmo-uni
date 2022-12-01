import task1_1 as mod # Используем функции как модуль 
from timeit import default_timer as timer

arr = [4, -3.9, -1, 0, -8, 2.4, 1, -14.01]
print(arr)
choice = input('Выберите метод сортировки: быстрая (0) / расчёской (1)? ')

start = timer()
if choice == '0':
    ans = mod.quick_sort(arr)
else:
    ans = mod.comb(arr)
end = timer()
print(f'Comb sort: {ans}\nTimeit: {end-start}')