X = input('coloque 10 numeros aqui:')
Vlidos = list(map(int, X.split()))

if len(Vlidos) == 10:
    Vpares = [y for y in Vlidos if y % 2 == 0]
    Vimpares = [y for y in Vlidos if y % 2 != 0]


    print('Lista pricipal: ', Vlidos)
    print('lista apenas com os pares: ', Vpares)
    print('lista apenas com os impares: ', Vimpares)

else:
    print('erro')