def leiaInt(txt=''):
    cond = False
    val = 0
    try:
        while True:
            try:
                num = str(input(txt)).strip()
                val = int(num)
                cond = True
                if cond:
                    break
            except (ValueError, TypeError):
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    except KeyboardInterrupt:
        num = 0
        print('\033[31mUsuario preferiu não digitar esse número.\033[m')
    return num


def leiaFloat(txt=''):
    cond = False
    val = 0
    try:
        while True:
            try:
                num = str(input(txt)).strip()
                val = float(num)
                cond = True
                if cond:
                    break
            except (ValueError, TypeError):
                print('\033[31mERRO! Digite um número decimal válido.\033[m')
    except KeyboardInterrupt:
        num = 0
        print('\033[31mUsuario preferiu não digitar esse número.\033[m')
    return num


i = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')
