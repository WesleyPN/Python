from random import choice
print('-=-'*20)
print('Vamos jogar Jokenpô')
print('Escolha entre PEDRA, PAPEL ou TESOURA:')
print('-=-'*20)
p = str(input('').upper())
lista = ['PEDRA', 'PAPEL', 'TESOURA']
c = choice(lista)
if p == c:
    print('EMPATAMOS! Eu escolhi {} e você escolheu {}.'.format(c, p))
elif (p == 'PEDRA' and c == 'TESOURA') or (p == 'PAPEL' and c == 'PEDRA') or (p == 'TESOURA' and c == 'PAPEL'):
    print('VOCÊ VENCEU! Eu escolhi {} e você escolheu {}.'.format(c, p))
else:
    print('VOCÊ PERDEU! Eu escolhi {} e você escolheu {}.'.format(c, p))
