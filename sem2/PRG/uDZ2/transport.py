import time
from abc import ABC, abstractmethod
import asyncio
class Transport:
    @abstractmethod
    def __init__(self, tpe="", load=0, length=0, width=0, height=0, booked=False):
        self.tpe = tpe
        self.load = load
        self.length = width
        self.height = height
        self.booked = booked


class Terminal:
    '''
    Этот класс отвечает за взаимодействие с пользователем
    через внутриинтерфейсную консоль
    '''
    def __init__(self):
        print(
            "Добро пожаловать в ПО компании 'Грузовой Автотранспорт'\n"
            "В нашей программе вам доступны следующие комманды: \n"
            "new – добавить грузовой транспорт\n"
            "del – удалить грузовой транспорт\n"
            "all – просмотреть весь автотранспорт\n"
            "load – просмотреть транспорт по грузоподъемности\n" 
            "available – просмотреть свободный грузовой транспорт\n"
            "unavailable – просмотреть занятый грузовой транспорт\n"
            "send – заявка на перевоз груза по габаритам\n"
            "order – подобрать и забронировать транспорт\n"
            )

    def get_menu(self):
        print("Сегодня в меню:\n1. Пицца Барбекю \n2. Пицца Пепперони\n3. Пицца Дары Моря\n")

    def get_command(self):
        cmd = input("Введите комманду: ")
        return cmd

class Order:
    def __init__(self):
        print("Создан новый заказ")
        self.order = []

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
        

class User:
    def __init__(self):
        self.name = input("Здравствуйте, введите имя ")
        print("Добро пожаловать в наш сервис, " + self.name)
        