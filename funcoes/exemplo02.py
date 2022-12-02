def soma(*args): #args é uma tupla
    r = 0
    for num in args:
        r += num
    return r
    #print(f"A soma de x e y é: {x+y}")

print(soma())
print(soma(6,7,9,4,3,3))