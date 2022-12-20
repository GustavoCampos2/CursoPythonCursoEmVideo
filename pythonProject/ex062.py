print('{:^30}'.format('Gerador de PA'))
print('-=-' * 10)
numero = int(input('Primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = numero
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ► '.format(termo), end='')
        termo = termo + razao    #termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
