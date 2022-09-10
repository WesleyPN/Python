def escreva(txt):
    linha = '~' * int(len(txt)+4)
    print(linha)
    print(f'{txt}'.center(len(linha)))
    print(linha)


escreva('Wesley Pinheiro')
escreva('Curso de Python no YouTube')
escreva('CeV')
titulo = str(input('Digite um texto: ')).title().strip()
escreva(titulo)
