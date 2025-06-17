dolar = float(input("Digite a cotação do dólar hoje: "))
libra = float(input("Digite a cotação da libra hoje: "))
euro = float(input("Digite a cotação do euro hoje: "))

codigo_moeda = input("Digite o código da moeda (USD para dólares, Lb para libras, EU para euros): ")
quantidade = float(input("Digite a quantidade que deseja comprar: "))

if quantidade < 1000:
    comissao = 0.05  # 5%
else:
    comissao = 0.03  # 3%

if codigo_moeda == "USD":
    valorTotal = quantidade * dolar
elif codigo_moeda == "Lb":
    ValorTotal = quantidade * libra
elif codigo_moeda == "EU":
    valorTotal = quantidade * euro
else:
    valorTotal = None

# Exibir o resultado
if valorTotal is not None:
    valorComComissao = valorTotal * (1 + comissao)
    print(f"O valor total em reais (incluindo comissão) é: R$ {valorComComissao}:")
else:
    print("Erro.")
