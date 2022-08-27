ln = []
lp = []
li = []
while True:
    n = int(input('Digite um número: '))
    ln.append(n)
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        print('-='*30)
        break
for c, v in enumerate(ln):
    if v % 2 == 0:
        lp.append(v)
    else:
        li.append(v)
print(f'Os valores digitados foram: {ln}')
print(f'Os pares são: {lp}')
print(f'Os impares são: {li}')
