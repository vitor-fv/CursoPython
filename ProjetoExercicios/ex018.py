import math
ang = float(input('Digite um Ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print('O ângulo {}, tem como seno: {:.2f}'.format(ang, seno))
print('O ângulo {}, tem como cosseno: {:.2f}'.format(ang, cos))
print('O ângulo {}, tem como tangente: {:.2f}'.format(ang, tg))

