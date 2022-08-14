n = str(input('Qual é seu nome? '))
if n == 'Wesley':
    print('Que nome bonito!')
elif n == 'Pedro' or n == 'Maria' or n == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif n in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(n))
