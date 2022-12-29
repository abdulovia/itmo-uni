STEP = 0


def binary_search(array, element, start, end):
    """Рекурсивный вариант бинарного поиска"""
    if start > end:  # если элемент не существует в списке
        return 'Данного элемента нет в списке!'

    global STEP
    STEP += 1
    mid = (start + end) // 2
    if element == array[mid]:
        return f'Итоговое количество шагов: {STEP}'

    if element < array[mid]:
        return binary_search(array, element, start, mid - 1)
    else:
        return binary_search(array, element, mid + 1, end)


try:
    print('Доброго времени суток! Данная программа осуществляет алгоритм бинарного поиска и '
          'выводит количество шагов для нахождения искомого числа!')
    arr = [int(i) for i in input('Для начала запишите через пробел все целые числа '
                                 'в порядке возрастания, среди которых будет вестись поиск:\n').split()]
    el = int(input('Теперь введите искомое число: '))
    print(binary_search(sorted(arr), el, 0, len(arr) - 1))
except Exception:
    print('Некорректный формат ввода!')
