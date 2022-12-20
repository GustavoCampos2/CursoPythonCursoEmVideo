lg = float(input('Largura da Parede: '))
al = float(input('Altura da Parece: '))
mq = lg * al
qt = mq / 2
print('a parede tem {:.2f}m², você precisa de {:.2f} litros para pintar essa parede'.format(mq, qt))
