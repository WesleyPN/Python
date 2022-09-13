def leiaInt(txt=''):
    while True:
        num = str(input(txt)).strip()
        if num.isnumeric():
            return num
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
