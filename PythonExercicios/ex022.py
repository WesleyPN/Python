n = str(input('Digite o nome completo: '))
print(n.upper())
print(n.lower())
n2 = n.split()
print('O nome todo tem {} letras'.format(len(''.join(n2))))
print('O primeiro nome tem {} letras'.format(len(n2[0])))