# minha resolução
t = 10
pt = int(input('Digite o primeiro termo da PA.: '))
r = int(input('Digeite a razão da PA.: '))
ut = pt + (t - 1) * r
pa = ''
while t != 0:
    for c in range(pt, ut+1, r):
        pa += str(c)+' - '
    print(pa+'Fim')
    t = int(input('Quer exibir mais quantos termos da PA.? '))
    if t != 0:
        pa = ''
        pt = c + r
        ut = pt + (t - 1) * r
# resolução do professor
'''print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo +=razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
'''
