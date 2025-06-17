X = []

print("Digite 10 números inteiros:")
for i in range(10):
    numero = int(input(f"Número {i+1}: "))
    X.append(numero)

p = int(input("Digite um numero para pesquisar no vetor: "))

posicoes = []
o = 0

for i in range(len(X)):
    if X[i] == p:
        posicoes.append(i)
        o += 1

if o > 0:
    print(f"O numero {p} foi encontrado nas posições: {posicoes}")
    print(f"Total de ocorrências: {o}")
else:
    print(f"O numero {p} não foi encontrado no vetor.")