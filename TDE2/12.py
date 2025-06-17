def classificar(peso):
    if peso >= 201:
        return "Peso-pesado"
    elif 176 <= peso < 200:
        return "Cruzador"
    elif 169 <= peso < 175:
        return "Peso-médio"
    elif 161 <= peso < 168:
        return "Super-médio"
    elif 0 < peso < 160:
        return "Categoria inferior a super-médio"
    else:
        return "erro"

Kg = float(input('Qual seu peso em Kg?'))
peso = Kg * 2.20462262

print(f"O boxeador esta na categoria {classificar(peso)}")