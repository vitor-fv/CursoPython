import math
cat_oposto = float(input('Digite um número do Cateto Oposto: '))
cat_adj = float(input('Digite um número do Cateto Adjacente: '))
hip = math.hypot(cat_oposto, cat_adj)
print('A hipotenusa vai medir {}'.format(hip))
