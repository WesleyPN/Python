def aumentar(n, p):
    porcento = n * p / 100
    return n + porcento


def diminuir(n, p):
    porcento = n * p / 100
    return n - porcento


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def moeda(n):
    return f'R${n:.2f}'
