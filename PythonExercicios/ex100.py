from random import randint


def sorteia(lst):
    print('Sorteando 5 valores da lista:', end=' ')
    for n in range(0, 5):
        lst.append(randint(1, 10))
        print(lst[n], end=' ')
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    print(f'Somando os valores pares de {lst},', end=' ')
    for c, v in enumerate(lst):
        if lst[c] % 2 == 0:
            soma += v
    print(f'temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
