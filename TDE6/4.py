import random

# Criar matriz 5x5
nlinha = 5
ncoluna = 5
Matriz = []

for i in range(nlinha):
    linhas = []
    for C in range(ncoluna):
        linhas.append(random.randint(10, 99))
    Matriz.append(linhas)

# matrz 1
print("\nMatriz original:")
for linha in range(nlinha):
    for coluna in range(ncoluna):
        print(f"{Matriz[linha][coluna]:2}", end=' ')
    print()

#matriz 2
print("\nFigura a) Cruz central:")
soma_a = 0
for i in range(nlinha):
    for j in range(ncoluna):
        if i == 2 or j == 2:
            print(f"{Matriz[i][j]:2}", end=' ')
            soma_a += Matriz[i][j]
        else:
            print("  ", end=' ')
    print()
print(f"Soma dos valores (a): {soma_a}")

# matriz 3
print("\nFigura b) Moldura:")
soma_b = 0
for i in range(nlinha):
    for j in range(ncoluna):
        if i == 0 or i == nlinha-1 or j == 0 or j == ncoluna-1:
            print(f"{Matriz[i][j]:2}", end=' ')
            soma_b += Matriz[i][j]
        else:
            print("  ", end=' ')
    print()
print(f"Soma dos valores (b): {soma_b}")

#matriz 4
print("\nFigura c) Diagonais:")
soma_c = 0
for i in range(nlinha):
    for j in range(ncoluna):
        if i == j or i + j == nlinha - 1:
            print(f"{Matriz[i][j]:2}", end=' ')
            soma_c += Matriz[i][j]
        else:
            print("  ", end=' ')
    print()
print(f"Soma dos valores (c): {soma_c}")

#matriz 4
print("\nFigura d) Xadrez:")
soma_d = 0
for i in range(nlinha):
    for j in range(ncoluna):
        if (i + j) % 2 == 0:
            print(f"{Matriz[i][j]:2}", end=' ')
            soma_d += Matriz[i][j]
        else:
            print("  ", end=' ')
    print()
print(f"Soma dos valores (d): {soma_d}")
