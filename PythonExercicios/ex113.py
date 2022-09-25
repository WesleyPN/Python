def leiaInt(txt=''):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def leiaFloat(txt=''):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número decimal válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


i = leiaInt('Digite um Inteiro: ')
f = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')
