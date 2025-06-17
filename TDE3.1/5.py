def calcular(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

try:
    numero = int(input("Digite um número inteiro: "))
    if numero < 0:
        print("Erro.")
    else:
        fatorial = calcular(numero)
        print(f"{numero}! = {fatorial}")
except ValueError:
    print("Erro.")
