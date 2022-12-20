media = 0
maioridadehomem = 0
nomevelho = ''
mulh = 0
for c in range(1, 5):
    print('---- {}ª -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    media = idade + media
    if c == 1 and sexo in 'Mn':
       maioridadehomem = idade
       nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulh += 1
media = media / 4
print('')
print('A media de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulh))
