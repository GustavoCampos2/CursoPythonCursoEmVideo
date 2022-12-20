num = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor in num:
        print('Valor duplicado! Não vou adicionar...')
    else:
        num.append(valor)
        print('Valor adicionado com sucesso...')
    stop = str(input('Quer continuar? [S/N]')).strip().upper()
    if stop in 'Nn':
        break
print('-=' * 30)
num.sort()
print(f'Você digitou os valores {num}')
