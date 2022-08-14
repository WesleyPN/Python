from random import choice
from time import sleep
print('-=-'*20)
print('Vamos jogar Jokenpô')
print('Escolha entre PEDRA, PAPEL ou TESOURA:')
print('-=-'*20)
p = str(input('Jogador> ').upper())
lista = ['PEDRA', 'PAPEL', 'TESOURA']
c = choice(lista)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-'*20)
if p in lista:
    if p == c:
        print('EMPATAMOS! Eu escolhi {} e você escolheu {}.'.format(c, p))
    elif (p == 'PEDRA' and c == 'TESOURA') or (p == 'PAPEL' and c == 'PEDRA') or (p == 'TESOURA' and c == 'PAPEL'):
        print('VOCÊ VENCEU! Eu escolhi {} e você escolheu {}.'.format(c, p))
    else:
        print('VOCÊ PERDEU! Eu escolhi {} e você escolheu {}.'.format(c, p))
else:
    print('Opção inválida. tente novamente')
