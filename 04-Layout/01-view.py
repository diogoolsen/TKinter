import sys
import tkinter as tk


class View():
    def __init__(self):
        self.root = tk.Tk()

        # Cria um primeiro frame e posiciona ele na janela
        self.topframe = tk.Frame(self.root)
        self.topframe.pack()

        # Cria um segundo frame e posiciona ele na janela, abaixo do primeiro
        self.bottomframe = tk.Frame(self.root)
        self.bottomframe.pack(side=tk.BOTTOM)

        # Cria um botão e o posiciona no primeiro frame
        self.button_01 = tk.Button(self.topframe, text="01")
        self.button_01.pack(side=tk.LEFT)

        # Cria outro botão e o empilha à esquerda do primeiro
        self.button_02 = tk.Button(self.topframe, text="02")
        self.button_02.pack(side=tk.LEFT)

        # Cria outro botão e o empilha à esquerda dos anteriores
        self.button_03 = tk.Button(self.topframe, text="03")
        self.button_03.pack(side=tk.LEFT)

        #
        # Este botão não fica à esquerda, pois está em outro frame
        # O Frame bottomframe está posicionado abaixo do bottomframe
        #
        self.button_04 = tk.Button(self.bottomframe, text="04")
        self.button_04.pack(side=tk.LEFT)

        self.root.bind('<Escape>', self.close)

        self.root.mainloop()

    def close(self, evento=None):
        sys.exit()


View()
