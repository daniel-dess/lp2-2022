def pessoas_idade(**kwargs): #kwargs é um dicionário
    for chave, valor in kwargs.items():
        print(f'chave:valor -> {chave}:{valor}')

pessoas_idade(maria=30,carlos=23,joão=19)