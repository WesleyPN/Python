s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    s += n
    c += 1
print(f'A soma de todos os {c} números é {s}')
