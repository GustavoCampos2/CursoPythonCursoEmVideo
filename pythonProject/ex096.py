def area(lag, com):
    r = lag * com
    print(f'A área do terreno {lag}x{com} é de {r}m².')


print('Controle de Terrenos')
print('-' * 15)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)
