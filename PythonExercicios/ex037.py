d = int(input('Digite um número para converção: '))
c = int(input('Digite 1 para conversão em binário. \nDigite 2 para conversão em octal. \nDigite 3 para conversão em hexadecimal.\n'))
if c == 1:
    b = str(bin(d))
    print('{} em binário é {}'.format(d, b[2::]))
elif c == 2:
    o = str(oct(d))
    print('{} em octal é {}'.format(d, o[2::]))
else:
    h = str(hex(d)).upper()
    print('{} em hexadecimal é {}'.format(d, h[2::]))
