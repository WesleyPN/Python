num = []
par = []
imp = []
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        par.append(n)
        par.sort()
    else:
        imp.append(n)
        imp.sort()
num.append(par[:])
num.append(imp[:])
print('-='*30)
print(f'Os números pares são: {num[0]}')
print(f'Os números ímpares são: {num[1]}')
