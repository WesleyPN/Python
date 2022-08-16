i = 0
mi = 0
hmv = ''
ihmv = 0
m20 = 0
for i in range(0, 4):
    print('----- {}ª PESSOA -----'.format(i+1))
    n = str(input('Nome: '))
    a = int(input('Idade: '))
    s = str(input('Sexo [M/F]: '))
    mi += a
    if i == 3:
        mi = mi/(i+1)
    if s.upper() == 'M' and a >= ihmv:
        ihmv = a
        hmv = n
    if s.upper() == 'F' and a < 20:
        m20 += 1
print('A média de idade do grupo é de {} anos.'.format(mi))
print('O nome do homem mais velho é {}, com {} anos.'.format(hmv, ihmv))
print('No total {} mulheres tem menos de 20 anos de idade.'.format(m20))
