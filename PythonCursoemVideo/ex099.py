from time import sleep


def maior(*num):
    maiorNumero = 0
    print('Analizando os valores passados...')
    for c, n in enumerate(num):
        print(n, end=' ',flush=True)
        sleep(0.5)
        if c == 0:
            maiorNumero = n
        elif n >= maiorNumero:
            maiorNumero = n
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior número é {maiorNumero}')


print('-='*30)
maior(2, 9, 4, 5, 7, 1)
print('-='*30)
maior(4, 7, 2)
print('-='*30)
maior(1, 2)
print('-='*30)
maior(6)
print('-='*30)
maior()
