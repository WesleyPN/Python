from time import sleep


def contador(inicio, fim, passo):
    if inicio < fim and passo > 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        for n in range(inicio, (fim+1), passo):
            print(n, end=' ', flush=True)
            sleep(0.5)
        print()
    elif inicio < fim and passo == 0:
        passo += 1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        for n in range(inicio, (fim+1), passo):
            print(n, end=' ', flush=True)
            sleep(0.5)
        print()
    elif inicio < fim and passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo*-1} em {passo*-1}:')
        for n in range(inicio, (fim+1), (passo*-1)):
            print(n, end=' ', flush=True)
            sleep(0.5)
        print()

    elif inicio > fim and passo > 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        for n in range(inicio, (fim-1), (passo*-1)):
            print(n, end=' ', flush=True)
            sleep(0.5)
        print()
    elif inicio > fim and passo == 0:
        passo += 1
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
        for n in range(inicio, (fim-1), (passo*-1)):
            print(n, end=' ', flush=True)
            sleep(0.5)
        print()
    elif inicio > fim and passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo*-1} em {passo*-1}:')
        for n in range(inicio, (fim-1), passo):
            print(n, end=' ', flush=True)
            sleep(0.5)
        print()


contador(1, 10, 1)
print('-='*30)
contador(10, 0, 2)
print('-='*30)
i = int(input('Digite o início da contagem: '))
f = int(input('Digite o fim da contagem: '))
p = int(input('Digite o passo da contagem: '))
print('-='*30)
contador(i, f, p)
