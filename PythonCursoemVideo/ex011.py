l = float(input('Informe a largura da parede: '))
a = float(input('Informe a altura da parede: '))
p = (l*a)
t = p/(2**2)
print('A parede tem {:.2f}m² e para pintar serão necessários {:.2f}L de tinta'.format(p, t))
