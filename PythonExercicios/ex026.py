f = str(input('Digite uma frase: ')).upper().strip()
print('Nesta frase a letra "A" aparece {} vezes'.format(f.count('A')))
print('A letra "A" aparece primeiro na posição {}'.format(f.find('A')+1))
print('A letra "A" aparece por ultimo na posição {}'.format(f.rfind('A')+1))
