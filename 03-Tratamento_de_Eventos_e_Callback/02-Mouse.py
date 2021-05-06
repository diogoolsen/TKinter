import sys
import tkinter as tk


class View():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x400')

        #
        # Associa eventos para:
        #
        # Quando a tela for clicada
        self.root.bind("<Button-1>", self.click)
        # Quando o cursor entrar na tela
        self.root.bind("<Enter>", self._in)
        # Quando o cursor sair da tela
        self.root.bind("<Leave>", self.out)

        # Quando a tecla ESC for pressionada
        self.root.bind('<Escape>', self.close)

        self.root.mainloop()

    def click(self, event):
        print('Click (' + str(event.x) + ',' + str(event.y) + ')')

    def _in(self, event):
        print('_in (' + str(event.x) + ',' + str(event.y) + ')')

    def out(self, event):
        print('out (' + str(event.x) + ',' + str(event.y) + ')')

    def close(self, evento=None):
        sys.exit()


View()
