I = int(input('Polegada(1-20) para Cm:'))
if 1 <= I <= 20:
    print(f"A medida em Cm de {I} Polegadas, é igual á {I*2.54}")
else:
    print('o numero não está dentro das especificações')