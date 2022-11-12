"""
Um problema conhecido de matemática a conjectura de Collatz. 
Ela diz que dado qualquer N, se você aplicar repetidas vezes a seguinte função:

f(N)=N/2, se N é par

f(N)=3⋅N+1, se N é impar

o valor eventualmente será igual a 1. 
Agora faça um programa que diz o número de vezes que a função é chamada 
antes que o valor de N seja igual a 1
Entrada

A entrada contem um único número N.
Saída

A quantidade de vezes que temos que aplicar a função para que N se torne igual a 1.
Restrições

    1<=N<=100000
"""
#---------------------------------------------
def collatz (numero):
    numero = int(input("Digite um número: "))
    contador = [numero]
    while numero != 1:
        if (numero % 2) == 0:
            numero = numero/2
        else:
            numero = 3*numero+1
        contador.append(int(numero))
    contador.pop()
    return contador


cont = 0
for v in (collatz(1)):
    cont += 1
print(cont)
#---------------------------------------------
