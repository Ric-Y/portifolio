Hora = float(input('quanto tempo o carro ficou estacionado em H?'))

if Hora  >= 1:
    print((Hora*1.5)+8, 'reais a pagar')
if Hora >= 0:
    print('erro')
else:
    print('8 Reais a pagar')