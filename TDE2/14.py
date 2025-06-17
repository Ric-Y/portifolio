# Leitura dos três números inteiros
n1 = int(input("Digite o primeiro numero inteiro: "))
n2 = int(input("Digite o segundo numero inteiro: "))
n3 = int(input("Digite o terceiro numero inteiro: "))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print("O maior numero é:", maior)