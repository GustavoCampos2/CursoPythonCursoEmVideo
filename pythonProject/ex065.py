num = int(input('Digite um numero: '))
stop = str(input('Quer Continuar? [S/N] ')).upper().strip()
soma = maior = menor = num
cont = 1
while stop != 'N':
    cont += 1
    num = int(input('Digite um numero: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    stop = str(input('Quer Continuar? [S/N] ')).upper().strip()
print('Voce digitou {} numeros e a media foi {}'.format(cont, soma/cont))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
