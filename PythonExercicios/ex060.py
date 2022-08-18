n = int(input('Digite um número: '))
f = n
c = n
# fatorial usando for
#for n in range(n, 1, -1):
#    f *= n-1
# fatorial usando while
while c != 1:
    f *= c-1
    c -= 1
print('{}! = {}'.format(n, f))
