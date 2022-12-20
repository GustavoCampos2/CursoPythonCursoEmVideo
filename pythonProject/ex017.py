import math
c1 = float(input('digite o numero do cateto oposto: '))
c2 = float(input('digite o numero do cateto adjacente: '))
h = math.sqrt((c1*c1)+(c2*c2))
print('{:.2f}'.format(h))
print('a hipotenusa é: {:.2f}'.format(math.hypot(c1, c2)))
