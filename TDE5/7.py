x = input('digite seus numeros')
try: #try verifica se nn tem erro no código (nesse caso no input do usuario), se tiver o except é ativado
    lista = list(map(int, x.split()))
    lista.sort()
    if len(lista) > 1:
        P = lista[-1] - lista[0]
        print(f'sua amplitude amostral é {P}')
except ValueError:
    print('erro')