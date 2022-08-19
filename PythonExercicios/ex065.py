n = s = c = 0
r = 's'
while r in 'Ss':
    n = float(input('Digite um número: '))
    s += n
    c += 1
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while r not in 'SsNn':
        r = str(input('Entrada inválida! tente novamente.\nQuer continuar? [S/N]: ')).strip().upper()
print('A média de todos os {} números digitados é {}'.format(c, (s/c)))
