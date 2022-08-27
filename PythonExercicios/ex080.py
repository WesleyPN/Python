num = []
for i in range(0, 5):
    n = int(input(f'Digite o {i+1}º valor: '))
    for c, v in enumerate(num):
        if n < v:
            num.insert(c, n)
            print(f'Adicionado na posição {c} da lista...')
            break
    else:
        num.append(n)
        print('Adicionado no final da lista...')

print(f'Os valores digitados, ordenados de forma crescente são: {num}')
