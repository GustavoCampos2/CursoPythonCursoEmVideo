from random import randint
computador = randint(1, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
contador = 0
while not acertou:
    user = int(input('Qual é seu palpite? '))
    contador += 1
    if user == computador:
        acertou = True
    else:
        if computador > user:
            print('Mais... Tente mais uma vez.')
        if computador < user:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentarivas. Parabéns!'.format(contador))
