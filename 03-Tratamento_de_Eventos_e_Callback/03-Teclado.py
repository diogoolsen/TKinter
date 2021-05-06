import sys
import tkinter as tk


class View():
    def __init__(self):
        self.root = tk.Tk()

        self.entry = tk.Entry(self.root, width=30)

        self.entry.pack()

        #
        # Associa funções aos eventos de:
        #
        # Alguma tecla for pressionada
        self.entry.bind("<Key>", self.trataTeclado)
        # Alguma tecla for liberada
        self.entry.bind("<KeyRelease>", self.trataTexto)
        # Tecla enter pressionada
        self.entry.bind("<Return>", self.trataEnter)
        # Teclas CTRL + C forem pressionadas
        self.entry.bind("<Control-c>", self.trataCopia)

        # Tecla ESC for pressionada
        self.root.bind('<Escape>', self.close)

        self.root.mainloop()

    def trataTeclado(self, event):
        print('Teclado pressionado - Texto:', self.entry.get())

    def trataTexto(self, event):
        print('Teclado Liberado - Texto:', self.entry.get())
        # Muito usado para autocompletar com consulta em BD

    def trataEnter(self, event):
        print('Enter pressionado - Texto:', self.entry.get())

    def trataCopia(self, event):
        print('CTRL+C pressionado - Texto:', self.entry.get())

    def close(self, evento=None):
        sys.exit()


View()
