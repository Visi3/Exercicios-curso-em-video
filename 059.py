n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
escolha = 0
# Menu de escolhas
print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')

while escolha != 5:
    escolha = int(input('\nDigite sua escolha: '))

    if escolha == 1:
        print('A soma dos números é {} '.format(n1 + n2))
    elif escolha == 2:
        print('A multiplicação dos números é {} '.format(n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            print('O maior número é {} '.format(n1))
        else:
            print('O maior é {} '.format(n2))
    elif escolha == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
print('\nFIM')
