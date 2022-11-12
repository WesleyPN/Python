"""
Xadrez

No tabuleiro de xadrez, a casa na linha 1, coluna 1 (canto superior esquerdo) é sempre branca 
e as cores das casas se alternam entre branca e preta, de acordo com o padrão conhecido como...xadrez! 
Dessa forma, como o tabuleiro tradicional tem oito linhas e oito colunas, 
a casa na linha 8, coluna 8 (canto inferior direito) será também branca. 
Neste problema, entretanto, queremos saber a cor da casa no canto inferior direito de um tabuleiro 
com dimensões quaisquer: L linhas e C colunas. No exemplo da figura, para L=6 e C=9, 
a casa no canto inferior direito será preta!

Figura 1 = https://api.neps.academy/image/1300.png
Entrada

A primeira linha da entrada contém um inteiro L indicando o número de linhas do tabuleiro. 
A segunda linha da entrada contém um inteiro C representando o número de colunas.
Saída

Imprima uma linha na saída. A linha deve conter um inteiro, representando a cor 
da casa no canto inferior direito do tabuleiro: 1, se for branca; e 0, se for preta.
Restrições

    1<=L,C<=1000
"""
#----------------------------------------------------------------------------------------------
l = int(input("Informe o número de linhas: "))
c = int(input("Informe o número de colunas: "))
vl = list()
vc = list()
for linha in range(0, l):
    vc.clear()
    for coluna in range(0, c):
        if linha % 2 == 0:
            if coluna % 2 == 0:
                vc.append(1)
            else:
                vc.append(0)
        else:
            if coluna % 2 != 0:
                vc.append(1)
            else:
                vc.append(0)
    vl.append(vc[:])

#print(vl)
print(vl[l-1][c-1])
#----------------------------------------------------------------------------------------------    
