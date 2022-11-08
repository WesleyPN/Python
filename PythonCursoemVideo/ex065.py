n = s = c = ma = me = 0
r = 's'
while r in 'Ss':
    n = float(input('Digite um número: '))
    s += n
    c += 1
    if c == 1:
        ma = me = n
    elif n > ma:
        ma = n
    elif n < me:
        me = n
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while r not in 'SsNn':
        r = str(input('Entrada inválida! tente novamente.\nQuer continuar? [S/N]: ')).strip().upper()
print('A média de todos os {} números digitados é {}'.format(c, (s/c)))
print('O maior valor foi {} e o menor valor foi {}'.format(ma, me))
