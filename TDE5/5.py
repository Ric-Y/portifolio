x = input('coloque os numeros que deseja verificar:')

Lista = list(map(int, x.split()))
for item in Lista:
    if item % 2 == 0:
        print("é par")
    else:
        print("é impar")