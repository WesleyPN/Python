s = float(input('Qual o seu salário? '))
if s > 1250:
    ns = s + (s * 0.1)
    print('O seu novo salário com o reajuste de 10% é de R${:.2f}'.format(ns))
else:
    ns = s + (s * 0.15)
    print('O seu novo salário com o reajuste de 15% é de R${:.2f}'.format(ns))
