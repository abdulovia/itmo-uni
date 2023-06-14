from transport import *
import asyncio
import sqlite3
import os


class WrongTrasnportError(Exception):
    def __init__(self, n, message="!"):
        self.n = n
        self.message = message
        super().__init__(self.message)


class Console:
    user = User()
    session = Terminal()
    # order = Order()

    def start(self):
        try:
            connection = sqlite3.connect('transport.db')
            cursor = connection.cursor()
            create_table_query = '''CREATE TABLE tTransport (
    id INTEGER PRIMARY KEY,
    type TEXT NOT NULL,
    load INTEGER,
    length INTEGER,
    width INTEGER,
    height INTEGER,
    );
    '''
            cursor.execute(create_table_query)

            while True:
                cmd = self.session.get_command()
                if cmd == 'new':
                    
                elif cmd == 'del':
                    self.ord.order.pop()
                elif cmd == 'all':
                    pass
                elif cmd == 'load':
                    if len(self.ord.order) == 0:
                        print("[]")
                    for i in range(len(self.ord.order)):
                        print(i + 1, self.ord.order[i])
                elif cmd == 'available':
                    self.ord = Order()
                elif cmd == 'unavailable':
                    pass
                elif cmd == 'send':
                    pass
                elif cmd == 'order':
                    price = self.ord.get_order_price()
                    if self.user.money >= price:
                        print(
                            "Заказ успешно оплачен. Спасибо, что выбираете нас. Приходите снова!")
                        self.user.money -= price
                        print("Остаток средств", self.user.money)
                        insert_query = '''INSERT INTO tOrder
                        (id, pizza) VALUES (?, ?)
                        '''
                        tPizza = [(i+1, f'{self.ord.order[i]}')
                                  for i in range(len(self.ord.order))]
                        # print(tPizza)
                        cursor.executemany(insert_query, tPizza)
                        select_query = '''SELECT * FROM tOrder'''
                        cursor.execute(select_query)
                        print('fetchone(): ', *cursor.fetchone())
                        print('Все оставшиеся записи', *cursor.fetchall())
                        cursor.close()
                        break
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (connection):
                connection.commit()
                connection.close()
                print("Соединение с SQLite закрыто")
            os.remove("transport.db")
