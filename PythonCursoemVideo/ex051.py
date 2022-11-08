# Minha resolução
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
# resolução do professor
#n = int(input('Digite o primeiro termo da PA.: '))
#r = int(input('Digite a razão da PA.: '))
#d = n + (10 - 1) * r
#pa = ''
#for c in range(n, d + r, r):
#    print('{}'.format(c), end=' -> ')
#print('Acabou')
