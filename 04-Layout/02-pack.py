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
        self.bottomFrame.pack(fill=tk.Y, expand=True)

        button = tk.Button(self.bottomFrame, text="^")
        button.pack(side=tk.TOP)
        button = tk.Button(self.bottomFrame, text="V")
        button.pack(side=tk.BOTTOM)
        button = tk.Button(self.bottomFrame, text="<")
        button.pack(side=tk.LEFT)
        button = tk.Button(self.bottomFrame, text=">")
        button.pack(side=tk.RIGHT)

        self.root.bind('<Escape>', self.close)

        self.root.mainloop()

    def close(self, evento=None):
        sys.exit()


View()
