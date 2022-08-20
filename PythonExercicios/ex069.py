ci = 0
ch = 0
cm = 0
while True:
    print('--'*20)
    print('     CADASTRE UMA PESSOA')
    print('--' * 20)
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while s not in 'MmFf':
        s = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('--'*30)
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if i > 18:
        ci += 1
    if s == 'M':
        ch += 1
    if i < 20 and s == 'F':
        cm += 1
    if r == 'N':
        break
        print('--' * 20)
print(f'A quantidade de pessoas com mais de 18 anos é: {ci}')
print(f'A quantidade de homens cadastrados é: {ch}')
print(f'A quantidade de mulheres com menos de 20 anos é: {cm}')
