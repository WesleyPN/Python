i = 0
mi = 0
hmv = ''
ihmv = 0
m20 = 0
for i in range(0, 4):
    n = str(input('Digite o nome da {}ª pessoa: '.format(i+1)))
    a = int(input('Digite a idade da {}ª pessoa: '.format(i+1)))
    s = str(input('Digite o sexo da {}ª pessoa (M ou F): '.format(i+1)))
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
print('{} mulheres tem menos de 20 anos de idade.'.format(m20))
