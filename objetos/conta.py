from historico import Historico

class Conta:
    #Para definir os atributos precisamos di init
    def __init__(self, n, t, s, l=100): #Variaveis locais
        self._numero = n #Variveis de objeto
        self._titular = t
        self._saldo = s #Atributo privado
        self._limite = l
        self._historico = Historico()

    #Métodos de acesso
    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        self._limite = valor

    def get_numero(self):
        return self._numero

    #Não faz sentido um set para o saldo, pois já temos sacar e depositar

    #Comportamentos
    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self._saldo = self.saldo - valor
            self._historico.transacoes.append(f'Saque de {valor}')
            return True

    def depositar(self, valor):
        self._saldo += valor
        self._historico.transacoes.append(f'Depósito de {valor}')

    #Como fazer uma transferência de uma conta para outra?
    def transfere(self, c_destino, valor):
        self.sacar(valor)
        c_destino.depositar(valor)
        self._historico.transacoes.append(f'Tranferência de {valor}')

    def extrato(self):
        self._historico.imprime()

    def __str__(self):
        return f'{self.__class__.__name__} {self._numero}: {self._titular} Saldo:{self._saldo}'
