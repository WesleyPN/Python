alunos = list()
notas = list()
while True:
    nome = str(input('Nome: ')).title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    notas = [n1, n2]
    alunos.append([nome[:], notas[:], (n1+n2)/2])

    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        print('-='*30)
        print(f'\033[4m{"R.A.": <5}|{"Nome": <20}|{"Média": <5}\033[m')
        for c in range(0, len(alunos)):
            print(f'\033[4m{alunos.index(alunos[c]): <5}|{alunos[c][0]: <20}|{alunos[c][2]: <5.2f}\033[m')
        break
while True:
    n = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if n == 999:
        break
    elif n > len(alunos)-1:
        print('R.A. inválido. Tente novamente!')
    else:
        print(f'Notas de {alunos[n][0]} são {alunos[n][1]}')
