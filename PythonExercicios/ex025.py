n = str(input('Digite seu nome completo: '))
n2 = n.upper().split()
if n2.count('SILVA'):
    print('O nome possui "Silva"')
else:
    print ('O nome não possui Silva')
