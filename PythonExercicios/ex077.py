palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for c in range(0, len(palavras)):
    p = str(palavras[c])
    vogais = ''
    for v in range(0, len(p)):
        if p[v].upper() in 'AEIOU':
            vogais += p[v]+' '
    print(f'Na palavra {p.upper()} temos {vogais}')
