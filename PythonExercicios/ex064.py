n = 0
s = 0
c = 0
while n != 999:
    n = float(input('Digite um número qualquer [Para sair digite 999]: '))
    if n != 999:
        s += n
        c += 1
print('A soma de todos os {} números digitados é {}'.format(c, s))
