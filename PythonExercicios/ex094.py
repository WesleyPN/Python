pessoa = {}
listaP = []
listaM = []
listaAM = []
cont = c = 0
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while pessoa['Sexo'] not in 'MF':
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    listaP.append(pessoa.copy())
    cont += pessoa['Idade']
    c += 1

    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        print('-='*30)
        break

print(f'Foram cadastradas {len(listaP)} pessoas.')
print(f'A média de idade do grupo é de {cont/len(listaP):.2f} anos.')
print('As mulheres cadastradas são: ', end='')
for v in listaP:
    if v['Sexo'] == 'F':
        print(f'{v["Nome"]} ', end='')
print()
print('Lista das pessoas com idade acima da média:')
for v in listaP:
    for k, n in v.items():
        if v['Idade'] > cont/len(listaP):
            print(f'{k} = {n}', end='; ')
    print()
