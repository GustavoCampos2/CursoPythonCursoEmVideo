num = list()
mai = men = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = num[c]
    else:
        if num[c] > mai:
            mai = num[c]
        if num[c] < men:
            men = num[c]
print('=-' * 30)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi o {mai} nas posições...', end='')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi o {men} posições...', end='')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}...', end='')
