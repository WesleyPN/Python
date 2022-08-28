ln = []
while True:
    n = int(input('Digite um número: '))
#    ln.append(n)
#    cont = 0
#    for c in range(0, len(ln)):
#        if n == ln[c]:
#            cont += 1
#        if cont >= 2:
#            ln.pop(c)
    if n not in ln:
        ln.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        ln.sort()
        break
print('-='*30)
print(f'Você digitou os valores: {ln}')
