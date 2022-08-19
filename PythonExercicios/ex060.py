n = int(input('Digite um número: '))
nf = n
f = n
c = n
fat = str(c)
# fatorial usando for
#for n in range(n, 1, -1):
#    f *= n-1
#    c -= 1
#    fat += ' x ' + str(c)
# fatorial usando while
while c != 1:
    f *= c-1
    c -= 1
    fat += ' x '+str(c)
print('{}!= {} = {}'.format(nf, fat, f))
