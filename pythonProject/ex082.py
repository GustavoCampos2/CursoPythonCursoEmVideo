lista = list()
par = list()
impar = list()
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    stop = str(input('Quer continuar? [S/N] ')).strip().upper()
    if stop in 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
