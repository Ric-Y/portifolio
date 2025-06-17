cont_0_25 = 0
cont_26_50 = 0
cont_51_75 = 0
cont_76_100 = 0

print("Digite números positivos. Para finalizar, digite -1.")
while True:
    valor = int(input("Digite um número: "))
    if valor == -1:
        break
    if 0 <= valor <= 25:
        cont_0_25 += 1
    elif 26 <= valor <= 50:
        cont_26_50 += 1
    elif 51 <= valor <= 75:
        cont_51_75 += 1
    elif 76 <= valor <= 100:
        cont_76_100 += 1

print("\nQuantidade de números em cada intervalo:")
print(f"[0-25]: {cont_0_25}, [26-50]: {cont_26_50}, [51-75]: {cont_51_75}, [76-100]: {cont_76_100}")
