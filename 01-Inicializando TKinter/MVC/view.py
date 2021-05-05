from model import Model
from controller import Controller

import sys
import tkinter


class View():

    def __init__(self):
        self.model = Model()
        self.controller = Controller(self, self.model)

        self.root = tkinter.Tk()

        self.topContainer = tkinter.Frame(self.root)
        self.topContainer.pack()

        self.bottomContainer = tkinter.Frame(self.root)
        self.bottomContainer.pack()

        self.containerRecebeDados(self.topContainer)
        self.containerExibeDados(self.topContainer)

        self.root.bind('<Escape>', self.close)

        self.root.mainloop()

    def containerRecebeDados(self, container):
        self.labelNome = tkinter.Label(container, width=20, text="Nome:")
        self.labelNome.pack()

        self.entryNome = tkinter.Entry(container, width=20)
        self.entryNome.pack()

        self.buttonSalvar = tkinter.Button(container,
                                           width=20,
                                           text='Salvar',
                                           command=self.salvarDados)
        self.buttonSalvar.pack()

    def containerExibeDados(self, container):
        self.labelResposta = tkinter.Label(container,
                                           width=20,
                                           text='')
        self.labelResposta.pack()

        self.buttonExibir = tkinter.Button(container,
                                           width=20,
                                           text='Exibir',
                                           command=self.pedirDados)
        self.buttonExibir.pack()

    def salvarDados(self):
        nome = self.entryNome.get()
        self.controller.salvar(nome)

    def pedirDados(self):
        self.controller.retornar()

    def exibirDados(self, data):
        self.labelResposta['text'] = data

    def close(self, evento):
        sys.exit()


Janela = View()
