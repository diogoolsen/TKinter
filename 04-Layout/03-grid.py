import tkinter as tk
import sys


class View():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x400")

        self.topFrame = tk.Frame(relief=tk.RAISED, borderwidth=1, bg="red")
        self.topFrame.pack(fill=tk.BOTH, expand=True)

        self.bottomFrame = tk.Frame(
            relief=tk.RAISED, borderwidth=1, bg="green")
        self.bottomFrame.pack()

        #
        # Utiliza o GRID para posicionar os componentes
        #
        # Funciona como uma matriz, baseando as posições em linhas e colunas
        #
        button = tk.Button(self.bottomFrame, text="^")
        button.grid(row=0, column=1)
        button = tk.Button(self.bottomFrame, text="V")
        button.grid(row=2, column=1)
        button = tk.Button(self.bottomFrame, text="<")
        button.grid(row=1, column=0)
        button = tk.Button(self.bottomFrame, text=">")
        button.grid(row=1, column=2)

        self.root.bind('<Escape>', self.close)

        self.root.mainloop()

    def close(self, evento=None):
        sys.exit()


View()
