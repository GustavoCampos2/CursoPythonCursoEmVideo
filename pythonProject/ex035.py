print('-=-'*10)
print('analisador de triângulos')
print('-=-'*10)
r1 = float(input('Digite o primeiro segmento:'))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r3 + r2 > r1 and r1 + r3 > r2 and r2 + r2 > r3:
    print('\033[36mOs tres segmentos formam um triangulo!')
else:
    print('\033[31mOs tres segmento não formam um triangulo')
