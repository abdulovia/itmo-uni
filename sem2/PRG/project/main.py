import tkinter as tk
from gui import MainApp

if __name__ == '__main__':
    root = tk.Tk()
    main_app = MainApp(root)
    main_app.pack()
    root.mainloop()
