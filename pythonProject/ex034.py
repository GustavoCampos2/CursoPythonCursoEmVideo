salario = float(input('Digite o salario do funcionario? R$'))
if salario > 1250:
    salario = salario * 110 / 100
else:
    salario = salario * 115 / 100
print('seu salario com aumento é R${:.2f}'.format(salario))
