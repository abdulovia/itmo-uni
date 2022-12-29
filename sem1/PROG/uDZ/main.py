collection = []
from datetime import datetime
def validate(date):
    try:
        datetime.strptime(date, '%d.%m.%Y')
    except ValueError:
        return False
    return True

    
def add():
    global collection
    product = input('Введите название продукта: ')
    category = input('Введите название категории: ')
    cost = input('Введите стоимость продукта (в рублях): ')
    date = input('Введите корректную дату покупки в формате ДД.ММ.ГГГГ: ')
    if not product or not category or not cost or not date or \
        not cost.isnumeric() or not validate(date):
        print('Ввод не распознан!')
        return
    print('Продукт добавлен в коллекцию!')
    collection += [[int(cost), product, category, date]]


def table_item(item):
    print(f'{item[1]:32s} {item[2]:32s} {item[0]:<10d} {item[3]:15s}')


def table_title():
    print(f'{"Продукт":32s} {"Категория":32s} {"Цена":<10s} {"Дата покупки":15s}')
    print('_'*89)


def All():
    table_title()
    for item in collection:
        table_item(item)
    print()


def bycd():
    flag = input('Просмотреть продукты по дате (0) или категории (1)? ')
    if flag == '1':
        cat = input('Введите категорию: ')
        table_title()
        for item in collection:
            if item[2] == cat:
                table_item(item)
    elif flag == '0':
        date = input('Введите дату в формате ДД.ММ.ГГГГ: ')
        if not validate(date): 
            print('Дата не распознана!')
            return
        table_title()
        for item in collection:
            if item[3] == date:
                table_item(item)
    else:
        print('Ввод не распознан!')
    print()


def Sort():
    global collection
    flag = input('Сортировать стоимость продуктов по убыванию (0) или по возрастанию (1)? ')
    if flag == '1':
        collection.sort()
    elif flag == '0':
        collection.sort(reverse=True)
    else:
        print('Ввод не распознан!')
        return
    All()


def Del():
    for i in range(len(collection)):
        item = collection[i]
        print(f'{str(i+1)}. [{item[1]}, {item[2]}, {item[0]}, {item[3]}]')
    flag = input('Введите номер записи, которую желаете удалить: ')
    if flag.isnumeric() and 1 <= int(flag) <= len(collection):
        flag = int(flag)-1
        item = collection.pop(flag)
        print(f'Запись [{item[1]}, {item[2]}, {item[0]}, {item[3]}] удалена из коллекции')
        print()
    else:
        print('Ввод не распознан!')
        

def extract():
    global collection
    with open('data.txt') as w: # data.txt – текстовый файл с продуктами
        for line in w.readlines():
            li = line.split('_')
            collection += [[int(li[0]), li[1], li[2], li[3]]]


def save():
    with open('data.txt', 'w') as w:
        for item in collection:
            w.write(f'{item[0]}_{item[1]}_{item[2]}_{item[3]}_\n')
    print('Коллекция сохранена в файл!')
    print()


def helper():
    print('!add – добавляет продукт в коллекцию')
    print('!all – показывает все продукты')
    print('!bycd – просмотреть продукты по дате и категории')
    print('!sort – распределяет продукты по стоимости')
    print('!del – удаляет запись')
    print('!save – сохраняет коллекцию в файл')
    print('!exit – выходит из программы')
    print()


command_dict = {
    '!add': add,
    '!all': All,
    '!bycd': bycd,
    '!sort': Sort,
    '!del': Del,
    '!exit': exit,
    '!help': helper,
    '!save': save,
}
print('Программа для контроля собственных денежных средств запущена\n')
helper() # Выводит команды, которые обрабатывает программа
extract() # Извлекает сохраненные продукты из файла в коллекцию
err_c = 0
while True:
    s = input('Введите команду: ')
    if s: s = s.split()[0]
    else: s = '!'
    if s[0] != '!': s = '!'+s
    if s in command_dict:
        command_dict[s]()
        err_c = 0
    else:
        err_c += 1
        if err_c > 2:
            print('Превышено количество попыток ввода, программа закрывается')
            break
        print('Команда введена неверно, попробуйте ещё раз!')
        continue
    
    
# сделать отчет в латехе всех функций программы, написать подробное описание текстом как работает функция
# описание этапа анализа предметной области и требований, строго по uDZ.pdf
# как работает программа на каждом этапе, четко и понятно для человека, который впервые видит эту программу
# в конце примерная работа программы на примерах
        