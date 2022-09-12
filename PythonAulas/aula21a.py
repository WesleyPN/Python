def fatorial (num=1):
    f = 1
    for c in range(num, 0,-1):
        f *= c
    return f

    
def par(n=0):
    if n%2==0:
        return True
    else:
        return False



numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é igual a {fatorial(numero)}')
f1=fatorial(5)
f2=fatorial(4)
f3=fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

if par(numero):
    print(f'{numero} é par')
else:
    print(f'{numero} é ímpar')
