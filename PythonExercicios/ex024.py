c = str(input('Digite o nome de uma cidade: ')).upper()
c2 = c.split()
if c2[0].count('SANTO'):
    print('O nome da cidade começa com {}'.format(c2[0]))
else:
    print('O nome da cidade não começa com SANTO, mas sim com {}'.format(c2[0]))
