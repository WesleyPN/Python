n = int(input('Digite um número: '))
c = 0
fib = ''
ult = 1
pen = 1
pxm = 0
while c < n:
    if c == 0:
        fib += str(0)+' - '
    elif c == 1 or c == 2:
        fib += str(1)+' - '
    else:
        pxm = pen + ult
        pen = ult
        ult = pxm
        fib += str(ult)+' - '
    c += 1
print(fib+'Fim')
