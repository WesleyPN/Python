lista = []
mai = men = 0
posmai = posmen = ''
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a {c}º posição: ')))
    if c == 0:
        mai = lista[c]
        men = mai
    if lista[c] > mai:
        mai = lista[c]
    elif lista[c] < men:
        men = lista[c]
for c, v in enumerate(lista):
    if mai == v:
        posmai += str(c) + '...'
    elif men == v:
        posmen += str(c) + '...'

print(f'Você digitou os valores: {lista}')
print(f'O maior valor foi {mai} nas posições {posmai}.')
print(f'O menor valor foi {men} nas posições {posmen}.')
