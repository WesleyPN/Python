t = 10
pt = int(input('Digite o primeiro termo da PA.: '))
r = int(input('Digeite a razão da PA.: '))
ut = pt + (t - 1) * r
pa = ''
while t != 0:
    for c in range(pt, ut+1, r):
        pa += str(c)+' - '
    print(pa+'Fim')
    t = int(input('Quer exibir mais quantos termos da PA.? '))
    if t != 0:
        pa = ''
        pt = c + r
        ut = pt + (t - 1) * r
