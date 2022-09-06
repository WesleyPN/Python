atletas = []
jogador = {}
gols = []
while True:
    jogador['Nome'] = str(input('Nome do Jogador: ')).title()
    part = int(input(f'Partidas jogadas por {jogador["Nome"]}: '))
    cont = 0
    for g in range(0, part):
        gols.append(int(input(f'Gols de {jogador["Nome"]} na partida {g+1}: ')))
        cont += gols[g]
    jogador['Gols'] = gols[:]
    jogador['Total'] = cont
    atletas.append(jogador.copy())
    gols.clear()
    cont = 0
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        print('-='*40)
        break
print(f'{"COD": <5}{"Nome": <20}{"Gols": <20}{"Total": <5}')
print('--'*40)
for c in range(0, len(atletas)):
    print(f'{c: ^5}{atletas[c]["Nome"]: <20}{str(atletas[c]["Gols"]): <20}{atletas[c]["Total"]: <5}')
print('--'*40)
while True:
    j = int(input('Mostrar dados de qual jogador? '))
    while j not in range(0, len(atletas)) and j != 999:
        print(f'ERRO! Não existe jogador com código {j} Tente novamente.')
        j = int(input('Mostrar dados de qual jogador? '))
    if j == 999:
        print('<<VOLTE SEMPRE!>>')
        break
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {atletas[j]["Nome"]}:')
        for c, v in enumerate(atletas[j]['Gols']):
            print(f'    No {c+1}º jogo fez {v} gols')
