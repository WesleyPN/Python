from random import randint
from time import sleep
from operator import itemgetter
res = dict()
ord = dict()
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
print('-='*30)
ord = sorted(res.items(), key=itemgetter(1), reverse=True)
for c, j in enumerate(ord):
    print(f'{c+1}º lugar: {j[0]} com {j[1]}')
    sleep(1)
