n = int(input('Digite um número pra saber sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, c * n))
