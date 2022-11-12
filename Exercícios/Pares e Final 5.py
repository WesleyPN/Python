"""
Pares ou com Último Algarismo Igual a 5

Bino encontrou 3 números inteiros X, Y e Z, e gostaria de saber quantos desses números 
são pares OU terminam com o algarismo 5.
Entrada

A entrada consiste de três linhas. A primeira linha contém um inteiro X. 
A segunda linha contém um inteiro Y. A terceira linha contém um inteiro Z.
Saída

A saída consiste de uma linha contendo a quantidade de números lidos que são pares ou 
tem o último algarismo igual a 5.
Restrições

    Os inteiros X, Y e Z são inteiros distintos, com valores entre 1 e 1000, inclusive.
"""
#----------------------------------------------------------------------------------------------
num = [int(input("Digite o primeiro número: ")),
       int(input("Digite o segundo número: ")),
       int(input("Digite o terceiro número: "))]
cont = 0
for n in num:
    if n % 2 == 0:
        cont += 1
    elif str(n)[-1]=="5":
        cont += 1

print(cont)
#----------------------------------------------------------------------------------------------
