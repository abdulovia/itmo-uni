class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        a, b, c = self.a, self.b, self.c
        if a+b <= c or a+c <= b or b+c <= a:
            print('Треугольника не существует')
        else:
            p = (a + b + c)/2
            print(f'{((p-a)*(p-b)*(p-c)*p)**0.5:.2f}')


rvnst = Triangle(2, 2, 2)
simp = Triangle(1, 2, 2)
nexist = Triangle(4, 9, 2)
rvnst.square()
simp.square()
nexist.square()