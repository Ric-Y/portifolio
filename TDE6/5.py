Matriz = []
import random


nlinha = int(input('numero de linhas da matriz:'))
ncoluna = int(input('numero de colunas da matriz:'))

for i in range(nlinha):

    linhas = []
    for C in range(ncoluna):
        linhas.append(random.randint(1, 100, ))
    Matriz.append(linhas)


for linha in range(nlinha):
    for coluna in range(ncoluna):
        print(Matriz[linha][coluna],end=' ')
    print('')


todos_numeros = [valor for linha in Matriz for valor in linha]

pares = [num for num in todos_numeros if num % 2 == 0]
impares = [num for num in todos_numeros if num % 2 != 0]

ordenados = pares + impares

print("\nMatriz modificada (pares primeiro, depois ímpares):")
for linha in Matriz:
    for valor in linha:
        print(valor, end=' ')
    print()
