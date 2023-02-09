import random
# Par ou Impar com o computador
while True:
    computador = random.randint(0, 10)
    jogador = int(input('\nDigite seu número: '))
    escolha = str(input('Par ou impar?  P/I ')).upper().strip()

    valor = jogador + computador
    if escolha == 'P':
        if valor % 2 == 0 :
            print(f'VOCÊ VENCEU! Computador jogou {computador}.')
        else:
            print(f'VOCÊ PERDEU! Computador jogou {computador}.')
            break

    if escolha == 'I':
        if valor % 2 == 1 :
            print(f'VOCÊ VENCEU! Computador jogou {computador}.')
        else:
            print(f'VOCÊ PERDEU! Computador jogou {computador}.')
            break
