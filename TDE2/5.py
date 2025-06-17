# Algoritmo para calcular o custo das fotocópias
numeroCopias = int(input("digite o numero de cópias: "))

if numeroCopias < 100:
    valorTotal = numeroCopias * 0.25
else:
    valorTotal = numeroCopias * 0.20

print(f"O valor total a pagar é: R$ {valorTotal}")