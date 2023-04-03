import sqlite3, os

try:
    # создаем свою базу country.db
    connection = sqlite3.connect('music.db')

    cursor = connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    # считывание файла скрипта для создания таблиц
    with open('sqlite_create_tables.sql', 'r') as sqlite_file:
        sql_script = sqlite_file.read()

    # создает в базе таблицы Музыкант (tMusician), Песни (tSongs), Комментарии (tComments).
    cursor.executescript(sql_script)
    print("Скрипт SQLite успешно выполнен")

    # используя методы execute(), executemany() и запрос INSERT INTO, заполнить таблицу произвольными данными
    musicians = [
        ('Drake', 36, 'М'),
        ('Taylor Swift', 33, 'Ж'),
        ('The Weeknd', 33, 'М'),
        ('Kanye West', 45, 'М'),
        ('Eminem', 50, 'М'),
        ('Future', 39, 'М'),
        ('Justin Bieber', 29, 'М'),
        ('Моргенштерн', 25,'М')
    ]

    insert_query = '''INSERT INTO tMusician
    (musicianId, stageName, age, gender) VALUES (NULL, ?, ?, ?)
    '''
    cursor.executemany(insert_query, musicians)

    songs = [
        ('Blinding Lights', '2020', 3),
        ('Starboy', '2016', 3),
        ('Mask off', '2017', 6)
    ]
    insert_query = '''INSERT INTO tSongs
        (songId, songName, description, musicianId) VALUES (NULL, ?, ?, ?)
        '''
    cursor.executemany(insert_query, songs)

    comments = [
        ('I love this song!', 2, 3),
        ('Кто слушает в 2022?', 3, 6),
        ('Моя любимая песня!', 1, 3)
    ]
    insert_query = '''INSERT INTO tComments
            (commentId, comment, songId, musicianId) VALUES (NULL, ?, ?, ?)
            '''
    cursor.executemany(insert_query, comments)

    select_query_tMusician = '''SELECT * FROM tMusician'''
    select_query_tSongs = '''SELECT * FROM tSongs'''
    select_query_tComments = '''SELECT * FROM tComments'''

    cursor.execute(select_query_tMusician)
    print(*cursor.fetchone())
    print(*cursor.fetchmany(5))

    cursor.execute(select_query_tSongs)
    print(*cursor.fetchone())

    cursor.execute(select_query_tComments)
    print(*cursor.fetchall())

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    # закрыть соединение с базой
    if (connection):
        connection.commit()
        connection.close()
        print("Соединение с SQLite закрыто")
    os.remove("music.db")