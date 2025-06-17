def classficar(imc):
    if 18.5 > imc:
        return "Abaixo do peso"
    elif 18.5 >= imc < 25:
        return "Peso normal"
    elif 25 >= imc < 30:
        return "Acima do peso"
    elif imc > 30:
        return "Obeso"
    else:
        return "erro"

massa = float(input("Digite sua massa em Kg: "))
altura = float(input("Digite sua altura em M: "))
imc = massa / (altura ** 2)
print(f"Seu IMC é {imc} e sua classificação na OMS é {classficar(imc)}")