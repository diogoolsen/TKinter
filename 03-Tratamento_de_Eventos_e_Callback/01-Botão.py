import sys
import tkinter as tk


class View():
    def __init__(self):
        self.root = tk.Tk()

        # Usa a opção command para associar uma função à ativação do widget
        self.button01 = tk.Button(self.root,
                                  width=20,
                                  text='Botão01',
                                  command=self.tratarBotao01Clicado)
        self.button01.pack()

        self.button02 = tk.Button(self.root,
                                  width=20,
                                  text='Botão02',
                                  command=self.tratarBotao02Clicado)
        self.button02.pack()
        # Associando eventos ao button02 e às funções de tratamento
        # formato:
        # widget.bind(stringDoEvento, funçãoParaTratamento)

        # Pode ter mais de um evento associado a um widget
        self.button02.bind('<Button-1>', self.tratarBotao02ClicadoBotao01)
        self.button02.bind('<Button-2>', self.tratarBotao02ClicadoBotao02)
        self.button02.bind('<Button-3>', self.tratarBotao02ClicadoBotao03)

        # E o mesmo widget pode estar associado ao mesmo evento com duas
        # ou mais funções diferentes
        self.button02.bind('<ButtonRelease-1>',
                           self.tratarBotao02ClicadoBotao01Liberado)
        self.button02.bind('<ButtonRelease-1>',
                           self.tratarBotao02ClicadoBotao01LiberadoV2)

        # Este evento escuta o botão esc para toda a plicação, pois
        # está associado ao root
        self.root.bind('<Escape>', self.close)

        self.root.mainloop()

    def tratarBotao02ClicadoBotao01LiberadoV2(self, event):
        print('Botao 02 liberado pelo botão esquerdo V2')

    def tratarBotao02ClicadoBotao01Liberado(self, event):
        print('Botao 02 liberado pelo botão esquerdo')

    def tratarBotao02ClicadoBotao01(self, event):
        print('Botao 02 clicado pelo botão esquerdo')

    def tratarBotao02ClicadoBotao02(self, event):
        print('Botao 02 clicado pelo botão do meio')

    def tratarBotao02ClicadoBotao03(self, event):
        print('Botao 02 clicado pelo botão direito')

    def tratarBotao02Clicado(self):
        print('Botao 02 clicado')

    def tratarBotao01Clicado(self):
        print('Botao 01 clicado')

    def tratarTextoDigitado(self):
        print('')

    def close(self, evento=None):
        sys.exit()


View()
