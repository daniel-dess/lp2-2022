from atividade_encapsulamento.banco import Banco
from atividade_encapsulamento.conta import Conta
from atividade_encapsulamento.emprestimo import Emprestimo

bb = Banco(1,'Banco do Brasil')
c1 = Conta(1,'Fulano', 1000)
c2 = Conta(2,'Ciclano', 2000)
bb.incluir_conta(c1)
bb.incluir_conta(c2)
#bb.listar_contas()
#bb.remover_conta(c2)
#print('Lista após a remoção da conta 2')
#c1.depositar(100)
#c1.sacar(500)
#c2.sacar(2000)
#c2.encerrar_conta()
#c1.transfere(c2, 500)
#bb.listar_contas()
emprestimo = Emprestimo(10000,10,25,c2)
for i in range(10):
    emprestimo.pagar_parcela()

