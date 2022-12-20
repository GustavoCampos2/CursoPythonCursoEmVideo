from random import choice
n1 = input('digite o nome do primeiro candidato: ')
n2 = input('digite o nome do segundo candidato: ')
n3 = input('digite o nome do terceiro candidato: ')
n4 = input('digite o nome do quarto candidato: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('eu vou votar no {}'.format(escolhido))
