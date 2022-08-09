from math import sin, cos, tan, radians
a = float(input('Digite o valor do ângulo'))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
if a == float(90) or a == float(270):
    t = str('inexistente')
    print('O ângulo {}º tem o seno {:.4f}, o cosseno {:.4f} e tangente {}'.format(a, s, c, t))
else:
    print('O ângulo {}º tem o seno {:.4f}, o cosseno {:.4f} e tangente {:.4f}'.format(a, s, c, t))
