i = int(input("Digite o limite inicial: "))
f = int(input("Digite o limite final: "))
print("Multiplos de 3 no intervalo aberto ({} a {}):".format(i, f))
for n in range(i + 1, f):
    if n % 3 == 0:
        print(n)
