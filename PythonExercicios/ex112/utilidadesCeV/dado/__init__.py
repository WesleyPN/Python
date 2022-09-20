def leiaDinheiro(txt=''):
    cond = False
    val = 0

    while True:
        num = str(input(txt)).strip()

        if num.isdecimal():
            val = float(num)
            cond = True
        else:
            print(f'\033[31mERRO! "{num}" é um preço inválido!\033[m')
        if cond:
            break
    return val
