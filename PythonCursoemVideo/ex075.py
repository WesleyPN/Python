n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))
n4 = int(input('Digite o 4º número: '))
tn = (n1, n2, n3, n4)
pares = ''
men3 = ''
for c in range(0, len(tn)):
    if 3 in tn:
        men3 = f'O valor 3 apareceu na {tn.index(3) + 1}ª posição'
    else:
        men3 = f'O valor 3 não foi digitado em nenhuma posição'
    if int(tn[c]) % 2 == 0:
        pares += str(tn[c])+' '
print(f'Você digitou os valores {tn}')
print(f'O valor 9 apareceu {tn.count(9)} vezes')
print(men3)
print(f'Os valores pares digitados foram {pares}')
