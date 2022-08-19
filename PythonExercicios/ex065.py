n = 0
s = 0
c = 0
r = 's'
while r in 'Ss':
    n = float(input('Digite um número: '))
    s += n
    c += 1
    r = str(input('Quer continuar? [S/N]: '))
print('A média de todos os {} números digitados é {}'.format(c, (s/c)))
