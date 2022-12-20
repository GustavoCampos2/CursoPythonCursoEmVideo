jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome do Jogador: '))
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for v in range(0, jogos):
    gols.append(int(input(f'Quantos gols na partida {v}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campos {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas')
for k, v in enumerate(jogador['gols']):
    print(f'    => Na partida {k+1}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols.')
