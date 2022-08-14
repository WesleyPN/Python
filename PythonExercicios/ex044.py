p = float(input('Digite o preço do produto: '))
print('Escolha a forma de pagamento:')
print('1 - À vista em dinheiro ou cheque')
print('2 - À vista no cartão')
print('3 - 2x no cartão')
print('4 - 3x ou mais no cartão')
fp = int(input(''))
if fp == 1:
    v = p - (p * 0.1)
    print('Pagando à vista em dinheiro ou cheque o preço total fica R${} com 10% de desconto.'.format(v))
elif fp == 2:
    v = p - (p * 0.05)
    print('Pagando à vista no cartão o preço total fica R${} com 5% de desconto.'.format(v))
elif fp == 3:
    v = p
    print('Pagando em 2x no cartão o preço total fica R${} sem desconto.'.format(v))
else:
    v = p + (p * 0.2)
    print('Pagando em 3x ou mais no cartão o preço total fica R${} com 20% de juros.'.format(v))
