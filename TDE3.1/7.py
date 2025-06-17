def primo(num):
    if num < 2:
        return False
    limite = int(num ** 0.5) + 1
    for i in range(2, limite):
        if num % i == 0:
            return False
    return True

entrada = input("Digite um numero inteiro: ")
if entrada.lstrip('-').isdigit():
    numero = int(entrada)
    if primo(numero):
        print(f"{numero} é um numero primo.")
    else:
        print(f"{numero} não é um numero primo.")
else:
    print("Erro.")
