continuar = True

import random


winA = 0
lossA = 0
winB = 0
lossB = 0
empate = 0

modo_de_jogo =  int(input("Jogue Jokenpo:  "        ## escolher o modo de jogo
            "modalidade:    "
            "1- Humano_X_Humano "
            "2- Humano_X_computador "
            "3- computador_X_computador "))
print(" ")
print('Para "pedra", digite Pedra, para papel, "Papel" e para tesoura, "Tesoura"')
print(" ")



#####################################################################################################################
def Jokenpo(A, B):       ## com os valores definidos na função while (em baixo) é comparada com essa def. que puxa os valores e atualiza o placar
    global winA
    global winB
    global lossA
    global lossB
    global empate
    ## tesoura e pedra
    if A == 'Pedra' and B == 'Tesoura':
        winA += 1
        lossB += 1
        return "Pedra venceu, player A"
    elif A == 'Tesoura' and B == 'Pedra':
        winB += 1
        lossA += 1
        return "Pedra venceu, player B"
    ## pedra e papel
    elif A == 'Papel' and B == 'Pedra':
        winA += 1
        lossB += 1
        return "Papel venceu, player A"
    elif A == 'Pedra' and B == 'Papel':
        winB += 1
        lossA += 1
        return "Papel venceu, player B"
    ## tesoura e papel
    elif A == 'Tesoura' and B == 'Papel':
        winA += 1
        lossB += 1
        return "Tesoura venceu, player A"
    elif A == 'Papel' and B == 'Tesoura':
        winB += 1
        lossA += 1
        return "Tesoura venceu, player B"
    ## empates
    elif A == 'Tesoura' and B == 'Tesoura':
        empate += 1
        return "Empate"
    elif A == 'Pedra' and B == 'Pedra':
        empate += 1
        return "Empate"
    elif A == 'Papel' and B == 'Papel':
        empate += 1
        return "Empate"
    else:
        return "erro"

#######################################################################################################################

while continuar:        ## após escolher o modo de jogo, essa parte irá definir os valores de Pedra, Papel ou Tesoura de cada player

    if modo_de_jogo == 1:
        A = input('Qual sua primeira escolha? Tesoura, Pedra ou Papel:   ')
        B = input('Qual sua segunda escolha? Tesoura, Pedra ou Papel:    ')

    elif modo_de_jogo == 2:
        A = input('Qual sua primeira escolha? Tesoura, Pedra ou Papel:   ')
        B = random.choice(['Tesoura', 'Pedra', 'Papel'])
        print("B: ", B)

    elif modo_de_jogo == 3:
        A = random.choice(['Tesoura', 'Pedra', 'Papel'])
        B = random.choice(['Tesoura', 'Pedra', 'Papel'])
        print(f'Computador A: {A} ## Computador B: {B}')

    else:
        print('erro')

    print(" ")       ## no fim há a opção de continuar ou não, se sim então refaz tudo, se não, o placar é mostrado e o jogo acaba
    print(Jokenpo(A, B))
    Pergunta = int(input('Quer continuar? 1-Sim 2-Não'))

    if Pergunta == 1:
        continuar = True
    else:
        continuar = False
        print(" ")
        print(" ")
        print(f"PlacarA: player A vitória e derrota = {winA}/{lossA}")
        print(f"PlacarB: Player B vitória e derrota = {winB}/{lossB}")
        print(f"Total de empates = {empate}")