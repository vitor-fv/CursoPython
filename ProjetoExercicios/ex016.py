num = float(input('Digite um número: '))

from math import trunc
n = trunc(num)

print('O número {:.3f} tem a parte inteira {} '.format(num, n))

