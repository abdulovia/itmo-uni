import tkinter as tk
from tkinter import ttk
from utils import Transport, Database


class MainApp(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Создание базы данных SQLite и таблиц для хранения информации о грузах и транспорте
        self.db = Database()
        self.db.create_tables()

        # Создание виджетов для графического интерфейса
        self.layout = tk.Frame(self)

        # Создание кнопок для добавления/удаления грузового транспорта и просмотра доступного транспорта
        self.add_transport_button = ttk.Button(
            self.layout, text='Добавить транспорт', command=self.add_transport)
        self.remove_transport_button = ttk.Button(
            self.layout, text='Удалить транспорт', command=self.remove_transport)
        self.view_transport_button = ttk.Button(
            self.layout, text='Просмотреть доступный транспорт', command=self.view_transport)

        # Создание таблицы для отображения информации о грузах и транспорте
        self.table = ttk.Treeview(self.layout, columns=(
            'name', 'weight', 'length', 'width', 'height'))
        self.table.heading('name', text='Тип')
        self.table.heading('weight', text='Грузоподъемность')
        self.table.heading('length', text='Длина')
        self.table.heading('width', text='Ширина')
        self.table.heading('height', text='Высота')

        # Добавление кнопок на главное окно
        self.add_transport_button.pack(side=tk.BOTTOM, padx=5, pady=5)
        self.remove_transport_button.pack(side=tk.BOTTOM, padx=5, pady=5)
        self.view_transport_button.pack(side=tk.BOTTOM, padx=5, pady=5)

        # Добавление таблицы на главное окно
        self.table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.layout.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def add_transport(self):
        # Создание формы для добавления нового транспорта
        add_form = tk.Toplevel(self)
        add_form.title('Добавление нового транспорта')

        # Создание виджетов для формы добавления нового транспорта
        name_label = ttk.Label(add_form, text='Название')
        name_entry = ttk.Entry(add_form)
        capacity_label = ttk.Label(add_form, text='Грузоподъемность')
        capacity_entry = ttk.Entry(add_form)
        length_label = ttk.Label(add_form, text='Длина')
        length_entry = ttk.Entry(add_form)
        width_label = ttk.Label(add_form, text='Ширина')
        width_entry = ttk.Entry(add_form)
        height_label = ttk.Label(add_form, text='Высота')
        height_entry = ttk.Entry(add_form)

        # Размещение виджетов на форме добавления нового транспорта
        name_label.grid(row=0, column=0, padx=5, pady=5)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        capacity_label.grid(row=1, column=0, padx=5, pady=5)
        capacity_entry.grid(row=1, column=1, padx=5, pady=5)
        length_label.grid(row=2, column=0, padx=5, pady=5)
        length_entry.grid(row=2, column=1, padx=5, pady=5)
        width_label.grid(row=3, column=0, padx=5, pady=5)
        width_entry.grid(row=3, column=1, padx=5, pady=5)
        height_label.grid(row=4, column=0, padx=5, pady=5)
        height_entry.grid(row=4, column=1, padx=5, pady=5)

        # Создание функции для обработки нажатия кнопки "Добавить"
        def add_transport_to_db():
            # Получение данных о новом транспорте из виджетов на форме
            name = name_entry.get()
            capacity = capacity_entry.get()
            length = length_entry.get()
            width = width_entry.get()
            height = height_entry.get()

            # Добавление нового транспорта в базу данных
            self.db.add_transport(name, capacity, length, width, height)

            # Обновление таблицы на главном окне
            self.update_table()

            # Закрытие формы добавления нового транспорта
            add_form.destroy()

        # Создание кнопки "Добавить" и привязка к ней функции add_transport_to_db()
        add_button = ttk.Button(add_form, text='Добавить',
                                command=add_transport_to_db)
        add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


    def remove_transport(self, transport_id):
        # Удаление транспорта из базы данных
        self.db.remove_transport(transport_id)

        # Обновление таблицы на главном окне
        self.update_table()


    def update_table(self):
        # Очистка таблицы на главном окне
        for row in self.table.get_children():
            self.table.delete(row)

        # Получение списка всех транспортных средств из базы данных
        transports = self.db.get_all_transports()

        # Добавление каждого транспорта в таблицу на главном окне
        for transport in transports:
            self.table.insert('', 'end', values=(transport.id, transport.name,
                            transport.capacity, transport.length, transport.width, transport.height))

    def view_transport(self, transport_id):
        # Получение информации о выбранном транспорте из базы данных
        transport = self.db.get_transport_by_id(transport_id)

        # Создание формы для просмотра информации о транспорте
        transport_form = tk.Toplevel(self)
        transport_form.title('Просмотр транспорта')

        # Создание виджетов для формы просмотра информации о транспорте
        name_label = ttk.Label(transport_form, text='Название')
        name_value = ttk.Label(transport_form, text=transport.name)
        capacity_label = ttk.Label(transport_form, text='Грузоподъемность')
        capacity_value = ttk.Label(transport_form, text=transport.capacity)
        length_label = ttk.Label(transport_form, text='Длина')
        length_value = ttk.Label(transport_form, text=transport.length)
        width_label = ttk.Label(transport_form, text='Ширина')
        width_value = ttk.Label(transport_form, text=transport.width)
        height_label = ttk.Label(transport_form, text='Высота')
        height_value = ttk.Label(transport_form, text=transport.height)

        # Размещение виджетов на форме просмотра информации о транспорте
        name_label.grid(row=0, column=0, padx=5, pady=5)
        name_value.grid(row=0, column=1, padx=5, pady=5)
        capacity_label.grid(row=1, column=0, padx=5, pady=5)
        capacity_value.grid(row=1, column=1, padx=5, pady=5)
        length_label.grid(row=2, column=0, padx=5, pady=5)
        length_value.grid(row=2, column=1, padx=5, pady=5)
        width_label.grid(row=3, column=0, padx=5, pady=5)
        width_value.grid(row=3, column=1, padx=5, pady=5)
        height_label.grid(row=4, column=0, padx=5, pady=5)
        height_value.grid(row=4, column=1, padx=5, pady=5)
