from functools import reduce

fatura = [('Net', 199.9), ('Ifood', 999.87), ('Gasolina', 678.0), ('Formigão', 400)]

#Tipo de gasto - R$ valor
print([f'{x} - R${y}' for x, y in fatura]) #1ª forma
#print(reduce(lambda x, y: f'{x} - R${y}', reduce(lambda x, y: x+y, fatura))) #Não ficou correto com reduce
lista2 = [(i[0], i[1]) for i in fatura]
for x in lista2: #2ª forma
    print(f'{x[0]} - R${x[1]}')
#Ordenando a fatura pelo valor
fatura.sort(key=lambda x: x[1])
print(fatura)
#Filtrando os valores maiores que 500
print(list(filter(lambda x: x[1] > 500, fatura)))
#Imprimindo o total da fatura
print(reduce(lambda x, y: x+y, [x[1] for x in fatura])) #1ª forma
print(sum([x[1] for x in fatura])) #2ª forma