from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p,fmt=True)} é {moeda.metade(p,fmt=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10,fmt=True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
