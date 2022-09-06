jogador = {}
gols = []
jogador['Nome'] = str(input('Nome do Jogador: ')).title()
part = int(input(f'Partidas jogadas por {jogador["Nome"]}: '))
cont = 0
for g in range(0, part):
    gols.append(int(input(f'Gols de {jogador["Nome"]} na partida {g+1}: ')))
    cont += gols[g]
jogador['Gols'] = gols[:]
jogador['Total'] = cont
print('-='*40)
print(jogador)
print('-='*40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*40)
print(f'O jogador {jogador["Nome"]} jogou {part} partidas.')
for c, g in enumerate(gols):
    print(f'    => Na partida {c+1}, fez {g} gols.')
print(f'Foi um total de {jogador["Total"]} gols')
