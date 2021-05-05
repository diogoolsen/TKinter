import tkinter


class View():

    def __init__(self):
        self.root = tkinter.Tk()

        # Insere dois containers para inserir componentes

        # Cria o objeto do tipo Frame
        self.topContainer = tkinter.Frame(self.root)
        # Adiciona ele à GUI
        self.topContainer.pack()

        self.bottomContainer = tkinter.Frame(self.root)
        self.bottomContainer.pack()

        # Adiciona os componentes AO container
        self.containerRecebeDados(self.topContainer)
        self.containerExibeDados(self.topContainer)

        self.root.mainloop()

    def containerRecebeDados(self, container):
        # Insere um label NO CONTAINER indicado
        self.labelNome = tkinter.Label(container, width=20, text="Nome:")
        self.labelNome.pack()

        # Insere um campo de texto
        self.entryNome = tkinter.Entry(container, width=20)
        self.entryNome.pack()

        # Insere um botão (ainda sem função)
        self.buttonExibir = tkinter.Button(container,
                                           width=20,
                                           text='Exibir')
        self.buttonExibir.pack()

    def containerExibeDados(self, container):
        self.labelResposta = tkinter.Label(container,
                                           width=20,
                                           text="Qual seu nome?")
        self.labelResposta.pack()

        self.buttonLimpar = tkinter.Button(container,
                                           width=20,
                                           text='Limpar')
        self.buttonLimpar.pack()


Janela = View()
