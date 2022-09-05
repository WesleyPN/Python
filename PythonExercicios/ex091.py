from random import randint
from time import sleep
res = dict()
print('Valores sorteados:')
for j in range(0, 4):
    res['Jogador-'+str(j+1)] = randint(1, 6)
for k, v in res.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('Ranking dos jogadores:')
for c, j in enumerate(sorted(res, key=res.get, reverse=True)):
    print(f'{c+1}ª lugar: {j} com {res[j]}')
    sleep(1)
