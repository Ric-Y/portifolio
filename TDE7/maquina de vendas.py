#Matriz com cada produto - add while em tudo
from sys import int_info

produtos = [
    ["Coca-cola", 3.75, 2],
    ["Pepsi", 3.67, 5],
    ["Monster", 9.96, 1],
    ["Café", 1.25, 100],
    ["Redbull", 13.99, 2]
]

### funções ##########################################################################################

#busca do modo de pagamento e calcula o troco
def pagamento():
    if pagamento_real >= preço_total:
        return f"pagamento em andamento, seu troco será de {valor_troco}"
    else:
        return "erro"

#gerando o troco
def troco():
    global valor_troco
    nota_do_troco = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]
    limite_notas = {100: 4, 50: 4, 20: 4, 10: 4, 5: 4, 2: 4, 1: 4}

    resultado = {}
    troco_restante = valor_troco  # Mantém o valor original do troco

    for nota in nota_do_troco:
        quantidade = troco_restante // nota
        if quantidade > 0:
            if nota in limite_notas and quantidade > limite_notas[nota]:
                quantidade = limite_notas[nota]
            resultado[nota] = int(quantidade)
            troco_restante = round(troco_restante - (quantidade * nota), 2)
    print('Notas do troco:')
    for nota, qtd in resultado.items():
        print(f'R$ {nota:.2f} → {qtd}x')

### código funcional ################################################################################

LOOP1 = True

while LOOP1:
    for num in range(len(produtos)):
        print(num+1,": ", produtos[num][0], produtos[num][1])
    x = int(input(f"""Digite o código do seu produto:"""))-1
    #quantidade de produtos
    c = int(input(f'Qual a quantidade de {produtos[x][0]} que você quer?\n'
                  f'{produtos[x][2]} <--- quantidade restante do produto.\n'))
    if c != -1:
        LOOP2 = True

        #verifica se o produto tem na quantidade pedida e calcula o preço total
        if c <= produtos[x][2]:
            produtos[x][2] -= c
            preço_total = produtos[x][1] * c
            print(f'valor a pagar: {preço_total}')

        #modo de pagamento - add while----------------------------------------------------------------------
            while LOOP2:
                modo_de_pagar = input('Vai pagar em Nota ou Cartão? ').strip().lower()
                if modo_de_pagar == "nota":
                    tipo_nota = int(input("Qual nota deseja inserir? "))
                    while tipo_nota not in [2, 5, 10, 20, 50, 100, 200]:
                        print('Nota invalida')
                    quantidade_nota = int(input("quantas notas deseja inserir? "))
                    pagamento_real = tipo_nota*quantidade_nota # calcula o valor que esta pagando
                    valor_troco = pagamento_real - preço_total
                    if valor_troco > 0:
                        troco()
                        continuar = input("quer continuar?").strip().lower()
                        if continuar == "sim":
                            LOOP1 = True
                            LOOP2 = False
                        elif continuar == "não":
                            LOOP1 = False
                            LOOP2 = False
                elif modo_de_pagar == "cartão":
                    print(f"insira o cartão ou aproxime da maquineta, valor total a pagar: {preço_total}")
                    continuar = input("quer continuar?").strip().lower()
                    if continuar == "sim":
                        LOOP1 = True
                        LOOP2 = False
                    elif continuar == "não":
                        LOOP1 = False
                        LOOP2 = False

                else:
                    print('metodo de pagamento invalido')
        # --------------------------------------------------------------------------------------------------
    #modo adm
    if c == -1:
        senha = int(input('Digite a senha:'))
        if senha == 12345:
            print(produtos, """\n 1 - nome do produto. 2 - preço, 3 - Quantidade""")
            modo_de_atualização = int(input("Deseja:\n 1: editar o preço do produto\n 2: apagar um protudo\n 3: adcionar um novo?"))
            if modo_de_atualização == 1:
                numero_prod_adm = int(input("Qua o código do produto?"))-1
                Novo_preço = float(input("Digite o novo preço, (exemplo 0.00):"))
                produtos[numero_prod_adm][1] = Novo_preço
            if modo_de_atualização == 2:
                numero_prod_remov = int(input('Digite o código do produto a ser removido: '))-1
                del produtos[numero_prod_remov]
            if modo_de_atualização == 3:
                lista = []
                PRODUTO_novo = input("Nome do protudo:")
                Preço_novo = float(input("Preço novo, (exemplo 0.00):"))
                Quantidade_novo = int(input("Quantidade:"))

                lista.append(PRODUTO_novo)
                lista.append(Preço_novo)
                lista.append(Quantidade_novo)
                produtos.append(lista)
                del lista
        else:
            print("senha errada")
    else:
        print('erro')