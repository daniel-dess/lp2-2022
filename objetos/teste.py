from cliente import Cliente
from conta import Conta

cli1 = Cliente('Fulano', 'Silva', '99999999999')
c1 = Conta(1, cli1, 1000, 200) #Criando uma instância da classe Conta
#Conta c3 = new Conta(3, 'Beltrano', 200, 100) #Java
print(c1)
if c1.sacar(500):
    print('Saque realizado com sucesso')
else:
    print('Vá trabalhar')
print(c1.numero)
print(c1.titular)
print(c1.saldo)
print(c1.limite)

c2 = Conta(2, 'Cicrano', 0, 200) #o init precisa de 4 argumentos
c1.transfere(c2, 500)
#c2.numero = 2
#print(c1.saldo)
print(c2.saldo)

c3 = c2 #A referencia c3 aponta para o mesmo endereço de c2

print(c3.saldo)

c4 = Conta(3, 'Limite Padrão', 200, 600)
print(c4.limite)

print(c1.__str__())

print('Extrato do cliente')
print(c1.extrato())

#Como melhorar a impressão do histórico?