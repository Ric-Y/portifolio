# Criando uma lista para armazenar as matrizes
matrizes = []

for u in range(2):
    Matriz = []

    nlinha = int(input(f'Número de linhas da matriz {u + 1}: '))
    ncoluna = int(input(f'Número de colunas da matriz {u + 1}: '))

    for i in range(nlinha):
        linhas = []
        for C in range(ncoluna):
            linhas.append(int(input(f'Qual número você deseja colocar na posição [{i+1}][{C+1}]? ')))
        Matriz.append(linhas)

    # Exibindo a matriz criada
    print(f'\nMatriz {u + 1}:')
    for linha in Matriz:
        print(linha)

    matrizes.append(Matriz)


# Multiplicação de matrizes
def multiplicar(matrizA, matrizB):
    if len(matrizA[0]) != len(matrizB):
        print("Erro: O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
        return None

    resultado = [[0] * len(matrizB[0]) for _ in range(len(matrizA))]

    for i in range(len(matrizA)):
        for j in range(len(matrizB[0])):
            for k in range(len(matrizB)):
                resultado[i][j] += matrizA[i][k] * matrizB[k][j]

    return resultado


matrizA, matrizB = matrizes
resultado = multiplicar(matrizA, matrizB)
if resultado:
    print("\nMatriz Resultante:")
    for linha in resultado:
        print(linha)