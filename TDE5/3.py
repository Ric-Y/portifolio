num = input('digite aqui 3 numeros:')

Numeros = list(map(int, num.split())) # o list vai criar a lista, o map vai pegar tudo do input o int vai ver se é numero e o split vai transformar tudo em string ou "".
P = Numeros[1]+Numeros[2]

if Numeros[0] < P:
    print('o primeiro numero é menor q a soma do segundo e do terceiro')
elif Numeros[0] > P:
    print('o primeiro numero é maior q a soma do segundo e do terceiro')
else:
    print('o primeiro numero é igual a soma do segundo e do terceiro')