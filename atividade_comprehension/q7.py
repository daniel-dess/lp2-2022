import random
#[(1,76),(2,'par'),(3,23),...,(100,'par')]
lista = [(i, 'par' if i%2==0 else random.randint(0,100)) for i in range(1, 101)]
print(lista)

