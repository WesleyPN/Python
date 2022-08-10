f = str(input('Digite uma frase: '))
print('Nesta frase a letra "A" aparece {} vezes'.format(f.lower().count('a')))
print('A letra "A" aparece primeiro na posição {}'.format(f.find('a')))
print('A letra "A" aparece por ultimo na posição {}'.format(f.rfind('a')))
