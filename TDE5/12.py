print("Escreva 20 números:")
lista = []
for X in range(1, 21):
    b = int(input(f"{X}: "))
    lista.append(b)
for i in range(len(lista)):
    menor = i
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[menor]:
            menor = j
    lista[i], lista[menor] = lista[menor], lista[i]
print("Lista ordenada:", lista)