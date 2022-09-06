aluno = dict()
aluno['Nome'] = str(input('Nome: ')).title()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 < aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    if type(v) == float:
        print(f'{k} é igual a {v:.2f}')
    else:
        print(f'{k} é igual a {v}')
