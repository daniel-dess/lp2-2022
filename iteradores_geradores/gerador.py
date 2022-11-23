def geradora2():
    return (i*i for i in range(10))

def geradora():
    print("Linha 1")
    yield ""
    print("Linha 2")
    yield 2
    print("Linha 3")
    yield 3

g = geradora2()
print(type(g))
print(next(g))
print(next(g))
for x in g:
    print(x, end=',')