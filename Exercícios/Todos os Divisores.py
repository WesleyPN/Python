"""
Todos os Divisores

Dado um número inteiro X, encontre todos os divisores de X.
Entrada

A entrada consiste de apenas uma linha contendo o número X.
Saída

A saída do seu programa deve conter apenas uma linha com os divisores de X separados por um espaço em branco.
Os divisores devem ser impressos em ordem crescente.
Restrições

    2 <= X <= 10⁹
"""
#---------------------------------------
i = int(input("Digite um número: "))
n = float(i)
for n in range(2, i+1):
    if i <= pow(10, 9):
        if i % n == 0:
            print(n, end=' ')
    else:
        break
#---------------------------------------
"""
while True:
    i = int(input("Digite um número: "))
    n = float(i)
    c = 'S'
    for n in range(2, i+1):
        if i <= pow(10, 9):
            if i % n == 0:
                print(n, end=' ')
        else:
            print("Por favor, informe um valor menor ou igual a 10⁹")
            break
    print()
    c = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if c in "Nn":
        break
"""
