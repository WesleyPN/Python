f = str(input('Digite uma frase: ')).upper()
f2 = ''.join(f.split())
fc = str('')
for i in range(0, len(f), 1):
    fc = f[i].strip()+fc
if f2 == fc:
    print('A frase "{}" é um palíndromo'.format(f))
else:
    print('A frase "{}" não é um palíndromo'.format(f))
