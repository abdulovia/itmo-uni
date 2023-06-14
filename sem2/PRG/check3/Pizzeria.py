import time
from abc import ABC, abstractmethod
import asyncio

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

    def opening():
        print("Подождите, пиццерия открывается...")
    def opened():
        print("Пиццерия открыта, добро пожаловать!")

        
class PizzaBarbeku(Pizza):
    def __init__(self, add_fill=""):
        self.name = 'Барбекю'
        super().__init__("мягкое тесто для пиццы", "томатный соус", "сыр моцарелла, говядина, шампиньоны"+add_fill, 349)

    def __repr__(self):
        return self.name

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
        return self.name


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

class MoneyLowerThanZeroError(Exception): # Класс исключений
    '''Исключение возникает из-за отрицательной денежной суммы.
    
    Атрибуты:
        money: число, которое вызвало ошибку
        message: объяснение ошибки
    '''
    def __init__(self, money, message="Количество средств не может быть отрицательным числом"):
        self.money = money
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f'{self.money} -> {self.message}'
        

class welcome:
    def __init__(self):
        self.msg = input("Здравствуйте, как к вам можно обращаться? ")
        print("Welcome to our Pizzeria, "+self.msg)
        # перехват исключения, когда пользователь не вводит целое число
        while True:
            try:
                self.money = int(input("Введите сколько у вас средств на карточке: "))
                if self.money < 0:
                    raise MoneyLowerThanZeroError(self.money) # применение собственного класса исключений
                break
            except ValueError:
                print("Введите целое число!")
        