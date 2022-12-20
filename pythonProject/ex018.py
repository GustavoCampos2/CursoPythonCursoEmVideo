from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que voce deseja: '))
seno = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
cos = cos(radians(an))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an, cos))
tang = tan(radians(an))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(an, tang))
