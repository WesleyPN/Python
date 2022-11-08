def leiaInt(txt=''):
    cond = False
    val = 0
    while True:
        num = str(input(txt)).strip()
        if num.isnumeric():
            val = int(num)
            cond = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if cond:
            break
    return num

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
