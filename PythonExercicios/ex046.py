from time import sleep
from emoji import emojize
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize(':fireworks:' * 14))
print(emojize(':fireworks: FELIZ ANO NOVO!!! :fireworks:'))
print(emojize(':fireworks:' * 14))
