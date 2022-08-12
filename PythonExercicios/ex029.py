v = float(input('Digite a velocidade do carro: '))
m = (v - 80) * 7
if v > 80:
    print('Você foi multado em R${:.2f} por estar a {:.1f}Km/h em uma via de 80Km/h'.format(m, v))
else:
    print('Tenha um bom dia. Dirira com cuidado!')
