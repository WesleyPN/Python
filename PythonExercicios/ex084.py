pessoas = list()
pes = []
lev = []
while True:
    pessoas.append([str(input('Nome: ')).title(), float(input('Peso: '))])
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        print('-='*30)
        break
for c in range(0, len(pessoas)):
    if c == 0:
        pesado = leve = pessoas[c][1]
    elif pessoas[c][1] >= pesado:
        pesado = pessoas[c][1]
    elif pessoas[c][1] <= leve:
        leve = pessoas[c][1]
for p in range(0, len(pessoas)):
    if pesado in pessoas[p]:
        pes.append(pessoas[p][0])
    elif leve in pessoas[p]:
        lev.append(pessoas[p][0])

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {pesado}Kg. Peso de {pes}')
print(f'O menor peso foi de {leve}Kg. Peso de {lev}')
