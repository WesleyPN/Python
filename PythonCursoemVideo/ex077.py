palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    vogais = ''
    for v in p:
        if v.upper() in 'AEIOU':
            vogais += v+' '
    print(f'Na palavra {p.upper()} temos {vogais}')
