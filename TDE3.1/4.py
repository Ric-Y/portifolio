def calcular_potencia(base, expoente):
    resultado = 1

    if expoente >= 0:
        for _ in range(expoente):
            resultado *= base
    else:
        if base == 0:
            raise ValueError("Erro.")
        for _ in range(-expoente):
            resultado *= base
        resultado = 1 / resultado

    return resultado




try:
    base = float(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))

    potencia = calcular_potencia(base, expoente)

    print(f"{base} elevado a {expoente} é igual a {potencia}.")
except ValueError as e:
    print("Entrada invalida:", e)
