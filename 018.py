from math import radians,cos,sin,tan

# Calculando Seno, Cosseno e Tangente
ang = float(input('Digite o angulo: '))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sin(radians(ang)),cos(radians(ang)),tan(radians(ang))))
