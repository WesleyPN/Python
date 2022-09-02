alunos = list()
notas = list()

while True:
    alunos.append(str(input('Nome: ')).title())
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    notas = n1, n2
    alunos.append(notas[:])
    alunos.append((n1+n2)/2)

    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        print('-='*30)
        for c in range(0, len(alunos), 3):
            print(f'{c} {alunos[c]} {alunos[c+2]:.2f}')
        break
print(alunos)
