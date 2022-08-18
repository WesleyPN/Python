n = int(input('Digite o primeiro termo da PA.: '))
r = int(input('Digite a razão da PA.: '))
pa = ''
c = 1
while c <= 10:
    if c == 1:
        pa = '['+str(n) + ', '
    elif c == 10:
        n += r
        pa += str(n) + ']'
    else:
        n += r
        pa += str(n)+', '
    c += 1
print('Os 10 primeiros termos da PA. são: \n{}'.format(pa))