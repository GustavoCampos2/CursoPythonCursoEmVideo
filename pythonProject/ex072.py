num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    user = int(input('Digite um número entre 0 e 20: '))
    if 0 <= user <= 20:
        break
    print('Tente novamente.', end='')
print(f'voce digitou o número {num[user]}')
