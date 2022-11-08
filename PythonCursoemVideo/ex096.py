def área(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}M²')


lar = float(input('Digite a largura em metros do terreno: '))
com = float(input('Digite o comprimento em metros do terreno: '))

área(lar, com)
