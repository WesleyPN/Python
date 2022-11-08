i = int(input('Digite sua idade: '))
c = ['MIRIN', 'INFANTIL', 'JUNIOR', 'SENIOR', 'MASTER']
if i <= 9:
    print('Com {} anos, sua categoria é {}'.format(i, c[0]))
elif i <= 14:
    print('Com {} anos, sua categoria é {}'.format(i, c[1]))
elif i <= 19:
    print('Com {} anos, sua categoria é {}'.format(i, c[2]))
elif i == 20:
    print('Com {} anos, sua categoria é {}'.format(i, c[3]))
else:
    print('Com {} anos, sua categoria é {}'.format(i, c[4]))
