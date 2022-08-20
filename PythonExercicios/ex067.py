while True:
    n = int(input('Qual tabuada você quer saber? '))
    if n < 0:
        break
    print('-='*20)
    print(f'Tabuada do {n}')
    print('-=' * 20)
    for c in range(0, 10):
        print(f'{n} x {(c+1):>2} = {n*(c+1)}')
    print('-=' * 20)
