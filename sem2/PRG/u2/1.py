class Pupil:
    name, age, classNumber = 'Radomir', 8, '1-A'

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setClassNumber(self, num):
        self.classNumber = num

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

    def getClassNumber(self):
        print(self.classNumber)

    def allInfo(self):
        print(self.name, self.age, self.classNumber)


p1, p2, p3, p4, p5 = Pupil(), Pupil(), Pupil(), Pupil(), Pupil()

p1.setName('Vladimir')
p1.setAge(68)
p1.setClassNumber('11-B')
p1.allInfo()

p2.setName('Petr')
p2.setAge(32)
p2.allInfo()

p3.allInfo()

p4.setClassNumber('10-C')
p4.getClassNumber()
