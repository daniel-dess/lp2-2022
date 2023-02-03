from historico import Historico

class Conta:
    #Atributo de classe
    _total_contas = 0
    #Variável slots para definir os objetos do tipo Conta
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico', '_status']

    #Para definir os atributos precisamos do init
    def __init__(self, n, t, s, l=100): #Variaveis locais
        self._numero = n #Variveis de objeto
        self._titular = t
        self._saldo = s #Atributo privado
        self._limite = l
        self._historico = Historico()
        Conta._total_contas += 1 #Incrementa o total
        self._status = True

    #Função para encerrar a conta
    def encerrar_conta(self):
        if self._saldo == 0:
            self._status = False
        elif self._saldo > 0:
            print(f'Vc pode sacar {self._saldo}')
        else:
            print(f'Vc precisa depositar {self._saldo}')

    #Método get para o status das contas
    @property
    def status(self):
        return self._status

    #Métodos de acesso
    #Acesso para o atributo de classe
    #@staticmethod #Primeira forma
    @classmethod #Segunda forma
    def get_total_contas(cls):
        return Conta._total_contas

    @property #Método getter
    def saldo(self):
        return self._saldo

    @property #Método getter
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        self._limite = valor

    def get_numero(self): #Método getter
        return self._numero

    #Não faz sentido um set para o saldo, pois já temos sacar e depositar

    #Comportamentos
    def sacar(self, valor):
        if self.status:
            if self._saldo < valor:
                return False
            else:
                self._saldo = self._saldo - valor
                self._historico.transacoes.append(f'Saque de {valor}')
                return True
        else:
            print('Conta inativa não pode realizar saques')

    def depositar(self, valor):
        if self.status:
            self._saldo += valor
            self._historico.transacoes.append(f'Depósito de {valor}')
        else:
            print('Conta inativa não pode realizar depósitos')

    #Como fazer uma transferência de uma conta para outra?
    def transfere(self, c_destino, valor):
        if self.status and c_destino.status:
            self.sacar(valor)
            c_destino.depositar(valor)
            self._historico.transacoes.append(f'Tranferência de {valor}')
        else:
            print('Conta inativa não pode realizar transferências')

    def extrato(self):
        self._historico.imprime()

    def __str__(self):
        return f'{self.__class__.__name__} {self._numero}: {self._titular} Saldo:{self._saldo}'
