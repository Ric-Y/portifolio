numeros = []
soma = 0
print("Digite 10 números inteiros:")
for _ in range(10):
    numero = int(input("Número: "))
    numeros.append(numero)
    soma += numero

media = soma / len(numeros)
print(f"\nSoma dos números: {soma}")
print(f"Média aritmética: {media:.2f}")
