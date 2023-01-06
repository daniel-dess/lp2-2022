from historico import Historico

class Conta:
    #Para definir os atributos precisamos di init
    def __init__(self, n, t, s, l=100): #Variaveis locais
        self.numero = n #Variveis de objeto
        self.titular = t
        self.saldo = s
        self.limite = l
        self.historico = Historico()

    #Comportamentos
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo = self.saldo - valor
            self.historico.transacoes.append(f'Saque de {valor}')
            return True

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f'Depósito de {valor}')

    #Como fazer uma transferência de uma conta para outra?
    def transfere(self, c_destino, valor):
        self.sacar(valor)
        c_destino.depositar(valor)
        self.historico.transacoes.append(f'Tranferência de {valor}')

    def extrato(self):
        self.historico.imprime()

    def __str__(self):
        return f'{self.__class__.__name__} {self.numero}: {self.titular} Saldo:{self.saldo}'
