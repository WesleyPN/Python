m3x3 = [[], [], []], [[], [], []], [[], [], []]
for lin in range(0, 3):
    for col in range(0, 3):
        m3x3[lin][col] = int(input(f'Digite um valor para a posição {lin}x{col} da matriz: '))
print('-='*30)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{m3x3[lin][col]:^5}]', end='')
    print()
