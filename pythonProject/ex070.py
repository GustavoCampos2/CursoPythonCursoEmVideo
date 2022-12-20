print('-' * 25)
print('   LOJA SUPER BARATÃO   ')
print('-' * 25)
total = totmil = menor = 0
item = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        totmil += 1
    if menor == 0 or menor > preco:
        menor = preco
        item = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {item} que custa R${menor:.2f}')
