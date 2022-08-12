#-------------------------------Minha Resolução-----------------------------------
d = float(input('Digite a distância da viagem: '))
if d <= 200:
    p = d * 0.5
else:
    p = d * 0.45
print ('O preço da passagem para uma viagem de {}Km é de R${:.2f}'.format(d, p))
#-------------------------------Resolução do Professor----------------------------
#d = float(input('Qual a distância da sua viagem? '))
#p = d * 0.5 if d <= 200 else d * 0.45
#print('O preço de sua passagem será de R${:.2f}'.format(p))
