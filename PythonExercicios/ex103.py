def ficha(nome=0, gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


jogador = str(input('Nome do Jogador: '))
ngols = str(input('Número de Gols: '))
print(ficha(jogador, ngols))
