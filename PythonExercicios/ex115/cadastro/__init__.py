def cadastropessoas():
    try:
        nome = str(input('Nome: ')).title().strip()
        while True:
            try:
                idade = int(input('Idade: '))
                if type(idade) == int:
                    break
            except (ValueError, TypeError):
                print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
        with open('ex115.txt', 'a+') as f:
            f.write(f'{nome:30}\t{idade:5>} anos\n')
        print(f'Novo registro de {nome} adicionado.')
    except KeyboardInterrupt:
        print('\033[31mUsuário encerrou o programa. Até logo!\033[m')
        exit()


def exibepessoas():
    from time import sleep
    try:
        pessoas = list()
        with open('ex115.txt', 'r+') as f:
            for p in f:
                pessoas.append(p.replace('\n', ''))
            for c in range(0, len(pessoas)):
                print(pessoas[c])
    except FileNotFoundError:
        print('Criando arquivo,aguarde', end='', flush=True)
        for c in range(0, 3):
            sleep(1)
            print(' . ', end='')
        with open('ex115.txt', 'a+') as f:
            f.write('')
        print('Arquivo criado com sucesso!')
        print('-' * 50)
