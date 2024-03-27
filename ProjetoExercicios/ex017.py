cat_oposto = int(input('Digite um número do Cateto Oposto: '))
cat_adj = int(input('Digite um número do Cateto Adjacente: '))

from math import pow
soma = pow(cat_oposto, 2) + pow(cat_adj, 2)
from math import sqrt
raiz = sqrt(soma)
print('O valor da hipotenusa, entre os catetos {} e {} é {:.2f} '.format(cat_oposto, cat_adj, raiz))
