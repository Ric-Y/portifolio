Matriz = []

MaioresValoresDaMatriz = []

nlinha = int(input('numero de linhas da matriz:'))
ncoluna = int(input('numero de colunas da matriz:'))


for i in range(nlinha):
    linhas = []
    for C in range(ncoluna):
        linhas.append(int(input('Qual numero voce deseja colocar?')))
    Matriz.append(linhas)

for linha in range(nlinha):
    for coluna in range(ncoluna):
        print(Matriz[linha][coluna],end=' ')
    print('')
    print('')

for linha in Matriz:
    F = max(linha)
    MaioresValoresDaMatriz.append(F)
print('os maiores valores por linha são: ',MaioresValoresDaMatriz)
print('')