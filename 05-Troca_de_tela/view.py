import sys

import tkinter as tk
from tkinter import messagebox

# Alternativa mais elegante
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter


class View():

    def __init__(self):
        self.root = tk.Tk()

        # Cria um frame e o posiciona na janela
        self.container = tk.Frame(self.root)
        self.container.pack()

        # Cria 3 outros Frames, associados frame anterior (self.container)
        self.createFrame1()
        self.createFrame2()
        self.createFrame3()

        # Posiciona todos com grid na mesma posição
        self.frame1.grid(row=0, column=0, sticky='nsew')
        self.frame2.grid(row=0, column=0, sticky='nsew')
        self.frame3.grid(row=0, column=0, sticky='nsew')

        # Seleciona qual dos frames será exibido
        self.showFrame1()

        self.root.bind('<Escape>', self.close)

        self.root.mainloop()

    def close(self, evento=None):
        sys.exit()

    def showFrame1(self):
        # Exibe o frame 1
        self.frame1.tkraise()

    def showFrame2(self):
        # Exibe o frame 2
        self.frame2.tkraise()

    def showFrame3(self):
        # Exibe o frame 3
        self.frame3.tkraise()

    def showInfo(self):
        messagebox.showinfo('Informação', 'Info!!!')

    def showWarning(self):
        messagebox.showwarning('Warning', 'Aviso!!')

    def showError(self):
        messagebox.showerror('Error', 'Erro!!')

    def createFrame1(self):
        self.frame1 = tk.Frame(self.container)

        label = tk.Label(self.frame1, text='Página 1')
        label.pack(side='top')

        buttonMsg = tk.Button(self.frame1, text='Mensagem',
                              command=self.showInfo)
        buttonMsg.pack(side='top')

        buttonNext = tk.Button(self.frame1, text='Próxima tela',
                               command=self.showFrame2)
        buttonNext.pack(side='right')

        buttonBack = tk.Button(self.frame1, text='Tela anterior',
                               command=self.showFrame3)
        buttonBack.pack(side='right')

    def createFrame2(self):
        self.frame2 = tk.Frame(self.container)

        label = tk.Label(self.frame2, text='Página 2')
        label.pack(side='top')

        buttonMsg = tk.Button(self.frame2, text='Aviso',
                              command=self.showWarning)
        buttonMsg.pack(side='top')

        buttonNext = tk.Button(self.frame2, text='Próxima tela',
                               command=self.showFrame3)
        buttonNext.pack(side='right')

        buttonBack = tk.Button(self.frame2, text='Tela anterior',
                               command=self.showFrame1)
        buttonBack.pack(side='right')

    def createFrame3(self):
        self.frame3 = tk.Frame(self.container)

        label = tk.Label(self.frame3, text='Página 3')
        label.pack(side='top')

        buttonMsg = tk.Button(self.frame3, text='Erro',
                              command=self.showError)
        buttonMsg.pack(side='top')

        buttonNext = tk.Button(self.frame3, text='Próxima tela',
                               command=self.showFrame1)
        buttonNext.pack(side='right')

        buttonBack = tk.Button(self.frame3, text='Tela anterior',
                               command=self.showFrame2)
        buttonBack.pack(side='right')


View()
