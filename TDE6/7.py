cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília"]
distancias = [
    [0, 429, 586, 1015],
    [429, 0, 438, 1148],
    [586, 438, 0, 716],
    [1015, 1148, 716, 0]
]

cidade_nova = input("Nova cidade: ")
cidades.append(cidade_nova)

nova_distancia = []
for cidade in cidades[:-1]:
    distancia = int(input(f"Distância de {cidade_nova} para {cidade}: "))
    nova_distancia.append(distancia)

nova_distancia.append(0)
distancias.append(nova_distancia)
for i in range(len(distancias) - 1):
    distancias[i].append(nova_distancia[i])

print("\nLista:", cidades)
print("Matriz:")
for linha in distancias:
    print(linha)


origem = input("cidade de origem ")
destino = input("cidade de destino: ")
velocidade = float(input("a velocidade média do veículo (km/h): "))

if origem in cidades and destino in cidades:
    i = cidades.index(origem)
    j = cidades.index(destino)
    distancia = distancias[i][j]
    tempo = distancia / velocidade
    print(f"O tempo estimado de viagem entre {origem} e {destino} é de {tempo:.2f} horas.")
else:
    print("Erro")