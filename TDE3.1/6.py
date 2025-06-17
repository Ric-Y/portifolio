def main():
    try:
        n = int(input("Digite o número de pessoas: "))
    except ValueError:
        print("Entrada inválida! Informe um número inteiro para a quantidade de pessoas.")
        return

    if n <= 0:
        print("O número de pessoas deve ser maior que zero!")
        return

    soma_idades = 0
    for i in range(1, n + 1):
        while True:
            try:
                idade = float(input(f"Digite a idade da {i} pessoa: "))
                if idade < 0:
                    print("Erro.")
                    continue
                break
            except ValueError:
                print("Erro.")
        soma_idades += idade

    media_idade = soma_idades / n
    print(f"\nA média de idade da turma é: {media_idade:.2f}")
    if 0 <= media_idade <= 25:
        print("A turma é jovem.")
    elif 26 <= media_idade <= 60:
        print("A turma é adulta.")
    elif media_idade > 60:
        print("A turma é idosa.")

print(main())