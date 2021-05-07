

class Model():

    def __init__(self):
        self.data = ''

    def salvar(self, data):
        self.data = self.data + '\n' + data

    def getData(self):
        return self.data
