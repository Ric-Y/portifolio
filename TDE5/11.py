import random
def gerar_aposta():
    return random.sample(range(1, 61), 6)
def obter_aposta_usuario():
    aposta_usuario = set()
    while len(aposta_usuario) < 6:
        try:
            numero = int(input(f"Digite um número entre 1 e 60 ({len(aposta_usuario)+1}/6): "))
            if numero < 1 or numero > 60:
                print("Número fora do intervalo. Tente novamente.")
            elif numero in aposta_usuario:
                print("Número repetido. Tente novamente.")
            else:
                aposta_usuario.add(numero)
        except ValueError:
            print("Entrada inválida. Digite um número.")
    return list(aposta_usuario)
def verificar_acertos(aposta_gerada, aposta_usuario):
    acertos = set(aposta_gerada) & set(aposta_usuario)
    return acertos

aposta_gerada = gerar_aposta()
print("\nNúmeros sorteados:", aposta_gerada)

aposta_usuario = obter_aposta_usuario()
print("\nSua aposta:", aposta_usuario)

acertos = verificar_acertos(aposta_gerada, aposta_usuario)
print(f"\nVocê acertou {len(acertos)} número(s): {sorted(acertos)}")

