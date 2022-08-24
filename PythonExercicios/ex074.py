from random import randint
numal = (randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60))
print(f'Os números gerados foram: {numal}')
mev = mav = 0
for c in range(0, len(numal)):
    if c == 0:
        mev = numal[c]
        mav = numal[c]
    elif numal[c] > mav:
        mav = numal[c]
    elif numal[c] < mev:
        mev = numal[c]
print(f'O maior valor na tupla é {mav}')
print(f'O menor valor na tupla é {mev}')
