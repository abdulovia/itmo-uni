from tkinter import *
from tkinter import ttk

class Main(Frame):
    def __init__(self, tk):
        super(Main, self).__init__(tk)
        if tk.title() == "Калькулятор":
            return
        tk.title("Калькулятор")
        self.build()
        
    def build(self):
        btns = [
            "CE", "⌫", "%", "÷",
            "7", "8", "9", "×",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "^", "0", ".", "="
        ]
        x, y = 10, 140
        for bt in btns:
            com = lambda x=bt: self.logic(x)
            Button(text=bt,
                   font=("", 16, "bold"),
                   command=com).place(x=x, y=y, width=115, height=80)
            x += 117
            if x > 400:
                x = 10
                y += 81
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("", 48, "bold"))
        self.lbl.place(x=15, y=40)
    
    def logic(self, operation):
        if operation == "CE":
            self.formula = ""
        elif operation == "⌫":
            self.formula = self.formula[0:-1]
        elif operation == "^":
            self.formula += "**"
        elif operation == "×":
            self.formula += "*"
        elif operation == "÷":
            self.formula += "/"
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0" and operation in "0123456789":
                self.formula = ""
            self.formula += operation
        self.update()
    
    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)
        
class Re(Frame):
    def __init__(self, tk):
        super(Re, self).__init__(tk)
        if tk.title() == "Прямоугольник":
            return
        tk.title("Прямоугольник")
        self.build()
        
    def build(self):
        ttk.Label(text="Длина прямоугольника:").pack()
        self.width = ttk.Entry()
        self.width.pack()
        ttk.Label(text="Ширина прямоугольника:").pack()
        self.length = ttk.Entry()
        self.length.pack()
        canvas = Canvas(bg="white", width=220, height=200)
        canvas.pack(anchor=CENTER, expand=1)
        com = lambda x="Расчёт": self.logic(canvas)
        Button(text="Расчёт", command=com).place(x=195, y=150, width=100, height=50)
        self.lblSq = Label(text="Площадь прямоугольника: 0")
        self.lblSq.place(x=150, y=205)
        self.lblPe = Label(text="Периметр прямоугольника: 0")
        self.lblPe.place(x=150, y=225)
    
    def logic(self, canvas):
        w = int(self.width.get())
        l = int(self.length.get())
        canvas.delete("all")
        canvas.create_rectangle(10, 20, 10+w, 10+l, fill="#80CBC4", outline="#004D40")
        square = w * l
        perimeter = (w + l) * 2
        self.update(square, perimeter)
    
    def update(self, square, perimeter):
        self.lblSq.configure(text="Площадь прямоугольника: "+str(square))
        self.lblPe.configure(text="Периметр прямоугольника: "+str(perimeter))

def clear_frame():
   for widgets in tk.winfo_children():
       if not isinstance(widgets, Radiobutton):
           widgets.destroy()

def calc():
    var.get()
    clear_frame()
    Main(tk).pack()
    
def rect():
    var.get()
    clear_frame()
    Re(tk).pack()
    
def about():
    window = Tk()
    window.title("О программе")
    window.geometry("400x100")
    label=ttk.Label(window, text="Пиццерия \nЭто программа российского производства, 2023г. \nЭто программа разработана на КР3 по программированию в \nИТМО под руководством Казановой П.П.")
    label.pack(anchor=CENTER, expand=1)
    

tk = Tk()
tk.geometry("485x550+600+200")

tk.resizable(False, False)

mainmenu = Menu(tk) 
tk.config(menu=mainmenu) 

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Выход", command=tk.quit)

operations = Menu(mainmenu, tearoff=0)
operations.add_command(label="Очистить данные", command=clear_frame)

helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="О программе", command=about)

mainmenu.add_cascade(label="Файл",
                    menu=filemenu)
mainmenu.add_cascade(label="Операции",
                    menu=operations)
mainmenu.add_cascade(label="Справка",
                    menu=helpmenu)

var = StringVar(tk, "CALC")
tk.title("Starting app...")
Main(tk).pack()
Radiobutton(text="Калькулятор", command=calc,
        variable=var, value="CALC").pack()
Radiobutton(text="Прямоугольник", command=rect,
        variable=var, value="RECT").pack()

tk.mainloop()
    