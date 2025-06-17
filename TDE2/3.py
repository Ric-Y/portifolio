import math

numero = int(input("Digite um numero inteiro: "))

if numero < 0:
    print("Erro, Numero Negativo")
else:
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")