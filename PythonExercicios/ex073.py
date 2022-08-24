cambra = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Internacional', 'Athletico-PR', 'Atlético-MG',
          'Santos', 'América-MG', 'Bragantino', 'Goiás', 'São Paulo', 'Fortaleza', 'Botafogo', 'Ceará', 'Cuiabá',
          'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')
print('-='*30)
print(f'Lista de times do Brasileirão: {cambra}')
print('-='*30)
print(f'Os 5 primeiros são: {cambra[0:5]}')
print('-='*30)
print(f'Os 4 últimos são: {cambra[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(cambra)}')
print('-='*30)
print(f'O Santos está na {cambra.index("Santos")+1}ª posição')
