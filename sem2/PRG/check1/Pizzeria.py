import time
from abc import ABC, abstractmethod
class Pizza:
    name = "pizza"
    @abstractmethod
    def __init__(self, dough="", sauce="", filling="", price=""): # тесто соус начиинка цена
        self.dough = dough
        self.sauce = sauce
        self.filling = filling
        self.price = price

    def __add__(self, other):
        self.filling += other.filling

    def wait(func):
        def wrapper():
            func()
            time.sleep(2)
        return wrapper()

    @wait
    def opening():
        print("Подождите, пиццерия открывается...")
    @wait
    def opened():
        print("Пиццерия открыта, добро пожаловать!")
    def prep(self):
        print("Начинается процесс подготовки пиццы")

    def star(self):
        print("Тесто для пиццы замешено\nИнгридиенты для пиццы собраны\nПицца помещается в духовку")

    def bake(self):
        print("Пицца успешно испечена")

    def end(self):
        print("Пицца нарезана и упакована")

class Circle:
    def radius(self):
        print(3.14*30**2)
        
class PizzaBarbeku(Pizza):
    def __init__(self, add_fill=""):
        self.name = 'Барбекю'
        super().__init__("мягкое тесто для пиццы", "томатный соус", "сыр моцарелла, говядина, шампиньоны"+add_fill, 349)

    def __repr__(self):
        return self.filling

class Mixin(Circle, PizzaBarbeku):
    pass

class PizzaPepperoni(Pizza):
    def __init__(self, add_fill=""):
        self.name = 'Пепперони'
        super().__init__("стандартное тесто для пиццы", "томатный соус", "грибы, сыр моцарелла"+add_fill, 429)

    def __repr__(self):
        return self.name


class PizzaDaryMorya(Pizza):
    def __init__(self, add_fill=""):
        self.name = 'Дары Моря'
        super().__init__("тонкое тесто для пиццы", "соус", "зелень, морской коктйель, моцарелла"+add_fill, 499)

    def __repr__(self):
        return self.sauce

class Mixin1:
    def test(self):
        print("Mixin1")

class Terminal:
    '''
    Класс отвечает за взаимодействие с пользователем

    '''
    def __init__(self):
        print("Вас приветствует интерактивный помощник, который сегодня будет вас обслуживать\n")
        print("В нашей пиццерии вам доступны следующие комманды: \n"
              "menu – просмотреть меню;\n"
              "order – просмотреть заказ\n"
              "new – новый заказ;\n"
              "pay – оплатить заказ;\n"
              "add – добавить в заказ;\n"
              "del – удалить последнее из заказа.\n")

    def get_menu(self):
        print("Сегодня в меню:\n1. Пицца Барбекю \n2. Пицца Пепперони\n3. Пицца Дары Моря\n")

    def get_command(self):
        cmd = input("Введите комманду: ")
        return cmd

class Order:
    def __init__(self):
        print("Создан новый заказ")
        self.order = []

    def get_order_price(self):
        total = 0
        for pizza in self.order:
            total += pizza.price
        return total

class Mixins(Terminal, Order, Mixin1):
    pass

class welcome:
    def __init__(self):
        self.msg = input("Здравствуйте, как к вам можно обращаться? ")
        print("Welcome to our Pizzeria, "+self.msg)
        self.money = int(input("Введите сколько у вас средств на карточке: "))