expressao = input('Digite um expressão: ')
cont = 0
for c in expressao:
    if c == '(':
        cont += 1
    elif c == ')':
        cont -= 1
    if cont < 0:
        break
if cont == 0:
    print('Expressão valida')
else:
    print('Expressão invalida')
