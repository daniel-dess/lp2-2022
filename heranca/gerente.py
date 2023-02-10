from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtde):
        #Funcionario.__init__(self, nome, cpf, salario)
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtde = qtde

    def autentica(self, senha):
        if self._senha == senha:
            return True
        else:
            return False

    def get_bonifica(self):
        return super().get_bonifica() + 1100