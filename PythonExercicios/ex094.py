pessoa = {}
listaP = []
listaM = []
listaAM = []
cont = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    listaP.append(pessoa.copy())
    cont += pessoa['Idade']
    while True:
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if r in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if r == 'N':
        break
print(f'Foram cadastradas {len(listaP)} pessoas.')
print(f'A média de idade do grupo é de {cont/len(listaP):.2f} anos.')
print('As mulheres cadastradas são: ', end='')
for v in listaP:
    if v['Sexo'] == 'F':
        print(f'{v["Nome"]} ', end='')
print()
print('Lista das pessoas com idade acima da média:', end='')
for v in listaP:
    if v['Idade'] > cont / len(listaP):
        print('     ')
        for k, n in v.items():
            print(f'{k} = {n}', end='; ')
        print()
print('<< ENCERRADO >>')
