# Trabalhando com Módulos:
# import math = todas as funcionalidades
# from math import (variavel) = especificas funcionalidades

# math = biblioteca de matemática (ceil = arredondar pra cima / floor = pra baixo / trunc = sem arredondar)
# pow = potência (**) / sqrt = raiz quadrada / factorial = fatorial
# from math import sqrt

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))