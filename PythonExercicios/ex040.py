n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('Você foi REPROVADO!')
elif 5 <= m <= 6.9:
    print('Você está de RECUPERAÇÂO. Estude mais!')
else:
    print('Parabéns, você foi APROVADO')
