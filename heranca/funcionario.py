class Funcionario:
    def __init__(self, nome, cpf, salario, idade):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._idade = idade

    def get_bonifica(self):
        return self._salario * 0.1