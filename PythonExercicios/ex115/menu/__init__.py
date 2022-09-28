from ex115 import cadastro
from time import sleep


def titulo(txt=''):
    print('-' * 50)
    print(txt.center(50))
    print('-' * 50)


def menu():
    print('\033[33m1 -\033[m \033[34mVer pessoas cadastradas\033[m')
    print('\033[33m2 -\033[m \033[34mCadastrar nova Pessoa\033[m')
    print('\033[33m3 -\033[m \033[34mSair do Sistema\033[m')
    print('-' * 50)


def cadpessoa():
    while True:
        print('\033[42m', end='')
        titulo('MENU PRINCIPAL')
        print('\033[m', end='')
        menu()
        try:
            opcao = int(input('\033[33mSua Opção:\033[m '))
            if opcao == 1:
                print('\033[30;43m', end='')
                titulo('PESSOAS CADASTRADAS')
                print('\033[m', end='')
                print('\033[7;40m', end='')
                cadastro.exibepessoas()
                print('\033[m', end='')

                sleep(1)
            elif opcao == 2:
                print('\033[30;44m', end='')
                titulo('NOVO CADASTRO')
                print('\033[m', end='')
                cadastro.cadastropessoas()
                sleep(1)
            elif opcao == 3:
                print('\033[30;41m', end='')
                titulo('Saindo do sistema... Até logo!')
                print('\033[m', end='')
                break
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[m')
        except (TypeError, ValueError):
            print('ERRO! Por favor, digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\033[31mUsuário encerrou o programa. Até logo!\033[m')
            break
