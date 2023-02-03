class Banco:

    def __init__(self, num, nome_banco):
        self._num = num
        self._nome_banco = nome_banco
        self._lista_contas = []

    def listar_contas(self):
        for i in self._lista_contas:
            print(i)
            i.extrato()

    def incluir_conta(self, conta):
        self._lista_contas.append(conta)

    def remover_conta(self, conta):
        self._lista_contas.remove(conta)


