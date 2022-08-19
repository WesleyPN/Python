n = int(input('Digite um número: '))
nf = n
f = n
c = n
fat = str(c)
# fatorial usando for
#for nf in range(nf, 1, -1):
#    f *= nf-1
#    c -= 1
#    fat += ' x ' + str(c)
# fatorial usando while
while c != 1:
    f *= c-1
    c -= 1
    fat += ' x '+str(c)
print('{}!= {} = {}'.format(n, fat, f))
