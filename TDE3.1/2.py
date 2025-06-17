def is_triangular(n):
    if n < 6:
        return False

    i = 1
    while True:
        produto = i * (i + 1) * (i + 2)
        if produto == n:
            return True
        elif produto > n:
            return False
        i += 1
try:
    n = int(input("Digite um numero inteiro não negativo: "))
    if n < 0:
        print("Erro.")
    else:
        if is_triangular(n):
            print(f"{n} é um numero triangular!")
        else:
            print(f"{n} não é um numero triangular.")
except ValueError:
    print("Erro.")
