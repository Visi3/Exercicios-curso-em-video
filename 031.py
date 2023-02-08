distancia = int(input('Digite a distância da viagem:'))
# Preço da passagem
if distancia > 200:
    print('O valor da passagem é {} reais!'.format(distancia * 0.45))
else:
    print('O valor da passagem é {} reais!'.format(distancia * 0.50))