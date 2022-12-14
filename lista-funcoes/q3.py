def inverte(*args, **kwargs):
    for i in range(len(args)-1, -1, -1):
        print(args[i])
    #print(args[::-1])

    # lista = list(kwargs.items())
    # lista.sort(key=lambda x: x[1])
    # lista2 = dict(lista)
    # print(lista2)
    kw_ordenado = sorted(kwargs.items(), key=lambda x: x[0])
    print(kw_ordenado)

inverte(2,'q',[3,4,5],True,(2,3),{'a':2}, teclado=30,mouse=10,a=40)

