massa = float(input("Digite sua massa em Kg: "))
altura = float(input("Digite sua altura em M: "))
imc = massa / (altura ** 2)
print('IMC:', imc)
if 18.5 <= imc < 25:
    print("Seu IMC está na faixa normal segundo a OMS.")
else:
    print("Seu IMC não está na faixa normal segundo a OMS.")
