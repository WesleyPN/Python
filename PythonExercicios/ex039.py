from datetime import date
a = int(input('Em que ano você nasceu: '))
v = date.today().year - a
if v < 18:
    print('Faltam {} anos pra você se alistar.'.format((18-v)))
elif v > 18:
    print('Seu alistamento está {} ano(s) atrasado.'.format(v - 18))
else:
    print('Este ano você completa ou completou 18 anos. Está na hora de se alistar.')
