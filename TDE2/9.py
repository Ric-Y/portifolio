idade = int(input("Sua idade: "))
if idade < 16:
    X = "Não votante"
elif 16 <= idade < 18 or idade > 65:
    X = "Eleitor facultativo"
else:
    X = "Eleitor obrigatório"

print(f"Com {idade} anos, sua classe eleitoral é: {classe_eleitoral}")

## se usar F e duas aspas da pra usar o {} e encurtar a frase no print
## exemplo f("--- {} --")
