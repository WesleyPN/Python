from random import randint
from time import sleep
ms = []
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
print('-'*30)
nj = int(input('Quantos jogos quer que eu sorteie? '))
lnum = []
n = 0
print('{} SORTEANDO {} JOGOS {}'.format('-='*3, nj, '-='*3))
for c in range(0, nj):
    lnum.clear()
    v = 0
    while v < 6:
        n = randint(1, 60)
        if n not in lnum:
            lnum.append(n)
            lnum.sort()
            v += 1
    ms.append(lnum[:])
    sleep(1)
    print(f'Jogo {c+1}: {ms[c]}')
print('{:-^30}'.format('< BOA SORTE! >'))
