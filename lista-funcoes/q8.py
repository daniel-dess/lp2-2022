frase = "Ainda bem que deu ruim antes da Argentina"
lista = frase.split()
vogais = ['a','e','i','o','u']
print(list(map(lambda x: (len(x), len([i for i in x if i.lower() in vogais])), lista)))