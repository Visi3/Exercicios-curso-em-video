valor = float(input('Digte o valor normal do produto: '))
pgm = int(input('''1 - Dinheiro/Cheque
2 - Cartão à vista
3 - Parcelado em até 2x
4 - 3x ou mais no cartão\n'''))
# Gerenciador de pagamentos
if pgm == 1:
    print('Ganhou 20% de desconto! Total a pagar: {:.2f}'.format(valor - ((valor/100) * 20)))
elif pgm == 2:
    print('Ganhou 5% de desconto! Total a pagar: {:.2f}'.format(valor - ((valor/100) * 5)))
elif pgm == 3:
    print('Total a pagar: {:.2f}'.format(valor))
elif pgm == 4:
    print('Juros adicional de 20%! Total a pagar: {:.2f}'.format(valor + ((valor/100) * 20)))
else:
    print('Forma de pagamento incorreta!')
