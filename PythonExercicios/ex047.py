print('os número pares que estão no intervalo entre 1 e 50 são:')
par = str('')
for c in range(1, 51, 2):
    if c+1 == 48:
        par += str(c + 1) + " e "
    elif c+1 == 50:
        par += str(c + 1) + "!"
    else:
        par += str(c+1)+", "
print(par)
