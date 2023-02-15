class Tree:
    p, v = False, False

    def __init__(self, name, age, height):
        self.name, self.age, self.height = name, age, height

    def peresadka(self):
        if self.p:
            print('уже было пересажено')
            return
        self.p = True
        print('Дерево пересадили')

    def virubka(self):
        if self.v:
            print('уже было вырублено')
            return
        self.v = True
        print('Дерево вырубили')

    def namin(self, name):
        self.name = name

    def agein(self, age):
        self.age = age

    def heightin(self, height):
        self.height = height

    def allInfo(self):
        print(self.name, self.age, self.height)


tree1 = Tree('Derevo', 10, '3m')
tree1.allInfo()
tree1.virubka()
tree1.virubka()