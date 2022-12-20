brasileirao = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense',
               'Corinthians', 'Athletico-PR', 'Atletico-MG', 'America-MG',
               'Fortaleza', 'Botafogo', 'Santos', 'São Paulo', 'Bragantino',
               'Goiás', 'Coritiba', 'Ceará', 'Cuiabá', 'Atletico-GO', 'Avaí', 'Juventude')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-=' * 20)
print(f'Os 5 primeiros são {brasileirao[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {brasileirao[-4:]}')
print('-=' * 20)
print(f'times em ordem alfabética: {sorted(brasileirao)}')
print('-=' * 20)
print(f'A Botafogo está na {brasileirao.index("Botafogo")+1}ª posição')
