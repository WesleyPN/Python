def voto(anoNascimento=0):
    from datetime import date
    
    anoAtual = date.today().year
    idade = anoAtual - anoNascimento
    if idade < 16:
        return f'Com {idade} anos: NÂO VOTA.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
