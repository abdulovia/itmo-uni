import tkinter as tk
from tkinter import ttk
import sys

ttl = 0

class Pizza:
    name = "pizza"
    def __init__(self, dough="", sauce="", filling="", price=149):
        self.dough = dough
        self.sauce = sauce
        self.filling = filling
        self.price = price

    def __add__(self, other):
        self.filling += other.filling

        
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

class Order:
    def __init__(self):
        self.order = []

    def get_order_price(self):
        total = 0
        for pizza in self.order:
            total += pizza.price
        return total

def show_message():
    global ttl
    text = entry.get()
    if text == 'BBQ':
        order.order += [PizzaBarbeku()]
    elif text == 'PEP':
        order.order += [PizzaPepperoni()]
    elif text == 'DAR':
        order.order += [PizzaDaryMorya()]
    ttl += 149
    label["text"] = order.order
    
def del_pizza():
    global ttl
    if len(order.order) > 0:
        order.order.pop()
    ttl -= 149
    label["text"] = order.order
    
def show_price():
    global ttl
    label["text"] = ttl

root = tk.Tk()
root.geometry("960x720+600+200")
root.title = "Pizzeria"

order = Order()
# tk.resizable(False, False)

mainmenu = tk.Menu(root) 
root.config(menu=mainmenu) 

filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Выход", command=root.quit)

operations = tk.Menu(mainmenu, tearoff=0)
operations.add_command(label="Очистить данные")

helpmenu = tk.Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="О программе")

mainmenu.add_cascade(label="Файл",
                    menu=filemenu)
mainmenu.add_cascade(label="Операции",
                    menu=operations)
mainmenu.add_cascade(label="Справка",
                    menu=helpmenu)

entry = ttk.Entry()
entry.pack(anchor=tk.NW, padx=6, pady=6)

btn = ttk.Button(text="Добавить", command=show_message)
btn.pack(anchor=tk.NW, padx=6, pady=6)

dbtn = ttk.Button(text="Удалить", command=del_pizza)
dbtn.pack(anchor=tk.NW, padx=6, pady=6)

pbtn = ttk.Button(text="Стоимость", command=show_price)
pbtn.pack(anchor=tk.NW, padx=6, pady=6)
 
label = ttk.Label()
label.pack(anchor=tk.NW, padx=6, pady=6)

root.mainloop()