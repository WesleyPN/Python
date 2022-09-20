def aumentar(n, p, fmt=False):
    porcento = n * p / 100
    if fmt:
        return moeda(n + porcento)
    else:
        return n + porcento


def diminuir(n, p, fmt=False):
    porcento = n * p / 100
    if fmt:
        return moeda(n - porcento)
    else:
        return n - porcento


def dobro(n, fmt=False):
    if fmt:
        return moeda(n * 2)
    else:
        return n * 2


def metade(n, fmt=False):
    if fmt:
        return moeda(n / 2)
    else:
        return n / 2


def moeda(n):
    return f'R${n:.2f}'


def resumo(n, a=0, r=0):
    print('\033[1;42m' + ('-' * 30))
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print('\033[m', end='')
    print(f'\033[7;40mPreço analisado:    {moeda(n)}')
    print(f'Dobro do preço:     {dobro(n, fmt=True)}')
    print(f'Metade do preço:    {metade(n, fmt=True)}')
    print(f'{a}% de aumento:     {aumentar(n, a, fmt=True)}')
    print(f'{r}% de redução:     {diminuir(n, r, fmt=True)}')
    print('\033[m' + '\033[42m-' * 30)
    print('\033[m')
