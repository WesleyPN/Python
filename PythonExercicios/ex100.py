from random import randint


def sorteia(lst):
    for n in range(0, 5):
        lst.append(randint(1, 10))


def somaPar(lst):
    soma = 0
    print(f'Os valores informados são', end=' ')
    for c, v in enumerate(lst):
        print(v, end=' ')
        if lst[c] % 2 == 0:
            soma += v
    print()
    print(f'A soma dos pares é {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
