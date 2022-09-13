def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


jogador = str(input('Nome do Jogador: '))
ngols = str(input('Número de Gols: '))
if ngols.isnumeric():
    ngols = int(ngols)
else:
    ngols = 0
if jogador.strip() == '':
    ficha(gols=ngols)
else:
    ficha(jogador,ngols)
