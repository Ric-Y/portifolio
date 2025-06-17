def classificar(idade):
    if 5 <= idade <= 7:
        return "Infantil A"
    elif 8 <= idade <= 10:
        return "Infantil B"
    elif 11 <= idade <= 13:
        return "Juvenil A"
    elif 14 <= idade <= 17:
        return "Juvenil B"
    elif idade >= 18:
        return "Adulto"
    else:
        return "Erro"


idade = int(input("Digite a idade do nadador: "))
categoria = classificar(idade)
print(f"A categoria do nadador é: {categoria}")