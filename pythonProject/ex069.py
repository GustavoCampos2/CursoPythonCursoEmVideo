maior18 = homens = mulher20 = 0
print('-' * 30)
print(f'{"CADASTRO DE PESSOAS":^25}')
print('-' * 30)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opc == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')
