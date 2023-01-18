from conta import Conta
conta1 = Conta(1, 'Cliente 1', 100)
conta2 = Conta(2, 'Cliente 2', 100)


#print(f'Total de Contas: {conta1.total_contas}')
#print(f'Total de Contas: {Conta._total_contas}')
print(conta1.get_numero())
print(conta2.get_numero())
#Conta._total_contas = 4 #Forma errada de acessar
#print(f'Total de Contas: {conta2.total_contas}')
#print(f'Total de Contas: {Conta._total_contas}')
#print(conta1.get_total_contas()) #Forma incorreta de acessar o método de classe
print(Conta.get_total_contas())
print(vars(conta1))
conta1.pix = '9999999999'
print(vars(conta1))
#print(conta1.pix)
