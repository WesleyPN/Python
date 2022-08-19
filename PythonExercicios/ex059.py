n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
m = 0
r = 0
while m != 5:
    print('-=-' * 20)
    print('Escolha entre as opções a seguir:')
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos números \n[5] Sair')
    print('-=-' * 20)
    m = int(input('>'))

    if m == 1:
        r = n1 + n2
        print('A soma de {} e {} é {}'.format(n1, n2, r))
    elif m == 2:
        r = n1 * n2
        print('A multiplicação de {} e {} é {}'.format(n1, n2, r))
    elif m == 3:
        if n1 > n2:
            r = n1
        else:
            r = n2
        print('O maior número é {}'.format(r))
    elif m == 4:
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif m == 0 or m > 5:
        print('Opção inválida! Tente novamente')
