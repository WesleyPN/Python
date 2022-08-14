p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
imc = p / (a ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.2f}. Você está abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.2f}. Você está com o peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.2f}. Você está com sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.2f}. Você está com obesidade'.format(imc))
else:
    print('Seu IMC é de {:.2f}. Você está com obesidade mórbida'.format(imc))
