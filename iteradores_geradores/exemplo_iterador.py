lista = [1,2]
estrutura = ('Maria','João','Carlos')
z = zip(lista, estrutura)
print(next(z), next(z))
estrutura_it = enumerate(estrutura)
print(type(estrutura_it))
for j in estrutura_it:
    print(j)
#print(next(estrutura))
iterador = iter(estrutura)
print(type(iterador))
print(estrutura[2])
#print(iterador[2]) #Não podemos acessar posições de um iterador
for i in iterador:
    if i == 'João':
        break
    print(i)
print(next(iterador))

