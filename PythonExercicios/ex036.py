print('Para que o empréstimo para a compra da casa seja aprovado, \nprecisamos que nos informe a seguir alguns dados:')
vc = float(input('Informe o valor do imóvel: '))
s = float(input('Informe o seu salário: '))
a = int(input('Informe em quantos anos pretende pagar: '))
p = vc/(a * 12)

if p <= (s * 0.3):
    print('Parabéns! O empréstimo foi aprovado.')
else:
    print('Infelizmente você não pode financiar esta casa. O empréstimo não foi aprovado.')
