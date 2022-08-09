from math import pow, sqrt, hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h2 = pow(co,2) + pow(ca, 2)
h = sqrt(h2)
print('O comprimento da hipotenusa é  {:.2f}'.format(h))
print('O comprimento da hipotenusa é  {:.2f}'.format(hypot(co, ca)))
