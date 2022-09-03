m3x3 = [[], [], []], [[], [], []], [[], [], []]
par = stc = mai = 0
for lin in range(0, 3):
    for col in range(0, 3):
        m3x3[lin][col] = int(input(f'Digite um valor para a posição {lin}x{col} da matriz: '))
        if m3x3[lin][col] % 2 == 0:
            par += int(m3x3[lin][col])
        if col == 2:
            stc += m3x3[lin][col]
        if m3x3[lin][col] > mai and lin == 1:
            mai = m3x3[lin][col]
print('-='*30)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{m3x3[lin][col]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares digitados é: {par}')
print(f'A soma dos valores da terceira coluna é: {stc}')
print(f'O maior valor da segunda linha é: {mai}')
