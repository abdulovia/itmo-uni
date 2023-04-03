import sqlite3, os

try:
    # создаем свою базу country.db
    connection = sqlite3.connect('country.db')
    create_table_query = '''CREATE TABLE tCountry (
    id INTEGER PRIMARY KEY,
    country TEXT NOT NULL);
    '''

    cursor = connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    # создать в базе таблицу tCountry и полями: номер п/п, название страны
    cursor.execute(create_table_query)

    # используя методы execute(), executemany() и запрос INSERT INTO, заполнить таблицу произвольными данными
    countries = [
        (1, 'Россия'),(2, 'США'),(3, 'Великобритания'),(4, 'Эстония'),(5, 'Финляндия'),(6, 'Норвегия'),(7, 'Дания'),(8, 'Китай'),(9, 'Япония'),(10, 'Канада'),
    ]

    insert_query = '''INSERT INTO tCountry
    (id, country) VALUES (?, ?)
    '''
    cursor.executemany(insert_query, countries)

    select_query = '''SELECT * FROM tCountry'''
    cursor.execute(select_query)

    total = cursor.fetchone()
    print('.fetchone(): ', *total)

    total = cursor.fetchmany(3)
    print('.fetchmany(): ', *total)

    # снова делаем SELECT запрос ко всей таблице
    cursor.execute(select_query)

    total = cursor.fetchall()
    print('.fetchall(): ', *total)

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:

    # закрыть соединение с базой
    if (connection):
        connection.commit()
        connection.close()
        print("Соединение с SQLite закрыто")
    os.remove("country.db")
