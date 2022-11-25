class MinhaExcecaoError(Exception):     #Classe para definir uma exceção
    pass

while True:                             #loop que mantem o programa em execução
    n = input('Entre com o número:')
    try:
        n = int(n)                      #int() pode lançar a exceção ValueError
        if n > 35:                      #if pode lançar a exceção MinhaExcecaoError
            raise MinhaExcecaoError()
        n = 5 / n                       #/ pode lançar a exceção ZeroDivisionError
    except MinhaExcecaoError:
        print('O valor não pode ser maior que 35')
    except ValueError as erro:
        #print(str(erro))               #imprime o erro original da exceção
        print('Entrada inválida! Tente Novamente...')
    except ZeroDivisionError as erro:
        print('Não existe divisão por zero.')
    except Exception:                   #Evitar usar a exceção geral, mas pode ser usada no final das cláusulas except
        print('Erro geral.')
    else:                               #Cláusula else só executa caso nenhuma exceção seja lançada
        print(f'Resultado: {n}')
        print('Fim do programa.')
        break
