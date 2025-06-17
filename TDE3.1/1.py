X = int(input('Quantos numeros quer verificar?'))
O = 0
Soma_Total = 0
Soma_Par = 0
Soma_Impar = 0
while O < X:
    C = int(input('Seu numero:'))
    O += 1
    Soma_Total = C + Soma_Total
    if C % 2 == 0:
        Soma_Par = Soma_Par + C
    else:
        Soma_Impar = Soma_Impar + C

print(f"Soma total: {Soma_Total}, Soma dos N pares: {Soma_Par} e Soma dos N impares: {Soma_Impar}")