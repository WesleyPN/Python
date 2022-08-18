s = str(input('Sexo [M/F]: ')).strip()
while s not in 'MmFf':
    print('Dado inválido. Tente novamente.')
    s = str(input('Sexo [M/F]: ')).strip()
