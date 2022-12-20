print('{:^20}'.format('LOJA'))
vlr = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO'
[ 1 ] à vista dinheiro/cheque'
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opc = int(input('Qual é a sua opção? '))
if opc == 1:
    print('Sua compra no valor de {:.2f} vai sair por {:.2f} com 10% de desconto'.format(vlr, ((vlr*90)/100)))
elif opc == 2:
    print('Sua compra no valor de {:.2f} vai sair por {:.2f} com 5% de desconto'.format(vlr, ((vlr*95)/100)))
elif opc == 3:
    print('Sua compra no valor de {:.2f} não terá acrescimo'.format(vlr))
elif opc == 4:
    print('Sua compra no valor de {} vai sair por {:.2f} com 20% de juros'.format(vlr, ((vlr*120)/100)))
else:
    print('Opção invalida tente novamente')
