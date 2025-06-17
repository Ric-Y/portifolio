x = True
while x:
    Preco = float(input('Qual o preço:'))
    print("1.A vista = 8% de desconto, 2.2x = 4% de desconto, 3.3x = preço normal, 4.4x = 4% a mais, 5.cancelar")
    formaPagamento = int(input('forma de pagamento?'))

    if formaPagamento == 1:
        print(Preco-(Preco*0.08), 'reais a pagar')
    elif formaPagamento == 2:
        print(Preco-(Preco*0.04), 'reais a pagar')
    elif formaPagamento == 3:
        print(Preco, 'reais a pagar')
    elif formaPagamento == 4:
        print(Preco+(Preco*0.04), 'reais a pagar')
    elif formaPagamento ==5:
        x = False
    else:
        print('erro')
