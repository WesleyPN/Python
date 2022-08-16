i = 0
mi = 0
nh = ''
ih = 0
im = 0
for i in range(0, 4):
    print('----- {}ª PESSOA -----'.format(i+1))
    n = str(input('Nome: ')).strip()
    a = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip()
    mi += a
    if i == 3:
        mi = mi/(i+1)
    if s.upper() == 'M' and a >= ih:
        ih = a
        nh = n
    if s.upper() == 'F' and a < 20:
        im += 1
print('A média de idade do grupo é de {} anos.'.format(mi))
print('O nome do homem mais velho é {}, com {} anos.'.format(nh, ih))
print('No total {} mulheres tem menos de 20 anos de idade.'.format(im))
