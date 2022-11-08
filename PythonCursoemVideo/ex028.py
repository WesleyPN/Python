from random import randint
#-------------------------------Minha Resolução-----------------------------------
n = randint(0, 5)
n2 = int(input('Entre 0 e 5, qual número estou pensando? '))
if n == n2:
    print('Você acertou! o número que estou pensando é {}'.format(n))
else:
    print('Você errou! O número que estou pensando é {} e não {}'.format(n, n2))

#-------------------------------Resolução do Professor----------------------------
#from random import randint
#from time import sleep
#n = randint(0, 5)
#print('-=-' * 20)
#print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
#print('-=-' * 20)
#j = int(input('Em que número eu pensei? '))
#print('Processando...')
#sleep(3)
#if j == n:
#    print('Parabéns! Você conseguiu me vencer!')
#else:
#    print('Ganhei! Eu pensei no número {} e não no {}'.format(n, j))
