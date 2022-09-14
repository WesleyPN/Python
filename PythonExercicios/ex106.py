def escreva(txt):
    linha = '~' * int(len(txt)+4)
    print(linha)
    print(f'{txt}'.center(len(linha)))
    print(linha)


def manual():
    while True:
        escreva('SISTEMA DE AJUDA PyHELP')
        c = str(input('Digite o comando: ')).strip()
        m = ''
        fim = False
        if c.upper().strip() == 'FIM':
            fim = True
        else:
            m = str(help(c))
        if fim:
            break
    return f'\033[7;30m{m}\033[m'


manual()
