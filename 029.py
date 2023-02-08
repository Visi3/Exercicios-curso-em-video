km = int(input('Digite a velocidade do carro: '))
# Multa o carro

if km > 80:
    print('Você foi multado! A multa é {} reais.'.format((km-80)*7))
else:
    print('Tudo ok!')