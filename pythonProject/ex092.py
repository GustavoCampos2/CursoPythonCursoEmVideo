from datetime import datetime
ficha = dict()
ficha['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
ficha['idade'] = datetime.today().year - ano
ficha['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if ficha['ctps'] != 0:
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['salario'] = float(input('Salário: '))
    ficha['aposentadoria'] = ((ficha['contratação'] + 35) - ano)
print(ficha)
for k, v in ficha.items():
    print(f'{k} tem o valor {v}')
