m3 = 0
for c in range(1, 501, 2):
    if c % 3 == 0 and c % 2 != 0:
        m3 += c
print('A soma de todos os ímpares múltiplos de 3 entre 1 e 500 é {}'.format(m3))
