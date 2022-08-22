an = ''
ap = cm = mp =  0
print('--'*20)
print('     LOJA SUPER BARATÃO')
print('--'*20)
while True:
    np = str(input('Nome do Produto: '))
    pp = float(input('Preço: R$'))
    ap += pp
    if pp > 1000:
        cm += 1
    if ap == pp:
        an = np
        mp = pp
    elif pp < mp:
        an = np
        mp = pp
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        print('-------------FIM DO PROGRAMA-------------')
        break
print(f'O total da compra foi: R${ap:.2f}')
print(f'Temos {cm} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {an.capitalize()} que custa R${mp:.2f}')
