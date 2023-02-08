from random import randint
item = ('papel', 'tesoura','pedra')
computador = randint(0,2)
# Jokenpô
jogador = int(input('''0 - papel
1 - tesoura
2 - pedra'''))

print('O computador escolheu {}'.format(item[computador]))
print('O jogador escolheu {}'.format(item[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Jogada inválida')

if computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada inválida')

if computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida')

