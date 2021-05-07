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

        button = tk.Button(self.bottomFrame, text="^")
        button.grid(row=0, column=1)
        button = tk.Button(self.bottomFrame, text="V")
        button.grid(row=2, column=1)
        button = tk.Button(self.bottomFrame, text="<")
        button.grid(row=1, column=0)
        button = tk.Button(self.bottomFrame, text=">")
        button.grid(row=1, column=2)

        #
        # Utiliza o place para posicionar o label
        #
        # Baseia-se nas coordenadas X e Y para posicionar o componente
        #
        tk.Label(self.root, text="place(x=00, y=00)",
                 bg="black", fg="white").place(x=00, y=00)

        self.root.bind('<Escape>', self.close)

        self.root.mainloop()

    def close(self, evento=None):
        sys.exit()


View()
