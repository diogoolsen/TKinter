# Importar o módulo TKinter
import tkinter


class View():
    """
    Classe View - Responsável pela construção e apresentação da interface gráfica
    """

    def __init__(self):
        # Inicializar o gerenciador de Janelas
        self.root = tkinter.Tk()

        # loop principal
        # 
        # Operação BLOQUEANTE
        self.root.mainloop()


Janela = View()
