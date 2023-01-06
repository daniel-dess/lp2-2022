class Historico:
    def __init__(self):
        self.transacoes = []

    def imprime(self):
        for i in self.transacoes:
            print(i)