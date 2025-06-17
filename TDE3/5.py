O = int(input('de 1 à N, quantos numeros voce quer verificar?'))

for m in range(1, O+1):
    if m % 2 != 0:
        print(m)