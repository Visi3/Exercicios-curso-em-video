sal = float(input('Digite o seu salário: '))
# Calculando aumento de salário
if sal > 1250:
    print('Seu aumento foi de {:.2f} reais. Totalizando {:.2f} reais'.format((sal/100) * 10,sal + (sal/100) * 10))
else:
    print('Seu aumento foi de {:.2f} reais. Totalizando {:.2f} reais'.format((sal/100) * 15,sal + ((sal/100) * 15)))
