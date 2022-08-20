from random import randint
cv = bool(True)
c = 0
print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*20)
while True:
    nc = randint(1, 10)
    if not cv:
        break
    n = int(input('Digite um número: '))
    ip = n+nc
    e = str(input('Escolha, PAR ou IMPAR? [P/I] ')).upper().strip()[0]
    while e not in 'PpIi':
        e = str(input('Escolha, PAR ou IMPAR? [P/I] ')).upper().strip()[0]
    if ip % 2 == 0 and e in 'Pp':
        e = 'PAR'
        c += 1
        print('--' * 20)
        print('Você VENCEU!')
    elif ip % 2 != 0 and e in 'Ii':
        e = 'IMPAR'
        c += 1
        print('--' * 20)
        print('Você VENCEU!')
    elif ip % 2 != 0 and e in 'Pp':
        cv = False
        e = 'IMPAR'
        print('-*' * 20)
        print(f'Você PERDEU! \nFIM DE JOGO! Você teve {c} vitórias consecutivas')
    elif ip % 2 == 0 and e in 'Ii':
        cv = False
        e = 'PAR'
        print('-*' * 20)
        print(f'Você PERDEU! \nFIM DE JOGO! Você teve {c} vitórias consecutivas')
    print(f'Eu escolhi {nc} e você escolheu {n}. O resultado foi {ip} ({e}).')
