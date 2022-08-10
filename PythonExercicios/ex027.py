n = str(input('Digite o nome completo: '))
n2 = n.split()
un = int(len(n2))-1
print('O primeiro nome é {}'.format(n2[0]))
print('O ultimo nome é {}'.format(n2[un]))
