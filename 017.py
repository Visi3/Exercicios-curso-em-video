import math
# Encontrar o cateto da hipotenusa
adj = int(input('Digite o comprimento do cateto adjacente: '))
ops = int(input('Digite o comprimento do cateto oposto: '))
hpt = pow(adj,2) + pow(ops,2)
print('O cateto da hipotenusa é {}'.format(math.sqrt(hpt)))
