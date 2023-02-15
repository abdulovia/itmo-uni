class Coffee:
    def __init__(self, add=''):
        self.add = add

    def show_my_drink(self):
        if self.add == '':
            print('Черный кофе')
        else:
            print('Кофе и', self.add)

coffee_1 = Coffee('сахар')
coffee_2 = Coffee()
coffee_1.show_my_drink()
coffee_2.show_my_drink()