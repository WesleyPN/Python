ma = 0
me = 99999
for i in range(0, 5):
    p = float(input('Qual o peso da {}ª pessoa? '.format(i+1)))
    if p >= ma:
        ma = p
    elif p <= me:
        me = p
print('O maior peso é {}Kg e o menor peso é {}Kg'.format(ma, me))
