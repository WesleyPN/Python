print('=='*20)
print('{:^40}'.format('BANCO WPN'))
print('=='*20)
n = int(input('Quanto deseja sacar? R$'))
r = n
v50 = v20 = v10 = v1 = 0
while True:
    if r >= 50:
        v50 = r // 50
        r -= v50 * 50
    elif 50 > r >= 20:
        v20 = r // 20
        r -= v20 * 20
    elif 20 > r >= 10:
        v10 = r // 10
        r -= v10 * 10
    elif 10 > r >= 1:
        v1 = r // 1
        r -= v1 * 1
    else:
        break
print(f'Total de {v50} cédulas de R$50')
print(f'Total de {v20} cédulas de R$20')
print(f'Total de {v10} cédulas de R$10')
print(f'Total de {v1} cédulas de R$1')
print('=='*20)
print('Volte sempre ao BANCO WPN! Tenha um bom dia!')
