#-------------------------------Minha Resolução-----------------------------------
a = int(input('Digite um ano: '))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print('O ano {} é um ano bissexto'.format(a))
else:
    print('O ano {} não é um ano bissexto'.format(a))
#-------------------------------Resolução do Professor----------------------------
#from datetime import date
#a = int(input('Que ano que analizar? Coloque 0 para analizar o ano atual: '))
#if a == 0:
#    a = date.today().year
#if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
#    print('O ano {} é um ano bissexto'.format(a))
#else:
#    print('O ano {} não é um ano bissexto'.format(a))
