﻿# Дано натуральное число N. Найдите значение
# выражения:
# N + NN + NNN
# N может быть любой длины.

N = int(input('Дайте натуральное число N - '))

NN = int(N**2)

NNN = int(N**3)

print(f"{N} + {NN} + {NNN} = {N+NN+NNN}")