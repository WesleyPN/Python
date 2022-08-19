s = str(input('Sexo [M/F]: ')).strip().upper()[0]
while s not in 'MmFf':
    print('Dado inválido. Tente novamente.')
    s = str(input('Sexo [M/F]: ')).strip().upper()[0]
