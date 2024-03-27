ang = int(input('Digite um Ângulo: '))

import math

rad = math.radians(ang)
seno = math.sin(rad)
cos = math.cos(rad)
tg = math.tan(rad)

print('O ângulo {}, tem como seno: {:.2f}'.format(ang, seno))
print('O ângulo {}, tem como cosseno: {:.2f}'.format(ang, cos))
print('O ângulo {}, tem como tangente: {:.2f}'.format(ang, tg))

