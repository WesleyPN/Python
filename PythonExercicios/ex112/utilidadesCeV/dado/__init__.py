def leiaDinheiro(txt=''):
    cond = False
    val = 0

    while True:
        num = str(input(txt)).replace(',', '.').strip()

        if num.isalpha() or num == '':
            print(f'\033[31mERRO! "{num}" é um preço inválido!\033[m')
        else:
            val = float(num)
            cond = True
        if cond:
            break
    return val
