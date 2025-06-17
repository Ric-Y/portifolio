MILHA = 1609.344

print("Tabela de Conversão de Metros para Milhas")
print("{:<10} {:<10}".format("Km", "Milhas"))

for km in range(20, 161, 10):
    metros = km * 1000
    milhas = metros / MILHA
    print("{:<10} {:.2f}".format(km, milhas))
