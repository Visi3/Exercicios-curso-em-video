num = int(input('Digite um número inteiro: '))
tot = 0
# Verificar se é número primo
for c in range(1,num + 1 ,1):

    if num % c == 0:
        print('\033[32m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')

if tot == 2 :
    print('\n\033[m É um número primo!'.format(num))
else:
    print('\n\033[m Não é um número primo!'.format(num))