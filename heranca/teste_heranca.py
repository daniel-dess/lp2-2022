from heranca.controle import ControleBonificacao
from heranca.estagiario import Estagiario
from heranca.funcionario import Funcionario
from heranca.gerente import Gerente
from heranca.presidente import Presidente

f1 = Funcionario('Fulano', 99999999999, 1000)
g1 = Gerente('Gerente', 11111111111, 10000, '123456', 10)
p1 = Presidente('Presidente', 0000000000, 20000)
e1 = Estagiario()
#print(dir(p1))
#print(dir(g1))
print(f1.get_bonifica())
print(g1.get_bonifica())
print(p1.get_bonifica())
bonifica_natal = ControleBonificacao()
bonifica_natal.registra(f1)
bonifica_natal.registra(g1)
bonifica_natal.registra(p1)
bonifica_natal.registra(e1)
print(bonifica_natal.total)
