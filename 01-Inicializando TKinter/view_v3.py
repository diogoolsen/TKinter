import sys
import tkinter


class View():

    def __init__(self):
        self.root = tkinter.Tk()

        self.topContainer = tkinter.Frame(self.root)
        self.topContainer.pack()

        self.bottomContainer = tkinter.Frame(self.root)
        self.bottomContainer.pack()

        self.containerRecebeDados(self.topContainer)
        self.containerExibeDados(self.bottomContainer)

        # Adiciona um evento ao botão esc
        self.root.bind('<Escape>', self.close)

        # Operação Bloqueante
        self.root.mainloop()

    def containerRecebeDados(self, container):
        self.labelNome = tkinter.Label(container, width=20, text="Nome:")
        self.labelNome.pack()

        self.entryNome = tkinter.Entry(container, width=20)
        self.entryNome.pack()

        self.buttonExibir = tkinter.Button(container,
                                           width=20,
                                           text='Exibir')
        # Associa o botão à função exibirDados
        # Não use '()'
        self.buttonExibir["command"] = self.exibirDados
        self.buttonExibir.pack()

    def containerExibeDados(self, container):
        self.labelResposta = tkinter.Label(container,
                                           width=20,
                                           text="Qual seu nome?")
        self.labelResposta.pack()

        self.buttonLimpar = tkinter.Button(container,
                                           width=20,
                                           text='Limpar')
        self.buttonLimpar["command"] = self.limparDados
        self.buttonLimpar.pack()

    # Função que irá tratar o clique no botão Exibir
    def exibirDados(self):
        nome = self.entryNome.get()
        self.labelResposta['text'] = self.labelResposta['text'] +\
            '\n' + nome + '\nSeja bem vindo!\n'

    # Função que irá tratar o clique no botão Limpar
    def limparDados(self):
        self.labelResposta['text'] = ''

    # Função que trata o esc
    def close(self, evento):
        sys.exit()


Janela = View()
# Nada será executado após esta linha
