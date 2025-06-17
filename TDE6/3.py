Matriz = []
import random


nlinha = int(input('numero de linhas da matriz:'))
ncoluna = int(input('numero de colunas da matriz:'))

for i in range(nlinha):

    linhas = []
    for C in range(ncoluna):
        linhas.append(random.randint(100, 1000, ))
    Matriz.append(linhas)


for linha in range(nlinha):
    for coluna in range(ncoluna):
        print(Matriz[linha][coluna],end=' ')
    print('')
