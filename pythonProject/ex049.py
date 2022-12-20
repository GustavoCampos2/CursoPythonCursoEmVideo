n1 = int(input('Digite um numero para saber sua tabuada: '))
print('TABUADA DE {}'.format(n1))
for c in range(0, 11):
    print('{} * {} = {}'.format(n1, c, n1 * c))
