em = list(str(input('Digite a expressão: ')))
cont = 0
for c, v in enumerate(em):
    if v == '(':
        cont += 1
    elif v == ')':
        cont -= 1
if cont == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
