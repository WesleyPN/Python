n = int(input('Digite o primeiro termo da PA.: '))
r = int(input('Digite a razão da PA.: '))
pa = ''
for c in range(1, 11):
    if c == 1:
        pa = '['+str(n) + ', '
    elif c == 10:
        n += r
        pa += str(n) + ']'
    else:
        n += r
        pa += str(n)+', '
print('Os 10 primeiros termos da PA. são: \n{}'.format(pa))
