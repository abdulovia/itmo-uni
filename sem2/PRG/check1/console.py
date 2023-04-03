from Pizzeria import *

class Console:
    user = welcome()
    session = Terminal()
    ord = Order()
    pizzas = [PizzaBarbeku(), PizzaPepperoni(), PizzaDaryMorya()]

    def start(self):
        while True:
            cmd = self.session.get_command()
            if cmd == 'menu':
                self.session.get_menu()
            elif cmd == 'add':
                n = int(input("Выберите пиццу [1-3]: 1 Барбекю 2 Пепперони 3 Дары Моря\n"))
                self.pizzas[n - 1].prep()
                self.pizzas[n - 1].star()
                self.pizzas[n - 1].bake()
                self.pizzas[n - 1].end()
                self.ord.order += [self.pizzas[n - 1]]
            elif cmd == 'del':
                self.ord.order.pop()
            elif cmd == 'order':
                if len(self.ord.order) == 0:
                    print("[]")
                for i in range(len(self.ord.order)):
                    print(i + 1, self.ord.order[i])
            elif cmd == 'new':
                self.ord = Order()
            elif cmd == 'pay':
                price = self.ord.get_order_price()
                if self.user.money >= price:
                    print("Заказ успешно оплачен. Спасибо, что выбираете нас. Приходите снова!")
                    self.user.money -= price
                    print("Остаток средств", self.user.money)
                    break
                else:
                    print("Недостаточно средств на счету!")