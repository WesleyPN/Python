s = c = 0
while True:
    n = int(input('Digite um número: (999 para sair)'))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados {c} números e a soma total é {s}')
