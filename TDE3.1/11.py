N = int(input("Qual o numero de termos para o valor de H: "))
H = 0.0
for i in range(1, N + 1):
    H += 1 / i
print(f"O valor de H com {N} termos é: {H:.4f}")
