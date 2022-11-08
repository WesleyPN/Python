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
