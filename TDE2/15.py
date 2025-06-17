numero1 = int(input("Digite o primeiro numero inteiro: "))
numero2 = int(input("Digite o segundo numero inteiro: "))
numero3 = int(input("Digite o terceiro numero inteiro: "))

numeros = [numero1, numero2, numero3]

numeros.sort(reverse=True)

print("Os numeros em ordem decrescente são:", numeros)