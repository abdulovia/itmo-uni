class Mathem:

    def addition(self, a, b):
        return a + b

    def multiplication(self, a, b):
        return a * b

    def division(a, b):
        if b == 0:
            return 'деление на ноль!'
        return a / b

    def substraction(a, b):
        return a - b

m=Mathem()
print(m.addition(1, 3))
print(m.multiplication(1, 3))