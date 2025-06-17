X = input('coloque 10 numeros aqui:')
Vlidos = list(map(int, X.split()))

if len(Vlidos) == 10 and len(Vlidos) > 0:
    Vpares = [y for y in Vlidos if y % 2 == 0]
    Vimpares = [y for y in Vlidos if y % 2 != 0]

    print('lista desordenada: ', Vlidos)
    print('lista ordenada por Pares e Impares: ', Vpares, Vimpares)



else:
    print('erro')