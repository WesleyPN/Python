num = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
    'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Desesseis', 'Desessete', 'Desoito', 'Desenove', 'Vinte')
r = 'S'
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n < 0 or n > 20:
        n = int(input('Valor inválido. Por favor, digite um número entre 0 e 20: '))

    print(f'O número {n} escrito por extenso é "{num[n]}"')

    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r == 'N':
        break
