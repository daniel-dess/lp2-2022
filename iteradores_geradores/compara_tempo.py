import time

def loop(n):
    lista = []
    for i in range(n):
        if i % 2 == 0:
            lista.append(i*i)
        else:
            lista.append(i)
    return lista

def listc(n):
    return [i*i if i % 2 == 0 else i for i in range(n)]
ini = time.time()
loop(10**8)
fim = time.time()
print(f'Tempo do loop: {fim-ini}')
ini = time.time()
listc(10**8)
fim = time.time()
print(f'Tempo do list-comprehension: {fim-ini}')