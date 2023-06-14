from Pizzeria import *
import asyncio
import sqlite3, os, sys
import tkinter as tk
from tkinter import ttk

class Console:
    user = welcome()
    session = Terminal()
    ord = Order()
    pizzas = [PizzaBarbeku(), PizzaPepperoni(), PizzaDaryMorya()]
    
    def start(self):
        try:
            connection = sqlite3.connect('pizzeria.db')
            cursor = connection.cursor()
            create_table_query = '''CREATE TABLE tOrder (
    id INTEGER PRIMARY KEY,
    pizza TEXT NOT NULL);
    '''
            cursor.execute(create_table_query)
            
            while True:
                cmd = self.session.get_command()
                if cmd == 'menu':
                    self.session.get_menu()
                elif cmd == 'add':
                    n = int(input("Выберите пиццу [1-3]: 1 Барбекю 2 Пепперони 3 Дары Моря\n"))
                    if n <= 0 or n > 3:
                        raise WrongPizzaError(n)
                    coro = self.pizzas[n - 1].prep()
                    # self.pizzas[n - 1].star()
                    # self.pizzas[n - 1].bake()
                    # self.pizzas[n - 1].end()
                    # создание потока процесса
                    # вызов процесса в многопоточном режиме
                    asyncio.run(coro)
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
                        insert_query = '''INSERT INTO tOrder
                        (id, pizza) VALUES (?, ?)
                        '''
                        tPizza = [(i+1, f'{self.ord.order[i]}') for i in range(len(self.ord.order))]
                        # print(tPizza)
                        cursor.executemany(insert_query, tPizza)
                        select_query = '''SELECT * FROM tOrder'''
                        cursor.execute(select_query)
                        print('fetchone(): ', *cursor.fetchone())
                        print('Все оставшиеся записи', *cursor.fetchall())
                        cursor.close()
                        break
                    else:
                        print("Недостаточно средств на счету!")
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            # закрыть соединение с базой
            if (connection):
                connection.commit()
                connection.close()
                print("Соединение с SQLite закрыто")
            # os.remove("pizzeria.db")