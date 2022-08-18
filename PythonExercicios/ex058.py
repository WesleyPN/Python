from random import randint
n = randint(0, 10)
r = 'S'
c = 0
while r in 'Ss':
    c += 1
    n2 = int(input('Entre 0 e 10, qual número estou pensando? '))
    if n == n2:
        print('Você acertou! o número que estou pensando é {}. '.format(n))
        print('você precisou de {} tentativa(s) para acertar'.format(c))
        r = 'N'
    else:
        r = str(input('Você errou! O número que estou pensando não é {}. \nQuer continuar? [S/N]: '.format(n2))).strip()
