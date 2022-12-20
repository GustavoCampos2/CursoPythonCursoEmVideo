lista = (int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')))
print(f'Você digitou os valores {lista}')
print(f'o numero 9 aparece {(lista.count(9))} vezes')
if 3 in lista:
    print(f'o numero 3 aparece na {(lista.index(3))+1}ª posição')
else:
    print(f'o valor 3 não foi digitado em nenhuma posição')
for n in lista:
    if n % 2 == 0:
        print(f'Os valores pares digitados foram ', end='')
        print(n, end=' ')