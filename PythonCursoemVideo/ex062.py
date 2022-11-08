pt = int(input('Digite o primeiro termo da PA.: '))
r = int(input('Digeite a razão da PA.: '))
t = pt
c = 1
tt = 0
m = 10
pa = ''
while m != 0:
    tt += m
    while c <= tt:
        pa += str(t)+' - '
        t += r
        c += 1
    print(pa+'Fim')
    m = int(input('Quer exibir mais quantos termos da PA.? '))
    pa = ''
