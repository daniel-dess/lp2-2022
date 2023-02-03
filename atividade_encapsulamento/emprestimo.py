class Emprestimo:
    _total_emprestimos = 0
    def __init__(self, v, p, j, c):
        self._valor = v
        self._parcelas = p
        self._juros = j
        self._conta = c
        self._saldo_devedor = self._valor + self._valor * (self._juros / 100)
        self._valor_parcela = self._saldo_devedor / self._parcelas
        self._conta.depositar(self._valor)
        self._parcela_atual = 1
        Emprestimo._total_emprestimos += 1

    #Método para acessar o total de Emprestimos
    @classmethod
    def total_emprestimos(cls):
        return cls._total_emprestimos

    #Método para pagar uma parcela
    def pagar_parcela(self):
        if self._conta.sacar(self._valor_parcela):
            self._saldo_devedor -= self._valor_parcela
            self.imprime_situacao()
            self._parcela_atual += 1
        else:
            print('Saldo insuficiente para pagar a parcela')




    def imprime_situacao(self):
        print('=====Situação do Emprestimo=====')
        print(f'Seu saldo é de: {self._conta.saldo}')
        print(f'Parcela {self._parcela_atual} de {self._parcelas}')
        print(f'Valor pago: {self._valor_parcela}')
        print(f'Saldo devedor: {self._saldo_devedor}')
        print('================================')