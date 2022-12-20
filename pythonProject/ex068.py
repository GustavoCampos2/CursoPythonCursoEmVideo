from random import randint
print('-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-' * 15)
cont = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ').upper().strip())[0]
    print('-' * 30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador},', end='')
    resultado = (jogador + computador) % 2
    if resultado == 0:
        print(' DEU PAR')
        if tipo == 'P':
            cont += 1
            print('Você VENCEU!')
        else:
            print('Voce PERDEU')
            break
    else:
        print(' DEU IMPAR')
        if tipo == 'I':
            cont += 1
            print('Você GANHOU')
        else:
            print('Voce PERDEU')
            break
    print('-' * 30)
print(f'GAME OVER! Voce venceu {cont} vezes.')