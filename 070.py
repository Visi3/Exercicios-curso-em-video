print(15 * '_', end='')
print('LOJA ONLINE', end='')
print(15 * '_', )

nomeBarato = ' '
tot = totmil = barato = 0

while True:
    produto = str(input('\nNome do produto: '))
    valor = float(input('Valor do produto: R$'))

    if tot == 0 or valor < barato:
        barato = valor
        nomeBarato = produto

    if valor > 1000:
        totmil += 1

    tot += valor
    escolha = ' '

    while escolha not in 'SN':
        escolha = str(input('Quer continuar? S/N')).strip().upper()[0]
    if escolha == 'N':
        break

print(f'''\nO valor total da compra foi {tot}
Acima de mil reais: {totmil}
Produto mais barato: {nomeBarato}''')

print('{:_^40}'.format('FIM DO PROGRAMA'))
