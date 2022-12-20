print('{:^30}'.format('Gerador de PA'))
print('-=-' * 10)
numero = int(input('Primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = numero
cont = 1
while cont <= 10:
    print('{} ► '.format(termo), end='')
    termo = termo + razao    #termo += razao
    cont += 1
print('FIM')
