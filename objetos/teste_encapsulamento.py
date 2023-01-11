from objetos.cliente import Cliente
from objetos.conta import Conta

cli1 = Cliente('Fulano', 'Silva', '99999999999')
c1 = Conta(1, cli1, 1000, 200) #Criando uma instância da classe Conta

#c1._Conta_saldo = 2900
#print(c1._Conta_saldo)
print(c1.limite)
print(c1.saldo)
c1.limite = 300
print(c1.limite)
c1.sacar(100)
print(c1.saldo)
#print(str(c1))
#print(dir(c1))