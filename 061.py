termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
c = 1
# Os 10 primeiros termos de acordo com a razão
while c <= 10:
    print(' {} '.format(termo), end='')
    termo += razao
    c += 1
print('FIM')
