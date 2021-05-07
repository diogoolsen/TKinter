

class Controller():

    def __init__(self, view, model):
        self.view = view
        self.model = model

    def salvar(self, data):
        self.model.salvar(data)

    def retornar(self):
        data = self.model.getData()
        self.view.exibirDados(data)
