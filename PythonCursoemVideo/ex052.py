n = int(input('Digite um número: '))
c = 0
for i in range(1, n+1):
    if n % i == 0 and n / n == 1:
        c += 1
if c == 2:
    print('O número {} é um número primo'.format(n))
else:
    print('O número {} não é um número primo'.format(n))
