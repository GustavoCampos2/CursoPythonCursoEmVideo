matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceira = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            terceira += matriz[l][c]
        if l == 1:
            if c == 0 or matriz[l][c] > maior:
                maior = matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {pares}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da terceira linha é {maior}')
