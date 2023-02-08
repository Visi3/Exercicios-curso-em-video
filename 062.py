termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
# Mostrar quantos termos a pessoa quiser
escolha=1
c=1
limite=10

while limite != 0:
    while c <= limite:
        print(' {} '.format(termo), end='')
        termo += razao
        c += 1

    print('\n')
    escolha = int(input('''\n\nEscolha:
    [1] Adicionar mais
    [0] Encerrar'''))
    if escolha == 1:
        limite += int(input('\nQuantos a mais você quer?'))
print('FIM')
