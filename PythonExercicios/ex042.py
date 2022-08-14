r1 = float(input('Digite o valor do 1º lado do triângulo: '))
r2 = float(input('Digite o valor do 2º lado do triângulo: '))
r3 = float(input('Digite o valor do 3º lado do triângulo: '))
if (r1+r2) > r3 and (r1+r3) > r2 and (r2+r3) > r1:
    print('As retas com valores {:.1f}, {:.1f} e {:.1f} formam um triângulo'.format(r1, r2, r3))
    if r1 == r2 == r3:
        print('Por ter os três lados iguais, este é um triângulo EQUILÁTERO')
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print('Por ter os dois lados iguais, este é um triângulo ISÓSCELES')
    else:
        print('Por ter todos os lados diferentes, este é um triângulo ESCALENO')
else:
    print('As retas com valores {:.1f}, {:.1f} e {:.1f} NÂO formam um triângulo'.format(r1, r2, r3))
