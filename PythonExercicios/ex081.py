ln = []
c = 0
while True:
    n = int(input('Digite um número: '))
    ln.append(n)
    ln.sort(reverse=True)
    c += 1

    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        print('-='*30)
        break

print(f'Foram digitados {c} números')
print(f'Os valores em ordem decrescente são {ln}')
print('O valor 5 faz parte da lista!' if 5 in ln else 'O valor 5 NÃO faz parte da lista!')
