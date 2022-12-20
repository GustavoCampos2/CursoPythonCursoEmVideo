princ = [[], []]
for v in range(1, 8):
    valor = int(input(f'Digite {v}o. valor: '))
    if valor % 2 == 0:
        princ[0].append(valor)
    else:
        princ[1].append(valor)
print('-=' * 30)
princ[0].sort()
princ[1].sort()
print(f'Os valores pares digitados foram: {princ[0]}')
print(f'Os valores ímpares digitados foram: {princ[1]}')
