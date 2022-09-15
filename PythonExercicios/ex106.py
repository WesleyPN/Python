from time import sleep


def escreva(txt, cor='Fim'):
    linha = '~' * int(len(txt)+4)
    print(cores[cor], end='')
    print(linha)
    print(f'{txt}'.center(len(linha)))
    print(linha)
    print(cores['Fim'], end='')
    sleep(1)


def manual(txt):
    escreva(f"Acessando o manual do comando \'{txt}\'", 'Azul')
    print(cores['Branco'])
    help(txt)
    print(cores['Fim'], end='')
    sleep(2)


cores = {'Fim': '\033[m',
         'Branco': '\033[7;40m',
         'Vermelho': '\033[0;41m',
         'Verde': '\033[0;42m',
         'Amarelo': '\033[0;43m',
         'Azul': '\033[0;44m',
         'Magenta': '\033[0;45m',
         'Ciano': '\033[0;46m',
         'Cinza': '\033[0;47m'}

while True:
    escreva('SISTEMA DE AJUDA PyHELP', 'Verde')
    c = str(input('Função ou Biblioteca > ')).strip()
    m = ''
    fim = False
    if c.upper().strip() == 'FIM':
        escreva(f'ATÉ LOGO!', 'Vermelho')
        break
    else:
        manual(c)
