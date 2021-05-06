import sys
import tkinter as tk
from tkinter import ttk


def donothing():
    pass


class View():
    def __init__(self):
        self.root = tk.Tk()

        self.menu()
        self.autoria()
        self.genero()
        self.formato()
        self.emprestimo()

        self.root.bind('<Escape>', self.close)

        self.root.mainloop()

    def menu(self):
        # Cria o menu principal
        menubar = tk.Menu(self.root)
        # Associa o menu à janela raiz
        self.root.config(menu=menubar)

        # Cria os menus Arquivo e Ajuda
        fileMenu = tk.Menu(menubar, tearoff=0)
        helpMenu = tk.Menu(menubar, tearoff=0)

        # Insere os menus no estilo cascata ao menu principal
        menubar.add_cascade(label='Arquivo', menu=fileMenu)
        menubar.add_cascade(label='Ajuda', menu=helpMenu)

        # Configura o menu Arquivo inserindo o comando Novo
        fileMenu.add_command(label='Novo', command=self.novo)
        fileMenu.add_separator()

        # Cria outro menu, dentro do menu Arquivo
        # Cria o menu
        salvarMenu = tk.Menu(menubar, tearoff=0)

        # Insere o menu Salvar em Arquivo
        fileMenu.add_cascade(label='Salvar', menu=salvarMenu)

        # Insere os comando Salvar e Salvar Como
        salvarMenu.add_command(label='Salvar', command=donothing)
        salvarMenu.add_command(label='Salvar Como', command=donothing)

        # Adiciona um separador
        fileMenu.add_separator()

        # Insere os comandos Relatório e Sair
        fileMenu.add_command(label='Relatório', command=self.relatorio)
        fileMenu.add_command(label='Sair', command=self.close)

        # No menu Ajuda, insere os comandos ajuda e sobre
        helpMenu.add_command(label='Ajuda', command=donothing)
        helpMenu.add_command(label='Sobre', command=donothing)

    def autoria(self):
        container = tk.Frame(self.root)
        container.pack()

        labelTitulo = tk.Label(container, width=20, text='Título:')
        # Grid posiciona os componentes como uma tabela, organizados por
        # linhas e colunas
        labelTitulo.grid(column=0, row=0, padx=5, pady=5)

        self.entryTitulo = tk.Entry(container, width=20)
        self.entryTitulo.grid(column=1, row=0, padx=5, pady=5)

        labelAutor = tk.Label(container, width=20, text='Autor:')
        labelAutor.grid(column=0, row=1, padx=5, pady=5)

        self.entryAutor = tk.Entry(container, width=20)
        self.entryAutor.grid(column=1, row=1, padx=5, pady=5)

    def genero(self):
        container = tk.Frame(self.root)
        container.pack()

        labelGenero = tk.Label(container, width=20, text='Genero:')
        labelGenero.grid(column=0, row=0, padx=5, pady=5)

        # Cria uma variável para receber o valor do radiobutton
        self.radioValue = tk.StringVar()

        # Cria um radiobutton
        self.radioUm = tk.Radiobutton(container, text='Terror', width=20,
                                      # Associa a variável 'radioValue'
                                      # com a string 'terror'
                                      variable=self.radioValue, value='terror',
                                      # Alinha a esqueda 'WEST'
                                      anchor=tk.W)
        # Insere o botão
        self.radioUm.grid(column=1, row=0, padx=5, pady=5)

        self.radioDois = tk.Radiobutton(container, text='Computação', width=20,
                                        variable=self.radioValue,
                                        value='computação',
                                        anchor=tk.W)
        self.radioDois.grid(column=1, row=1, padx=5, pady=5)

        self.radioTres = tk.Radiobutton(container, text='Biografia', width=20,
                                        variable=self.radioValue,
                                        value='biografia',
                                        anchor=tk.W)
        self.radioTres.grid(column=1, row=2, padx=5, pady=5)

    def formato(self):
        container = tk.Frame(self.root)
        container.pack()

        labelFormato = tk.Label(container, width=20, text='Formato:')
        labelFormato.grid(column=0, row=0, padx=5, pady=5)

        # Cria uma variável para armazenar o valor do botão
        self.capaDura = tk.BooleanVar()
        self.brochura = tk.BooleanVar()
        self.digital = tk.BooleanVar()

        # Cria o botão associado à variavel e alinhado à esquerda
        chkBttn = tk.Checkbutton(container, text='Capa dura', width=20,
                                 variable=self.capaDura, anchor=tk.W)
        # Insere o botão
        chkBttn.grid(column=1, row=0, padx=5, pady=5)

        chkBttn = tk.Checkbutton(container, text='Brochura', width=20,
                                 variable=self.brochura, anchor=tk.W)
        chkBttn.grid(column=1, row=1, padx=5, pady=5)

        chkBttn = tk.Checkbutton(container, text='Digital', width=20,
                                 variable=self.digital, anchor=tk.W)
        chkBttn.grid(column=1, row=2, padx=5, pady=5)

    def emprestimo(self):
        container = tk.Frame(self.root)
        container.pack()

        labelEmprestimo = tk.Label(container, width=20, text='Emprestimo:')
        labelEmprestimo.grid(column=0, row=0, padx=5, pady=5)

        # Cria um combobox com as opções: 'livre, 'local' e 'restrito'
        # Precisa da importação de ttk, que expande o TK
        self.comboEmprestimo = ttk.Combobox(container, width=20,
                                            values=['Livre',
                                                    'Especial',
                                                    'Restrito'])
        self.comboEmprestimo.grid(column=1, row=0, padx=5, pady=5)

        labelEmprestimo = tk.Label(container, width=20, text='Periodo:')
        labelEmprestimo.grid(column=0, row=0, padx=5, pady=5)

        # Cria uma variável para receber o período
        self.periodo = tk.DoubleVar()

        # Cria a escala
        escalaPeriodo = tk.Scale(container, from_=7, to=30, width=20,
                                 length=200, variable=self.periodo,
                                 orient=tk.HORIZONTAL)
        escalaPeriodo.grid(column=1, row=1, padx=5, pady=5)

    def relatorio(self):
        print('Titulo:', self.entryTitulo.get())
        print('Autor:', self.entryAutor.get())
        print('Genero:', self.radioValue.get())
        print('Formatos:')
        print('\tCapa Dura:', self.capaDura.get())
        print('\tBrochura:', self.brochura.get())
        print('\tDigital:', self.digital.get())
        print('Emprestimo:', self.comboEmprestimo.get())
        print('Período:', self.periodo.get())

    def novo(self):
        self.entryTitulo.delete(0, 100)
        self.entryAutor.delete(0, 100)
        self.radioUm.deselect()
        self.radioDois.deselect()
        self.radioTres.deselect()
        self.capaDura.set(False)
        self.brochura.set(False)
        self.digital.set(False)
        self.comboEmprestimo.set('')
        self.periodo.set(0)

        print('Titulo:', self.entryTitulo.get())
        print('Autor:', self.entryAutor.get())
        print('Genero:', self.radioValue.get())
        print('Formatos:')
        print('\tCapa Dura:', self.capaDura.get())
        print('\tBrochura:', self.brochura.get())
        print('\tDigital:', self.digital.get())
        print('Emprestimo:', self.comboEmprestimo.get())
        print('Período:', self.periodo.get())

    def close(self, evento=None):
        sys.exit()


Janela = View()
