casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salario: R$'))
tempo = int(input('Em quanto anos pretende pagar: '))
prestacao = casa / (tempo * 12)

if prestacao < (salario * 30) / 100:
    print('\033[34mparabens voce conseguiu o emprestimo\033[0m')
    print('A prestação mensal será de R${:.2f}'.format(prestacao))
else:
    print('\033[31mseu emprestimo foi negado\033[0m')
    print('A prestação de R${:.2f} ultrapassa os 30% do seu salario'.format(prestacao))
