lista = [int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')), int(input('Digite o 3º valor: ')),
         int(input('Digite o 4º valor: ')), int(input('Digite o 5º valor: '))]
mai = men = 0
pos1 = pos2 = ''
for c in range(len(lista)):
    if c == 0:
        mai = lista[c]
        men = mai
    if lista[c] > mai:
        mai = lista[c]
    elif lista[c] < men:
        men = lista[c]
for c, v in enumerate(lista):
    if mai == lista[c]:
        pos1 += str(c)+'...'
    elif men == lista[c]:
        pos2 += str(c)+'...'

print(f'Você digitou os valores: {lista}')
print(f'O maior valor foi {mai} nas posições {pos1}.')
print(f'O menor valor foi {men} nas posições {pos2}.')
