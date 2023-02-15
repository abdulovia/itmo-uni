class Doctor():
    def __init__(self):
        self.name = 'Айболит'
        self.age = 25

    def getName(self):
        print(self.name)

    def setName(self, name):
        self.name = name

class Pediatrist(Doctor):
    days = ['Вт']
    sal = 60_000
    def getName(self):
        print('педиатр')

class Oculist(Doctor):
    days = ['Пн', 'Ср']
    sal = 45_000
    def getName(self):
        print('окулист')

class Dentist(Doctor):
    days = ['Пт', 'Сб']
    sal = 90_000
    def getName(self):
        print('дантист')

dr1 = Dentist()
dr1.getName()

dr2 = Oculist()
print(dr2.days, dr2.sal)
