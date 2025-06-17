n = int(input("Digite o numero de termos que deseja ver na série: "))

soma = 0

print("A série formada é:")
for i in range(1, n + 1):
    denominador = 2 * i - 1
    termo = i / denominador
    soma = soma + termo
    if i < n:
        print(f"{i}/{denominador} + ", end="")
    else:
        print(f"{i}/{denominador} = ", end="")
print(soma)
