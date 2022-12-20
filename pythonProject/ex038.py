num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    ('{} é maior que {}'.format(num1, num2))
elif num2 > num1:
    ('{} é maior que {}'.format(num2, num1))
else:
    ('os dois valores são iguais')
