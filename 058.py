from random import randint
# Advinhar o número de 0 a 10
computador = randint(0,10) # Computador pensa em um número
adivinha = -1
c = 0

print('=|=' * 11, '\nTente adivinhar o número que o computador pensou\n','=|=' * 11)

while adivinha != computador:
    adivinha = int(input('\nDigite o número:'))
    c += 1
print('Você acertou! O número pensado era {}, você precisou de {} tentativas para acertar.'.format(computador,c))