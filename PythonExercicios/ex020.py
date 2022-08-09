from random import shuffle
a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2º aluno: ')
a3 = input('Digite o nome do 3º aluno: ')
a4 = input('Digite o nome do 4º aluno: ')
list = [a1, a2, a3, a4]
shuffle(list)
print('A ordem de apresentação é ')
print('1º', list.__getitem__(0))
print('2º', list.__getitem__(1))
print('3º', list.__getitem__(2))
print('4º', list.__getitem__(3))
