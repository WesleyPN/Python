def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    conta = f'!{n} = '
    for c in range(n, 0, -1):
        f *= c
        if c != 1:
            conta += str(c) + ' x '
        else:
            conta += str(c) + ' = '
    if show:
        return f'{conta}{f}'
    else:
        return f


print(fatorial(5, True))
help(fatorial)
