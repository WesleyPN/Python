"""teste = list()
teste.append('Wesley')
teste.append(29)
galera = list()
galera.append(teste[:])
teste[0] = 'Karen'
teste[1] = 25
galera.append(teste[:])
print(galera)"""
#----------
"""galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')"""
#--------
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        totmai += 1
        print(f'{p[0]} é maior de idade')
    else:
        totmen += 1
        print(f'{p[0]} é menor de idade')

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
