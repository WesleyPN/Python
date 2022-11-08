from datetime import date
apo = dict()
apo['Nome'] = str(input('Nome: ')).title()
apo['Idade'] = (date.today().year - int(input('Ano de nascimento: ')))
apo['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if apo['CTPS'] != 0:
    apo['AnoCont'] = int(input('Ano de contratação: '))
    apo['Salário'] = float(input('Salário: '))
    apo['IdadeApo'] = apo['Idade'] + ((apo['AnoCont']+35) - date.today().year)
for k, v in apo.items():
    print(f'{k} tem o valor {v}')
