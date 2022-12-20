print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)
numero = int(input('Primeiro numero: '))
razao = int(input('Razão: '))
decimo = numero + (10 - 1) * razao
for c in range(numero, decimo + razao, razao):
    print('{} '.format(c), end='► ')
print('acabou')