class Cat:
    def __init__(self, name='', age=0):
        self.name = name
        if age < 0 or age > 19:
            print('Возраст не корректен, выставлено значение по умолчанию [0]')
            self.age = 0
        else:
            self.age = age


class Sphinx(Cat):
    sherst = 'лысый'
    predn = 'охотник'


class Meicun(Cat):
    sherst = 'длинная'
    predn = 'крысолов'


class Korat(Cat):
    sherst = 'средняя'
    predn = 'играет'


cat1 = Sphinx('мурзик', 3)
cat2 = Meicun('мэй', 1)
cat3 = Korat('котенок', 2)
print(cat2.name, cat2.predn)
print(cat3.name, cat3.sherst)
print(cat1.sherst, cat1.name)

cat4 = Sphinx('кошечка', -1)
print(cat4.age)