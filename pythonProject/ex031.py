dist = float(input('Qual é a distância da sua viagem? '))
if dist <= 200:
    print('A sua viagem vai custar R${:.2f}'.format(dist * 0.50))
else:
    print('A sua viagem vai custar R${:.2f}'.format(dist * 0.45))
