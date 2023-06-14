import sqlite3

class Transport:
    def __init__(self, name, capacity, length, width, height):
        self.name = name
        self.capacity = capacity
        self.length = length
        self.width = width
        self.height = height

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('transport.db')
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transports (
            name TEXT, capacity REAL, length REAL, width REAL, height REAL)''')
        self.conn.commit()
    