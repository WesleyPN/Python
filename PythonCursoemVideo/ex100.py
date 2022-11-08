from random import randint
from time import sleep


def sorteia(lst):
    print('Sorteando 5 valores da lista:', end=' ')
    for n in range(0, 5):
        lst.append(randint(1, 10))
        print(lst[n], end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    print(f'Somando os valores pares de {lst},', end=' ')
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
