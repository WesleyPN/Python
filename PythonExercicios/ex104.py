def leiaInt(txt=''):
    while True:
        num = input(txt)
        if num.isnumeric():
            return num
        else:
            print('ERRO! Digite um número inteiro válido.')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
