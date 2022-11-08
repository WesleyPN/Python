from datetime import date
ma = 0
me = 0
for i in range(0, 7):
    a = int(input('Em que ano a {}ª pessoa nasceu? '.format(i+1)))
    if date.today().year - a >= 21:
        ma += 1
    else:
        me += 1
print('{} pessoa(s) ainda não atingiram a maioridade e {} pessoa(s) já são maior de idade'.format(me, ma))
