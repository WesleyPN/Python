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
    print(f'\033[7;40mPreço analisado: \t{moeda(n).replace(".",",")}')
    print(f'Dobro do preço: \t{dobro(n, fmt=True).replace(".",",")}')
    print(f'Metade do preço: \t{metade(n, fmt=True).replace(".",",")}')
    print(f'{a}% de aumento: \t{aumentar(n, a, fmt=True).replace(".",",")}')
    print(f'{r}% de redução: \t{diminuir(n, r, fmt=True).replace(".",",")}')
    print('\033[m' + '\033[42m-' * 30)
    print('\033[m')
