#Soma usando lambda
funcao_soma = lambda x=0,y=0: x+y
print(type(funcao_soma))
print(funcao_soma())
print((lambda x=0,y=0: x+y)(6,7))

soma2 = lambda *valores: sum(valores)
tupla = (1,2,3,4,5,6)
#print(soma2(tupla)) #tupla não é um parâmetro esperado pela função soma2
print(soma2(1,2,4,5,6,7))

d = {'a':10, 'b':11, 'c':12}
f_total = lambda **kwargs:sum(kwargs.values())
print(f_total(a=10, b=11, c=12))

print((lambda x, y: x+y if y>x else 0)(4,2))

nomes = ['maira', 'carlos', 'jose']
converte = lambda x: [i.upper() for i in x]
print(converte(nomes))

a = [1,4,9,16,25]
b = [i**2 for i in a]
print(b)
c = [a[i]+b[i] for i in range(len(a))]
print(c)