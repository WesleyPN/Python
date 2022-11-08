#minha solução
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
print('-='*30)
print(f'Os valores digitados, ordenados de forma crescente são: {num}')
#solução do professor
#num = []
#for c in range(0, 5):
#    n = int(input('Digite um valor: '))
#    if c == 0 or n > num[-1]:
#        num.append(n)
#        print('Adicionado no final da lista...')
#    else:
#        pos = 0
#        while pos < len(num):
#            if n <= num[pos]:
#                num.insert(pos, n)
#                print(f'Adicionado na posição {pos} da lista...')
#                break
#            pos += 1
#print('-='*30)
#print(f'Os valores digitados, ordenados de forma crescente são: {num}')
