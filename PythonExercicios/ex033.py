n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
ma = n1
me = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3

if n2 < n1 and n2 < n3:
    me = n2
if n3 < n2 and n3 < n1:
    me = n3
print('O maior número é {}'.format(ma))
print('O menor número é {}'.format(me))
